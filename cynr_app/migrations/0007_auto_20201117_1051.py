# Generated by Django 3.1.2 on 2020-11-17 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cynr_app', '0006_auto_20201112_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentos',
            name='id_cynr',
            field=models.ForeignKey(db_column='id_cynr', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='idCyNRDoc', to='cynr_app.cynr', verbose_name='CyNR'),
        ),
        migrations.AlterField(
            model_name='documentos',
            name='id_infra',
            field=models.ForeignKey(db_column='id_infra', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='idInfraDoc', to='cynr_app.infraestructura', verbose_name='Infraestructura'),
        ),
    ]
