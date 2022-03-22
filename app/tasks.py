from celery import shared_task

from barcode import main as mn
from image_crop import withOCR as oc

from .models import PdfTable, OrderDetails

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
                    OrderDetails.objects.create(pdftable=pdf_query, code=okok[0], type_design=okok[1], colour=okok[2])

    pdf_query.status = 1
    pdf_query.save()

    try:
        shutil.rmtree('movable')
        shutil.rmtree('image_dir')
        shutil.rmtree('text_ocr')
    except Exception as e:
        print(e)

    return self.request.id
