# Generated by Django 3.1.6 on 2021-02-18 17:39

from django.conf import settings
import django.contrib.gis.db.models.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrusel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('encabezado', models.CharField(default=None, max_length=250, verbose_name='Encabezado')),
                ('texto', models.TextField(default=None, verbose_name='Texto')),
                ('leer_mas_link', models.URLField(blank=True, max_length=500, verbose_name='Link Leer Más')),
            ],
            options={
                'db_table': 'carrusel',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Contactos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, default=None, max_length=250, verbose_name='Nombre')),
                ('apellido', models.CharField(blank=True, default=None, max_length=250, verbose_name='Apellido')),
                ('tel_particular', models.CharField(blank=True, default=None, max_length=250, verbose_name='Telefono Paricular')),
                ('email_particular', models.EmailField(blank=True, default=None, max_length=254, verbose_name='Email Particular')),
                ('institucion_no_reg', models.CharField(blank=True, default=None, max_length=250, verbose_name='Institución no Registrada')),
                ('cargo', models.CharField(blank=True, default=None, max_length=250, verbose_name='Cargo')),
                ('dir_inst', models.CharField(blank=True, default=None, max_length=250, verbose_name='Dirección Institucional')),
                ('tel_inst', models.CharField(blank=True, default=None, max_length=100, verbose_name='Teléfono Institucional')),
                ('email_inst', models.EmailField(blank=True, default=None, max_length=250, verbose_name='Email Institucional')),
            ],
            options={
                'db_table': 'contactos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ContDocumentos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(default=None, max_length=250, verbose_name='Título')),
                ('contenido', models.TextField(default=None, verbose_name='Contenido')),
                ('autor_id', models.ForeignKey(db_column='autor_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'cont_documentos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Infraestructura',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('categoria', models.CharField(default=None, max_length=250, verbose_name='Categoria')),
                ('nombre', models.CharField(default=None, max_length=250, verbose_name='Nombre')),
                ('descripcion', models.TextField(blank=True, default=None, verbose_name='Descripción')),
                ('geom', django.contrib.gis.db.models.fields.GeometryCollectionField(null=True, srid=4326, verbose_name='Georreferenciación')),
                ('ficha_tec', models.FileField(blank=True, upload_to='cynr_app/fichas_tecnicas/')),
                ('atributos', models.JSONField(blank=True, null=True)),
                ('autor_id', models.ForeignKey(db_column='autor_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'infraestructura',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Instituciones',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(default=None, max_length=250, verbose_name='Nombre')),
                ('categoria', models.CharField(default=None, max_length=250)),
                ('presentacion', models.TextField(blank=True, default=None, verbose_name='Presentación')),
                ('pag_web', models.URLField(blank=True, max_length=250, verbose_name='Página Web')),
                ('logo', models.ImageField(blank=True, upload_to='cynr_app/logos/', verbose_name='Logo')),
                ('direccion', models.CharField(default=None, max_length=250, verbose_name='Dirección')),
                ('tel', models.CharField(default=None, max_length=100, verbose_name='Teléfono')),
                ('alc_geografico', models.CharField(default=None, max_length=250, verbose_name='Alcance Geográfico')),
                ('autor_id', models.ForeignKey(db_column='autor_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'instituciones',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ObrasToma',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=250, verbose_name='Tipo')),
                ('funcionamiento', models.CharField(max_length=250, verbose_name='Funcionamiento')),
                ('uso', models.CharField(max_length=250, verbose_name='Uso')),
                ('estado', models.CharField(max_length=250, verbose_name='Estado')),
                ('desc_estado', models.TextField(blank=True, default=None, verbose_name='Descripción Estado')),
                ('autor_id', models.ForeignKey(db_column='autor_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('id_infra', models.ForeignKey(db_column='id_infra', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='idObrTomaInfra', to='cynr_app.infraestructura')),
            ],
            options={
                'db_table': 'obras_toma',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('encabezado', models.CharField(default=None, max_length=250, verbose_name='Encabezado')),
                ('presentacion', models.TextField(blank=True, default=None, verbose_name='Presentación')),
                ('fecha_hora', models.DateTimeField()),
                ('link_not', models.URLField(blank=True, max_length=250, verbose_name='Link Noticia')),
                ('arch_not', models.FileField(blank=True, max_length=200, upload_to='cynr_app/noticias', verbose_name='Archivo Noticia')),
                ('autor_id', models.ForeignKey(db_column='autor_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('id_infra', models.ForeignKey(blank=True, db_column='id_infra', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='idNotInfra', to='cynr_app.infraestructura', verbose_name='Infraestructura')),
                ('id_inst', models.ForeignKey(blank=True, db_column='id_inst', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='idNotInstitucion', to='cynr_app.instituciones', verbose_name='Institución')),
            ],
            options={
                'db_table': 'noticias',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='infraestructura',
            name='id_inst',
            field=models.ForeignKey(blank=True, db_column='id_inst', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='idInfInstitucion', to='cynr_app.instituciones'),
        ),
        migrations.CreateModel(
            name='Imagenes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('categoria', models.CharField(default=None, max_length=250, verbose_name='Título')),
                ('descripcion', models.TextField(default=None)),
                ('ilustracion', models.BooleanField(verbose_name='Ilustra Documento')),
                ('imagen', models.FileField(upload_to='imagenes/')),
                ('autor_id', models.ForeignKey(db_column='autor_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('id_cont', models.ForeignKey(db_column='id_cont', on_delete=django.db.models.deletion.CASCADE, related_name='idContImg', to='cynr_app.contdocumentos', verbose_name='Archivo')),
            ],
            options={
                'db_table': 'imagenes',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GruposCategorias',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('grupo', models.CharField(default=None, max_length=250, verbose_name='Grupo Categorías')),
                ('autor_id', models.ForeignKey(db_column='autor_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'grupos_categorias',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Documentos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('categoria', models.CharField(default=None, max_length=250, verbose_name='Categoria')),
                ('titulo', models.CharField(default=None, max_length=250, verbose_name='Título')),
                ('descripcion', models.TextField(blank=True, default=None)),
                ('fecha_hora', models.DateTimeField()),
                ('autor_id', models.ForeignKey(db_column='autor_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('id_contacto', models.ForeignKey(blank=True, db_column='id_contacto', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='idContDoc', to='cynr_app.contactos', verbose_name='Entrevistado')),
            ],
            options={
                'db_table': 'documentos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DocInstitucionales',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(default=None, max_length=250, verbose_name='Nombre')),
                ('presentacion', models.TextField(blank=True, default=None, verbose_name='Presentación')),
                ('categoria', models.CharField(default=None, max_length=250, verbose_name='Categoria')),
                ('link_doc', models.URLField(blank=True, max_length=250, verbose_name='Link Documento')),
                ('arch_doc', models.FileField(blank=True, max_length=250, upload_to='cynr_app/doc_instituciones', verbose_name='Archivo')),
                ('alc_geografico', models.CharField(default=None, max_length=250, verbose_name='Alcance Geográfico')),
                ('autor_id', models.ForeignKey(db_column='autor_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('id_inst', models.ForeignKey(db_column='id_inst', default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='idDocInstitucion', to='cynr_app.instituciones')),
            ],
            options={
                'db_table': 'doc_institucionales',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CyNR',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('unid_meteo_est', models.IntegerField(blank=True, null=True, verbose_name='Estación SIyAH')),
                ('referencia', models.CharField(max_length=250, verbose_name='Referencia')),
                ('valor', models.FloatField(null=True)),
                ('condicion', models.IntegerField(choices=[(1, 'menor que referencia'), (2, 'mayor que referencia')], verbose_name='Condicion')),
                ('probabilidad', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0, message='El valor debe ser mayor o igual a 0'), django.core.validators.MaxValueValidator(1.0, message='El valor debe ser menor o igual a 1')], verbose_name='Probabilidad')),
                ('descripcion', models.TextField()),
                ('autor_id', models.ForeignKey(db_column='autor_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('id_infra', models.ForeignKey(db_column='id_infra', on_delete=django.db.models.deletion.CASCADE, related_name='idInfraCyN', to='cynr_app.infraestructura')),
            ],
            options={
                'db_table': 'cynr',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='contdocumentos',
            name='id_cynr',
            field=models.ForeignKey(blank=True, db_column='id_cynr', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='idCynrDocCont', to='cynr_app.cynr', verbose_name='Cota o Nivel'),
        ),
        migrations.AddField(
            model_name='contdocumentos',
            name='id_doc',
            field=models.ForeignKey(db_column='id_doc', on_delete=django.db.models.deletion.CASCADE, related_name='idContDoc', to='cynr_app.documentos', verbose_name='Documento'),
        ),
        migrations.AddField(
            model_name='contdocumentos',
            name='id_infra',
            field=models.ForeignKey(blank=True, db_column='id_infra', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='idInfraDocCont', to='cynr_app.infraestructura', verbose_name='Infraestructura'),
        ),
        migrations.AddField(
            model_name='contactos',
            name='id_inst',
            field=models.ForeignKey(blank=True, db_column='id_inst', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='idContInstitucion', to='cynr_app.instituciones'),
        ),
        migrations.AddField(
            model_name='contactos',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contacto_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('categoria', models.CharField(default=None, max_length=250, verbose_name='Categoría')),
                ('autor_id', models.ForeignKey(db_column='autor_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('id_grupo', models.ForeignKey(db_column='id_grupo', on_delete=django.db.models.deletion.CASCADE, related_name='idGruposCategorias', to='cynr_app.gruposcategorias')),
            ],
            options={
                'db_table': 'categorias',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CapasGeoJson',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(default=None, max_length=250, verbose_name='Título')),
                ('descripcion', models.TextField(blank=True, default=None)),
                ('fecha_hora', models.DateTimeField(blank=True, null=True)),
                ('capa', models.JSONField()),
                ('autor_id', models.ForeignKey(db_column='autor_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Archivos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('categoria', models.CharField(default=None, max_length=250, verbose_name='Título')),
                ('descripcion', models.TextField(blank=True, default=None)),
                ('archivo', models.FileField(upload_to='archivos/')),
                ('autor_id', models.ForeignKey(db_column='autor_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('id_cont', models.ForeignKey(db_column='id_cont', on_delete=django.db.models.deletion.CASCADE, related_name='idContArch', to='cynr_app.documentos', verbose_name='Archivo')),
            ],
            options={
                'db_table': 'archivos',
                'managed': True,
            },
        ),
    ]
