# Generated by Django 3.1.7 on 2021-03-31 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cynr_app', '0004_auto_20210331_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='infraestructura',
            name='id_atr_def',
            field=models.ForeignKey(blank=True, db_column='id_atr_def', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='idAtrPorDefecto', to='cynr_app.atributospordefectoinfra'),
        ),
    ]
