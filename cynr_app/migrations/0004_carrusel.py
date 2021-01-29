# Generated by Django 2.1.5 on 2021-01-14 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cynr_app', '0003_auto_20210112_1105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrusel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('encabezado', models.CharField(default=None, max_length=250, verbose_name='Encabezado')),
                ('texto', models.TextField(default=None, verbose_name='Texto')),
            ],
            options={
                'db_table': 'carrusel',
                'managed': True,
            },
        ),
    ]