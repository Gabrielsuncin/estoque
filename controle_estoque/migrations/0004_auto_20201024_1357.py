# Generated by Django 3.1.1 on 2020-10-24 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_estoque', '0003_auto_20201020_1923'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='categoria',
            table='categoria',
        ),
        migrations.AlterModelTable(
            name='fornecedor',
            table='fornecedor',
        ),
        migrations.AlterModelTable(
            name='funcionario',
            table='funcionario',
        ),
        migrations.AlterModelTable(
            name='genero',
            table='genero',
        ),
        migrations.AlterModelTable(
            name='subcategoria',
            table='subcategoria',
        ),
    ]