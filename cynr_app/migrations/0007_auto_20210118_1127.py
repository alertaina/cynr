# Generated by Django 2.1.5 on 2021-01-18 11:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cynr_app', '0006_auto_20210118_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactos',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contacto_user', to=settings.AUTH_USER_MODEL),
        ),
    ]