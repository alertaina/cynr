# Generated by Django 3.1.7 on 2021-03-31 11:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cynr_app', '0003_auto_20210331_1036'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='atributospordefectoinfra',
            options={'managed': True},
        ),
        migrations.AlterField(
            model_name='atributospordefectoinfra',
            name='autor_id',
            field=models.ForeignKey(blank=True, db_column='autor_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterModelTable(
            name='atributospordefectoinfra',
            table='atributos_def_infra',
        ),
    ]
