# Generated by Django 2.1.3 on 2018-12-12 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cursos', '0011_auto_20181212_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='antepenultimo_anio',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='penultimo_anio',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='ultimo_anio',
            field=models.IntegerField(null=True),
        ),
    ]