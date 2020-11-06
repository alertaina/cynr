#from django.db import models
from django.contrib.postgres.fields import HStoreField
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from  django.utils.timezone import now
from django.contrib.postgres.fields import ArrayField
##########################################################################
# 1 CATEGORIAS
# Sirve para guardar categorias que luego se usan para campos del tipo choice, es decir
# en listas desplegables en las otras tablas. Definen valores posibles de algunos campos.
#-------------------------------------------------------------------------
class GruposCategorias(models.Model):
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    grupo = models.TextField(default=None,blank=False)
    class Meta:
        managed = True
        db_table = 'grupos_categorias'
class Categorias(models.Model):
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    id_grupo = models.ForeignKey(GruposCategorias,related_name='idGruposCategorias',on_delete=models.CASCADE, blank=False, null=False,db_column='id_grupo')
    categoria = models.TextField(default=None,blank=False)
    class Meta:
        managed = True
        db_table = 'categorias'
##########################################################################
# 2 INSTITUCIONES
#-------------------------------------------------------------------------
class Instituciones(models.Model):
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    razon_social = models.TextField(default=None,blank=False)
    categoria = models.TextField(default=None,blank=False)
    presentacion = models.TextField(default=None,null=True,blank=True)
    pag_web = models.TextField(default=None,null=True,blank=True)
    logo = models.ImageField(upload_to='cynr_app/logos',null=True,blank=True)
    direccion = models.TextField(default=None,null=True,blank=True)
    tel = models.TextField(default=None,null=True,blank=True)
    jurisdiccion = models.TextField(default=None,null=True,blank=True)
    class Meta:
        managed = True
        db_table = 'instituciones'

##########################################################################
# 3 DOC INSTITUCIONES
#-------------------------------------------------------------------------
##########################################################################
class DocInstituciones(models.Model):
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    id_inst = models.ManyToManyField(Instituciones) # crea otra tabla. un doc puede hacer referencia a varias instituciones
    doc = models.TextField(default=None,blank=True)
    conclusion = models.TextField(default=None,blank=True)
    class Meta:
        managed = True
        db_table = 'doc_instituciones'  

##########################################################################
# 4 CONTACTOS REGISTRADOS
#-------------------------------------------------------------------------
class Contactos(models.Model):
    # relacion uno a uno con los usuarios registrados
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_inst = models.ForeignKey(Instituciones,related_name='idInstitucion',on_delete=models.CASCADE,db_column='id_inst')
    nombre_cont = models.TextField(default=None,blank=False)
    apellido_cont = models.TextField(default=None,blank=False)
    cargo = models.TextField(default=None,blank=True)
    dir_inst = models.TextField(default=None,blank=True)
    tel_inst = models.TextField(default=None,blank=True)
    email_inst = models.TextField(default=None,blank=True)
    class Meta:
        managed = True
        db_table = 'contactos'

##########################################################################
# 5 INFRAESTRUCTURA
#-------------------------------------------------------------------------
class Infraestructura(models.Model):
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    categoria = models.TextField(default=None,blank=False)
    nombre = models.TextField(default=None,blank=False)
    descripcion = models.TextField(default=None,blank=True)    
    geom = models.GeometryField(blank=True, null=True)
    # file will be uploaded to MEDIA_ROOT / uploads 
    ficha_tec = models.FileField(upload_to ='fichas_tecnicas/')
    class Meta:
        managed = True
        db_table = 'infraestructura'
##########################################################################
# 6 OBRAS DE TOMA
#-------------------------------------------------------------------------
class ObrasToma(models.Model):
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    id_infra = models.ForeignKey(Infraestructura,related_name='idInfra',on_delete=models.CASCADE, blank=False,db_column='id_infra')
    tipo =  models.TextField(blank=False, null=False) # LISTA DESPLEGABLE
    funcionamiento = models.TextField(blank=False, null=False)# LISTA DESPLEGABLE
    uso = models.TextField(blank=False, null=False)# LISTA DESPLEGABLE
    estado = models.TextField(blank=False, null=False)# LISTA DESPLEGABLE
    desc_estado = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'obras_toma'

##########################################################################
# 7 COTAS Y NIVELES DE REFERENCIA
#-------------------------------------------------------------------------
class CyNR(models.Model):
   autor = models.ForeignKey(User,on_delete=models.CASCADE)
   id = models.AutoField(primary_key=True)
   unid_meteo_est = models.IntegerField(blank=True, null=True) # unid de la etacion en la base Meteorology
   id_infra = models.ForeignKey(Infraestructura,related_name='idInfraCyN',on_delete=models.CASCADE, blank=False, null=False,db_column='id_infra')    
   referencia = models.TextField(blank=False, null=False) # Ej Cota Sum Min Bomba1 Est Hernández
   valor = models.FloatField(blank=False, null=False)
   descripcion = models.TextField(blank=False, null=False)
   class Meta:
       managed = True
       db_table = 'cynr'

##########################################################################
# 8 DOCUMENTOS
#-------------------------------------------------------------------------
class Documentos(models.Model):
    autor = models.ForeignKey(User,on_delete=models.CASCADE)    
    id = models.AutoField(primary_key=True)
    id_infra = models.ForeignKey(Infraestructura,related_name='idInfraDoc',on_delete=models.CASCADE, blank=False,db_column='id_infra')
    id_cynr =  models.ForeignKey(Infraestructura,related_name='idCyNRDoc',on_delete=models.CASCADE, blank=False,db_column='id_cynr')
    categoria = models.TextField(default=None,blank=False)
    titulo = models.TextField(default=None,blank=False)
    descripcion = models.TextField(default=None,blank=True)
    documento = models.JSONField()
    class Meta:
        managed = True
        db_table = 'documentos'

##########################################################################
# 9 ARCHIVOS
#-------------------------------------------------------------------------
class Archivos(models.Model):
    autor = models.ForeignKey(User,on_delete=models.CASCADE)    
    id = models.AutoField(primary_key=True)
    categoria = models.TextField(default=None,blank=False)
    # file will be uploaded to MEDIA_ROOT / uploads 
    archivo = models.FileField(upload_to ='archivos/')
    class Meta:
        managed = True
        db_table = 'archivos'

##########################################################################
# 10 NOTICIAS
#-------------------------------------------------------------------------
