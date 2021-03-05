#from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from  django.utils.timezone import now

from django.core.validators import MaxValueValidator, MinValueValidator

##########################################################################
# 1 CATEGORIAS
# Sirve para guardar categorias que luego se usan para campos del tipo choice, es decir
# en listas desplegables en las otras tablas. Definen valores posibles de algunos campos.
#-------------------------------------------------------------------------
class GruposCategorias(models.Model):
    autor_id = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,db_column='autor_id')
    id = models.AutoField(primary_key=True)
    grupo = models.CharField(max_length=250,default=None,blank=False,verbose_name='Grupo Categorías')

    def __str__(self):
        return self.grupo

    class Meta:
        managed = True
        db_table = 'grupos_categorias'

class Categorias(models.Model):
    autor_id = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,db_column='autor_id')
    id = models.AutoField(primary_key=True)
    id_grupo = models.ForeignKey(GruposCategorias,related_name='idGruposCategorias',on_delete=models.CASCADE,null=False, blank=False,db_column='id_grupo')
    categoria = models.CharField(max_length=250,default=None,blank=False,verbose_name='Categoría')

    def __str__(self):
        return self.categoria

    class Meta:
        managed = True
        db_table = 'categorias'
##########################################################################
# 2 INSTITUCIONES
#-------------------------------------------------------------------------
# ADMINISTRADORES Y COLABORADORES
#---------------------------------
class Instituciones(models.Model):
    autor_id = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,db_column='autor_id')
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250,default=None,blank=False,verbose_name='Nombre')
    categoria = models.CharField(max_length=250,default=None,blank=False)
    presentacion = models.TextField(default=None,blank=True,verbose_name='Presentación')
    pag_web = models.URLField(max_length = 250,blank=True,verbose_name='Página Web')
    logo = models.ImageField(upload_to='logos/',default='logos_defecto/instituciones.jpg', blank=True,verbose_name='Logo')
    direccion = models.CharField(max_length=250,default=None,blank=True,verbose_name='Dirección')
    tel = models.CharField(max_length=100,default=None,blank=True,verbose_name='Teléfono')
    alc_geografico = models.CharField(max_length=250,default=None,blank=False,verbose_name='Alcance Geográfico')
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        managed = True
        db_table = 'instituciones'

##########################################################################
# 3 DOCUMENTOS INSTITUCIONALES
#-------------------------------------------------------------------------
# Documentos Institucionales, Leyes y Normas
# ADMINISTRADORES Y COLABORADORES
#---------------------------------
class DocInstitucionales(models.Model):
    autor_id = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,db_column='autor_id')
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250,default=None,blank=False,verbose_name='Nombre')
    presentacion = models.TextField(default=None,blank=True,verbose_name='Presentación')
    id_inst = models.ForeignKey(Instituciones,default=None, related_name='idDocInstitucion',null=True,on_delete=models.SET_NULL,db_column='id_inst') # Generador del documento
    categoria = models.CharField(max_length=250,default=None,blank=False,verbose_name='Categoria')
    link_doc = models.URLField(max_length = 250,blank=True,verbose_name='Link Documento')
    arch_doc = models.FileField(upload_to='cynr_app/doc_instituciones', max_length=250, blank=True, verbose_name='Archivo')
    alc_geografico = models.CharField(max_length=250,default=None,blank=False,verbose_name='Alcance Geográfico')

    def __str__(self):
        return self.nombre

    class Meta:
        managed = True
        db_table = 'doc_institucionales'  


##########################################################################
# 4 CONTACTOS REGISTRADOS Y NO REGISTRADOS
#-------------------------------------------------------------------------
class Contactos(models.Model):
    # relacion uno a uno con los usuarios registrados
    user = models.OneToOneField(User,related_name='contacto_user',null=True, blank=True, on_delete=models.SET_NULL)
    nombre = models.CharField(max_length=250,default=None,blank=True,verbose_name='Nombre')
    apellido = models.CharField(max_length=250,default=None,blank=True,verbose_name='Apellido')
    tel_particular = models.CharField(max_length=250,default=None,blank=True,verbose_name='Telefono Paricular')
    email_particular = models.EmailField(max_length=254,default=None,blank=True,verbose_name='Email Particular')
    institucion_no_reg = models.CharField(max_length=250,default=None,blank=True,verbose_name='Institución no Registrada')
    id_inst = models.ForeignKey(Instituciones,related_name='idContInstitucion',null=True,blank=True,on_delete=models.SET_NULL,db_column='id_inst')
    cargo = models.CharField(max_length=250,default=None,blank=True,verbose_name='Cargo')
    dir_inst = models.CharField(max_length=250,default=None,blank=True,verbose_name='Dirección Institucional')
    tel_inst = models.CharField(max_length=100,default=None,blank=True,verbose_name='Teléfono Institucional')
    email_inst = models.EmailField(max_length=250,default=None,blank=True,verbose_name='Email Institucional')

    def __str__(self):
        if self.user:
            return self.user.username
        else:
            pass
            return '{} {}'.format(self.nombre, self.apellido)

    class Meta:
        managed = True
        db_table = 'contactos'


##########################################################################
# 5 INFRAESTRUCTURA
#-------------------------------------------------------------------------
# ADMINISTRADORES Y COLABORADORES
#---------------------------------
class Infraestructura(models.Model):
    autor_id = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,db_column='autor_id')
    id = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=250,default=None,blank=False,verbose_name='Categoria')
    nombre = models.CharField(max_length=250,default=None,blank=False,verbose_name='Nombre')
    descripcion = models.TextField(default=None,blank=True,verbose_name='Descripción')    
    geom = models.GeometryCollectionField(null=True,verbose_name='Georreferenciación',srid=4326)
    id_inst = models.ForeignKey(Instituciones,related_name='idInfInstitucion',null=True,on_delete=models.SET_NULL,blank=True,db_column='id_inst')
    # file will be uploaded to MEDIA_ROOT / uploads 
    ficha_tec = models.FileField(upload_to ='cynr_app/fichas_tecnicas/',blank=True)
    atributos =  models.JSONField(null=True,blank=True) # permite cargar atributos en formato json
    def __str__(self):
        return self.nombre
 
    class Meta:
        managed = True
        db_table = 'infraestructura'
##########################################################################
# 6 OBRAS DE TOMA
#-------------------------------------------------------------------------
class ObrasToma(models.Model):
    autor_id = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,db_column='autor_id')
    id = models.AutoField(primary_key=True)
    id_infra = models.ForeignKey(Infraestructura,related_name='idObrTomaInfra',null=True,on_delete=models.SET_NULL, blank=False,db_column='id_infra')
    tipo =  models.CharField(max_length=250,blank=False,verbose_name='Tipo') # LISTA DESPLEGABLE
    funcionamiento = models.CharField(max_length=250,blank=False,verbose_name='Funcionamiento')# LISTA DESPLEGABLE
    uso = models.CharField(max_length=250,blank=False,verbose_name='Uso')# LISTA DESPLEGABLE
    estado = models.CharField(max_length=250,blank=False,verbose_name='Estado')# LISTA DESPLEGABLE
    desc_estado = models.TextField(default=None,blank=True,verbose_name='Descripción Estado')   # Descripción del estado

    class Meta:
        managed = True
        db_table = 'obras_toma'

##########################################################################
# 7 COTAS Y NIVELES DE REFERENCIA
#-------------------------------------------------------------------------
class CyNR(models.Model):
   condiciones = [(1,'menor que referencia'),(2,'mayor que referencia')] 
   autor_id = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,db_column='autor_id')
   id = models.AutoField(primary_key=True)
   unid_meteo_est = models.IntegerField(null=True,blank=True,verbose_name='Estación SIyAH') # unid de la etacion en la base Meteorology
   id_infra = models.ForeignKey(Infraestructura,related_name='idInfraCyN',on_delete=models.CASCADE, blank=False,db_column='id_infra')    
   referencia = models.CharField(max_length=250,blank=False,verbose_name='Referencia') # Ej Cota Sum Min Bomba1 Est Hernández
   valor = models.FloatField(null=True,blank=False)
   condicion = models.IntegerField(null = False,blank=False,choices = condiciones,verbose_name='Condicion') # 1 'menor que valor de referencia',
                                                                                                            # 2 'mayor que valor de referencia',
   probabilidad = models.FloatField(null = True,blank=True,
                                    validators=[MinValueValidator(0.0, message='El valor debe ser mayor o igual a 0'),
                                                MaxValueValidator(1.0, message= 'El valor debe ser menor o igual a 1')],
                                    verbose_name='Probabilidad')
   descripcion = models.TextField(blank=False)

   def __str__(self):
        return '{}@{}'.format(self.id_infra.nombre, self.referencia)

   class Meta:
       managed = True
       db_table = 'cynr'

##########################################################################
# 7 OBSERVACIONES DE REFERENTES LOCALES
#-------------------------------------------------------------------------
#class ObservacionesRL(model.Model):
#    autor_id = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
##########################################################################
# 8 DOCUMENTOS
#-------------------------------------------------------------------------
class Documentos(models.Model):
    autor_id = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,db_column='autor_id')    
    id = models.AutoField(primary_key=True)
    id_contacto = models.ForeignKey(Contactos,related_name='idContDoc',null=True,on_delete=models.SET_NULL, blank=True,db_column='id_contacto',verbose_name='Entrevistado')
    categoria = models.CharField(max_length=250,default=None,blank=False,verbose_name='Categoria')
    titulo = models.CharField(max_length=250,default=None,blank=False,verbose_name='Título')
    descripcion = models.TextField(default=None,blank=True)
    fecha_hora = models.DateTimeField(null=False,blank=False)
    def __str__(self):
        return self.titulo

    class Meta:
        managed = True
        db_table = 'documentos'

##########################################################################
# 9 CONTENIDO_DOCUMENTOS
#-------------------------------------------------------------------------
class ContDocumentos(models.Model):
    autor_id = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,db_column='autor_id')
    id = models.AutoField(primary_key=True)
    id_doc = models.ForeignKey(Documentos,related_name='idContDoc',on_delete=models.CASCADE,null=False, blank=False,db_column='id_doc',verbose_name='Documento')
    id_infra = models.ForeignKey(Infraestructura,related_name='idInfraDocCont',null=True,on_delete=models.SET_NULL, blank=True,db_column='id_infra',verbose_name='Infraestructura')
    id_cynr =  models.ForeignKey(CyNR,related_name='idCynrDocCont',null=True,on_delete=models.SET_NULL, blank=True,db_column='id_cynr',verbose_name='Cota o Nivel')   
    titulo = models.CharField(max_length=250,default=None,blank=False,verbose_name='Título')
    contenido = models.TextField(default=None,blank=False,verbose_name='Contenido')

    def __str__(self):
        return '{}@{}'.format(self.id_doc.titulo, self.titulo)

    class Meta:
        managed = True
        db_table = 'cont_documentos'

##########################################################################
# 10 IMAGENES CONTENIDOS DOCUMENTOS: Fotografías e imagenes
#-------------------------------------------------------------------------
class Imagenes(models.Model):
    autor_id = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,db_column='autor_id')    
    id = models.AutoField(primary_key=True)
    id_cont = models.ForeignKey(ContDocumentos,related_name='idContImg',on_delete=models.CASCADE,null=False, blank=False,db_column='id_cont',verbose_name='Archivo')
    categoria = models.CharField(max_length=250,default=None,blank=False,verbose_name='Título')
    descripcion = models.TextField(default=None,blank=False)
    ilustracion = models.BooleanField(verbose_name='Ilustra Documento' ) # para seleccionar la imagen que ilustre el documento
    # file will be uploaded to MEDIA_ROOT / uploads 
    imagen = models.FileField(upload_to ='imagenes/')

    def __str__(self):
        return self.descripcion

    class Meta:
        managed = True
        db_table = 'imagenes'



##########################################################################
# 10 ARCHIVOS CONTENIDOS DOCUMENTOS
#-------------------------------------------------------------------------
class Archivos(models.Model):
    autor_id = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,db_column='autor_id')    
    id = models.AutoField(primary_key=True)
    id_cont = models.ForeignKey(Documentos,related_name='idContArch',on_delete=models.CASCADE,null=False, blank=False,db_column='id_cont',verbose_name='Archivo')
    categoria = models.CharField(max_length=250,default=None,blank=False,verbose_name='Título')
    descripcion = models.TextField(default=None,blank=True)
    # file will be uploaded to MEDIA_ROOT / uploads 
    archivo = models.FileField(upload_to ='archivos/')

    def __str__(self):
        return self.descripcion

    class Meta:
        managed = True
        db_table = 'archivos'

##########################################################################
# 11 NOTICIAS
#-------------------------------------------------------------------------
class Noticias(models.Model):
    autor_id = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,db_column='autor_id')    
    id = models.AutoField(primary_key=True)
    id_inst = models.ForeignKey(Instituciones,related_name='idNotInstitucion',null=True,on_delete=models.SET_NULL,blank=True,db_column='id_inst',verbose_name='Institución')
    id_infra = models.ForeignKey(Infraestructura,related_name='idNotInfra',null=True,on_delete=models.SET_NULL,blank=True,db_column='id_infra',verbose_name='Infraestructura')    
    encabezado = models.CharField(max_length=250,default=None,blank=False,verbose_name='Encabezado')
    presentacion = models.TextField(default=None,blank=True,verbose_name='Presentación')
    fecha_hora = models.DateTimeField(null=False,blank=False)
    link_not = models.URLField(max_length = 250,blank=True,verbose_name='Link Noticia')
    arch_not = models.FileField(upload_to='cynr_app/noticias', max_length=200, blank=True, verbose_name='Archivo Noticia')  

    def __str__(self):
        return self.encabezado
    class Meta:
        managed = True
        db_table = 'noticias'   

##########################################################################
# 12 CAPAS GEOJSON
#-------------------------------------------------------------------------
class CapasGeoJson(models.Model):
    autor_id = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,db_column='autor_id')
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=250,default=None,blank=False,verbose_name='Título')
    descripcion = models.TextField(default=None,blank=True)
    fecha_hora = models.DateTimeField(null=True,blank=True)
    capa = models.JSONField(null=False,blank=False)    


##########################################################################
# 13 CARRUSEL DE LA PÁGINA PRINCIPAL
#-------------------------------------------------------------------------

class Carrusel(models.Model):
  id = models.AutoField(primary_key=True)
  encabezado = models.CharField(max_length=250,default=None,blank=False,verbose_name='Encabezado')
  texto = models.TextField(default=None,blank=False,verbose_name='Texto')  
  leer_mas_link = models.URLField(max_length = 500,blank=True,verbose_name='Link Leer Más')  
  def __str__(self):
    return self.encabezado
  class Meta:
    managed = True
    db_table = 'carrusel'  

##########################################################################
# 14 SECCIONES DE LA PÁGINA PRINCIPAL
#-------------------------------------------------------------------------

