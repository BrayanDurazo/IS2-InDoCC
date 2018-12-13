# Generated by Django 2.1.3 on 2018-12-12 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cursos', '0013_auto_20181212_0602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='antepenultimo_anio',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='nombre',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='numero_participantes',
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
        migrations.AlterField(
            model_name='programa',
            name='beneficios',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='programa',
            name='nombre',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
