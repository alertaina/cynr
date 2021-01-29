# Generated by Django 3.1.2 on 2020-12-28 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cynr_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenes',
            name='id_cont',
            field=models.ForeignKey(db_column='id_cont', on_delete=django.db.models.deletion.CASCADE, related_name='idContImg', to='cynr_app.contdocumentos', verbose_name='Archivo'),
        ),
        migrations.AlterField(
            model_name='instituciones',
            name='categoria',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
