# Generated by Django 3.2.4 on 2021-07-07 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_proveedor_direccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='moneda',
            field=models.ImageField(choices=[[0, 'Dolares'], [1, 'Pesos']], upload_to=''),
        ),
    ]
