# Generated by Django 4.0.3 on 2022-05-09 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_orderdetailsfinal_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='photo',
            field=models.ImageField(blank=True, default='default', null=True, upload_to='photos/table_photo'),
        ),
    ]