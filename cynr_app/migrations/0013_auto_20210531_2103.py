# Generated by Django 3.2 on 2021-05-31 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cynr_app', '0012_auto_20210531_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='id_infra',
            field=models.ManyToManyField(blank=True, default=None, to='cynr_app.Infraestructura'),
        ),
        migrations.AlterField(
            model_name='noticias',
            name='id_inst',
            field=models.ManyToManyField(blank=True, default=None, to='cynr_app.Instituciones'),
        ),
    ]