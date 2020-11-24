#from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from  django.utils.timezone import now

##########################################################################
# 1 CATEGORIAS
# Sirve para guardar categorias que luego se usan para campos del tipo choice, es decir
# en listas desplegables en las otras tablas. Definen valores posibles de algunos campos.
#-------------------------------------------------------------------------
class GruposCategorias(models.Model):
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    grupo = models.TextField(blank=False,verbose_name='Grupo Categoría')

    def __str__(self):
        return self.grupo

    class Meta:
        managed = True
        db_table = 'grupos_categorias'

class Categorias(models.Model):
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    id_grupo = models.ForeignKey(GruposCategorias,related_name='idGruposCategorias',on_delete=models.CASCADE, blank=False,db_column='id_grupo')
    categoria = models.TextField(blank=False,verbose_name='Categoría')

    def __str__(self):
        return self.categoria

    class Meta:
        managed = True
        db_table = 'categorias'
##########################################################################
# 2 INSTITUCIONES
#-------------------------------------------------------------------------
class Instituciones(models.Model):
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200,default=None,blank=False,verbose_name='Nombre')
    categoria = models.CharField(max_length=50,default=None,blank=False)
    presentacion = models.TextField(default=None,blank=True,verbose_name='Presentación')
    pag_web = models.URLField(max_length = 200,blank=True,verbose_name='Página Web')
    logo = models.ImageField(upload_to='cynr_app/logos',blank=True,verbose_name='Logo')
    direccion = models.CharField(max_length=200,default=None,blank=False,verbose_name='Dirección')
    tel = models.CharField(max_length=50,default=None,blank=False,verbose_name='Teléfono')
    jurisdiccion = models.CharField(max_length=200,default=None,blank=False,verbose_name='Jurisdicción')
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        managed = True
        db_table = 'instituciones'

##########################################################################
# 3 DOCUMENTOS INSTITUCIONALES
#-------------------------------------------------------------------------
# Documentos Institucionales, Leyes y Normas
class DocInstitucionales(models.Model):
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200,default=None,blank=False,verbose_name='Nombre')
    presentacion = models.TextField(default=None,blank=True,verbose_name='Presentación')
    id_inst = models.ForeignKey(Instituciones,default=None, related_name='idDocInstitucion',null=True,on_delete=models.SET_NULL,db_column='id_inst') # Generador del documento
    categoria = models.CharField(max_length=50,default=None,blank=False,verbose_name='Categoria')
    link_doc = models.URLField(max_length = 200,blank=True,verbose_name='Link Documento')
    arch_doc = models.FileField(upload_to='cynr_app/doc_instituciones', max_length=200, blank=True, verbose_name='Archivo')
    jurisdiccion = models.CharField(max_length=200,default=None,blank=False,verbose_name='Jurisdicción')

    def __str__(self):
        return self.nombre

    class Meta:
        managed = True
        db_table = 'doc_institucionales'  


##########################################################################
# 4 CONTACTOS REGISTRADOS
#-------------------------------------------------------------------------
class Contactos(models.Model):
    # relacion uno a uno con los usuarios registrados
    user = models.OneToOneField(User,related_name='contacto_user', on_delete=models.CASCADE)
    id_inst = models.ForeignKey(Instituciones,related_name='idContInstitucion',on_delete=models.CASCADE,db_column='id_inst')
    cargo = models.CharField(max_length=200,default=None,blank=True,verbose_name='Cargo')
    dir_inst = models.CharField(max_length=200,default=None,blank=True,verbose_name='Dirección Institucional')
    tel_inst = models.CharField(max_length=50,default=None,blank=True,verbose_name='Teléfono Institucional')
    email_inst = models.CharField(max_length = 50,default=None,blank=True,verbose_name='Email Institucional')

    def __str__(self):
        return self.user__username

    class Meta:
        managed = True
        db_table = 'contactos'

##########################################################################
# 5 INFRAESTRUCTURA
#-------------------------------------------------------------------------
class Infraestructura(models.Model):
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=50,default=None,blank=False,verbose_name='Categoria')
    nombre = models.CharField(max_length=200,default=None,blank=False,verbose_name='Nombre')
    descripcion = models.TextField(default=None,blank=True,verbose_name='Descripción')    
    geom = models.GeometryField(null=True,verbose_name='Georreferenciación',srid=4326)
    #geom2 = models.GeometryCollectionField(default=None,null=True,verbose_name='Georreferenciación Coleccion',srid=4326)
    id_inst = models.ForeignKey(Instituciones,related_name='idInfInstitucion',null=True,on_delete=models.SET_NULL,blank=True,db_column='id_inst')
    # file will be uploaded to MEDIA_ROOT / uploads 
    ficha_tec = models.FileField(upload_to ='fichas_tecnicas/',blank=True)
 
    def __str__(self):
        return self.nombre
 
    class Meta:
        managed = True
        db_table = 'infraestructura'
##########################################################################
# 6 OBRAS DE TOMA
#-------------------------------------------------------------------------
class ObrasToma(models.Model):
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    id_infra = models.ForeignKey(Infraestructura,related_name='idObrTomaInfra',on_delete=models.CASCADE, blank=False,db_column='id_infra')
    tipo =  models.CharField(max_length=200,blank=False,verbose_name='Tipo') # LISTA DESPLEGABLE
    funcionamiento = models.CharField(max_length=200,blank=False,verbose_name='Funcionamiento')# LISTA DESPLEGABLE
    uso = models.CharField(max_length=200,blank=False,verbose_name='Uso')# LISTA DESPLEGABLE
    estado = models.CharField(max_length=200,blank=False,verbose_name='Estado')# LISTA DESPLEGABLE
    desc_estado = models.TextField(default=None,blank=True,verbose_name='Descripción Estado')   # Descripción del estado

    class Meta:
        managed = True
        db_table = 'obras_toma'

##########################################################################
# 7 COTAS Y NIVELES DE REFERENCIA
#-------------------------------------------------------------------------
class CyNR(models.Model):
   autor = models.ForeignKey(User,on_delete=models.CASCADE)
   id = models.AutoField(primary_key=True)
   unid_meteo_est = models.IntegerField(null=True,blank=True,verbose_name='Estación SIyAH') # unid de la etacion en la base Meteorology
   id_infra = models.ForeignKey(Infraestructura,related_name='idInfraCyN',on_delete=models.CASCADE, blank=False,db_column='id_infra')    
   referencia = models.TextField(blank=False,verbose_name='Referencia') # Ej Cota Sum Min Bomba1 Est Hernández
   valor = models.FloatField(blank=False)
   descripcion = models.TextField(blank=False, null=False)

   def __str__(self):
        return '{}@{}'.format(self.id_infra.nombre, self.referencia)

   class Meta:
       managed = True
       db_table = 'cynr'

##########################################################################
# 8 DOCUMENTOS
#-------------------------------------------------------------------------
class Documentos(models.Model):
    autor = models.ForeignKey(User,on_delete=models.CASCADE)    
    id = models.AutoField(primary_key=True)
    id_infra = models.ForeignKey(Infraestructura,related_name='idInfraDoc',on_delete=models.CASCADE,null=True, blank=False,db_column='id_infra',verbose_name='Infraestructura')
    id_cynr =  models.ForeignKey(CyNR,related_name='idCyNRDoc',on_delete=models.CASCADE,null=True, blank=False,db_column='id_cynr',verbose_name='CyNR')
    categoria = models.TextField(default=None,blank=False)
    titulo = models.TextField(default=None,blank=False)
    descripcion = models.TextField(default=None,blank=True)
    documento = models.JSONField() #Por ahi vuela

    def __str__(self):
        return self.titulo

    class Meta:
        managed = True
        db_table = 'documentos'


   

##########################################################################
# 9 ARCHIVOS CONTENIDOS DOCUMENTOS
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
class Noticias(models.Model):
    autor = models.ForeignKey(User,on_delete=models.CASCADE)    
    id = models.AutoField(primary_key=True)
    id_inst = models.ForeignKey(Instituciones,related_name='idNotInstitucion',null=True,on_delete=models.SET_NULL,blank=True,db_column='id_inst')   
    encabezado = models.CharField(max_length=200,default=None,blank=False,verbose_name='Encabezado')
    presentacion = models.TextField(default=None,blank=True,verbose_name='Presentación')
    fecha_hora = models.DateTimeField(null=True,blank=True)
    link_not = models.URLField(max_length = 200,blank=True,verbose_name='Link Noticia')
    arch_not = models.FileField(upload_to='cynr_app/noticias', max_length=200, blank=True, verbose_name='Archivo Noticia')  

    def __str__(self):
        return self.encabezado
    class Meta:
        managed = True
        db_table = 'noticias'   
##########################################################################
# 11 OBSERVACIONES
#-------------------------------------------------------------------------
# Se formulan en función de la información obtenida; Documentos institucionales, entevistas, informes, Cotas y Niveles.



