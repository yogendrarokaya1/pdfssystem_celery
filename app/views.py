
from django.shortcuts import render, redirect
from .models import PdfTable, OrderDetails
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

    url = '/list_page/' + str(ids)

    test_func.delay(ids)
    messages.success(request, 'Pdf convert on process')

    return redirect('pdf_list_page_app')


def pdf_delete(request, ids):

    PdfTable.objects.filter(id=ids).delete()
    messages.success(request, 'Pdf deleted')

    return redirect('pdf_list_page_app')

