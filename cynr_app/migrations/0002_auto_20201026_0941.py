# Generated by Django 3.1.2 on 2020-10-26 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cynr_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='archivos',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='infraestructura',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='archivos',
            table='archivos',
        ),
        migrations.AlterModelTable(
            name='infraestructura',
            table='infraestructura',
        ),
    ]
