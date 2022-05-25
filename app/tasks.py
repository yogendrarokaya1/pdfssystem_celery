import re

from celery import shared_task

from barcode import main as mn
from image_crop import withOCR as oc
from django.core.files import File as DjangoFile

from .models import PdfTable, OrderDetails, ProductType, ProductSize, OrderDetailsFinal
from django.db.models.functions import Length
import os
import shutil


@shared_task(bind=True)
def test_func(self, ids):
    pdf_query = PdfTable.objects.get(id=ids)
    outputdir = 'movable/'
    mn.convert(pdf_query.files.path, pdf_query.title, outputdir)
    outputdir = outputdir + str(pdf_query.title)
    for file in os.listdir(outputdir):
        new_dir = outputdir + '/' + file

        final_per_obj = oc.image_crop(new_dir, str(pdf_query.title), file)

        for length in final_per_obj:
            if length[0] is not None:
                for okok in length[1]:
                    image_name = '%s_%s_%s.jpg' % (length[3], length[4], length[5])
                    file_obj1 = DjangoFile(open(length[2], mode='rb'), name=image_name)
                    OrderDetails.objects.create(barcode=length[0], pdftable=pdf_query, code=okok[0],
                                                type_design=okok[1], colour=okok[2], photo=file_obj1)

    pdf_query.status = 1
    pdf_query.save()

    product_size_query = ProductSize.objects.all().order_by(Length('title').desc())
    product_type_query = ProductType.objects.all()
    order_details_query = OrderDetails.objects.filter(status=0)
    _size = ''
    _type = ''
    for each in order_details_query:

        for item in product_size_query:
            if re.search(item.title, each.type_design):
                _size = item.size
                break

        for item in product_type_query:
            if re.search(item.title, each.type_design):
                _type = item.type
                break

        OrderDetailsFinal.objects.create(pdftable=each.pdftable, barcode=each.barcode, code=each.type_design, type=_type,
                                         size=_size, colour=each.colour, order_details=each, photo=each.photo)
        each.status = 1
        each.save()

    try:
        shutil.rmtree('movable')
        shutil.rmtree('image_dir')
        shutil.rmtree('text_ocr')
    except Exception as e:
        print(e)

    return self.request.id
