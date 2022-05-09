import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import PdfTable, OrderDetails, OrderDetailsFinal
from .tasks import test_func
from django.contrib import messages

# Create your views here.


def index(request):

    return render(request, 'index.html')


def upload(request):
    return render(request, 'upload.html')


def list_page(request, ids):
    pdf_query = PdfTable.objects.get(id=ids)
    pdf_data_query = OrderDetails.objects.filter(pdftable_id=ids)
    context = {'pdf_data_query': pdf_data_query, 'pdf_query': pdf_query}
    return render(request, 'table_list.html', context)


def final_list_page(request, ids):
    photo_list = []
    pdf_query = PdfTable.objects.get(id=ids)
    pdf_final_data_query = OrderDetailsFinal.objects.filter(pdftable_id=ids)
    for each in pdf_final_data_query:
        each_query = OrderDetails.objects.filter(id=each.order_details_id).last()
        photo_list.append(each_query.photo.url)

    data_obj = zip(pdf_final_data_query, photo_list)
    context = {'data_obj': data_obj, 'pdf_query': pdf_query}
    return render(request, 'final_list.html', context)


def pdf_list_page(request):
    pdf_query = PdfTable.objects.all()
    context = {'pdf_query': pdf_query}
    return render(request, 'pdf_list_page.html', context)


def pdf_post(request):
    if request.method == 'POST':
        pdf_file = request.FILES.get('_pdf_file')
        PdfTable.objects.create(files=pdf_file, title=pdf_file.name)

        return redirect('pdf_list_page_app')


def pdf_convert(request, ids):

    test_func.delay(ids)
    messages.success(request, 'Pdf convert on process')

    return redirect('pdf_list_page_app')


def pdf_delete(request, ids):

    PdfTable.objects.filter(id=ids).delete()
    messages.success(request, 'Pdf deleted')

    return redirect('pdf_list_page_app')


def order_details_del(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data['orderlistid']

        details_query = OrderDetailsFinal.objects.get(id=product_id)
        details_query.delete()
        return JsonResponse({'_actr': 'True'})


def order_details_update(request, ids):
    if request.method == 'POST':

        _type = request.POST.get('type')
        _colour = request.POST.get('colour')
        _size = request.POST.get('size')

        order_query = OrderDetailsFinal.objects.filter(id=ids).last()
        order_query.type = _type
        order_query.size = _size
        order_query.colour = _colour

        order_query.save()
        url = '/final_list_page/' + str(order_query.pdftable_id)
        messages.success(request, 'Order Updated!')
        return redirect(url)



