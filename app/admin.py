from django.contrib import admin
from .models import ProductSize, ProductType, PdfTable
# Register your models here.


admin.site.register(ProductSize)
admin.site.register(ProductType)
admin.site.register(PdfTable)
