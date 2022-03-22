# Generated by Django 4.0.3 on 2022-03-16 16:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PdfTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(upload_to='files/ProductPdf')),
                ('title', models.CharField(default='***', max_length=200)),
                ('date_uploaded', models.DateField(default=datetime.datetime.now)),
                ('time_uploaded', models.TimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'PdfTable',
            },
        ),
    ]