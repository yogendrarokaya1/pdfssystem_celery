from datetime import datetime

from django.db import models

# Create your models here.


class PdfTable(models.Model):
    class Meta:
        db_table = 'PdfTable'

    files = models.FileField(upload_to='files/ProductPdf')
    title = models.CharField(max_length=200, default='***')
    date_uploaded = models.DateField(default=datetime.now)
    time_uploaded = models.TimeField(default=datetime.now)
    status = models.BooleanField(default=0, help_text='0:processing, 1:completed')

    def __str__(self):
        return self.title


class OrderDetails(models.Model):
    class Meta:
        db_table = 'OrderDetails'

    pdftable = models.ForeignKey(PdfTable, on_delete=models.CASCADE, related_name="pdftable")
    code = models.CharField(max_length=200, default='***')
    type_design = models.CharField(max_length=200, default='***')
    colour = models.CharField(max_length=200, default='***')

    def __str__(self):
        return '%s %s' % (self.code, self.type_design)

