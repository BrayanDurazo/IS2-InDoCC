# Generated by Django 2.1.3 on 2018-12-06 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Procesos', '0004_auto_20181206_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proceso',
            name='evidencia',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]