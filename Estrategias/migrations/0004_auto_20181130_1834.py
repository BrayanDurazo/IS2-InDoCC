# Generated by Django 2.1.2 on 2018-11-30 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estrategias', '0003_estrategia_estrategia_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estrategia',
            name='Hay_estrategia_asignaturas',
            field=models.BinaryField(default=False),
        ),
        migrations.AlterField(
            model_name='estrategia',
            name='Hay_estrategia_posgrado',
            field=models.BinaryField(default=False),
        ),
    ]
