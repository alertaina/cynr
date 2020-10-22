#from django.db import models
from django.contrib.postgres.fields import HStoreField
from django.contrib.gis.db import models
from django.contrib.auth.models import User


##########################################################################
# ORGANISMOS
#-------------------------------------------------------------------------
class Organismos(models.Model):
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    razon_social = models.TextField(default=None,blank=False)
    presentacion = models.TextField(default=None,blank=True)
    logo = models.ImageField(upload_to='cynr_app/logos')
    ubicacion = models.TextField(default=None,blank=False)
    class Meta:
        managed = True
        db_table = 'organismos'

##########################################################################
# PRESTADORES DE SERVICIOS
#-------------------------------------------------------------------------
class PrestadoresServicios(models.Model):
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    razon_social = models.TextField(default=None,blank=False)
    presentacion = models.TextField(default=None,blank=True)
    logo = models.ImageField(upload_to='cynr_app/logos')
    ubicacion = models.TextField(default=None,blank=False)
    class Meta:
        managed = True
        db_table = 'prestadores_servicios'
##########################################################################
# CONTACTOS REGISTRADOS
#-------------------------------------------------------------------------
class Contactos(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_presserv = models.ForeignKey(PrestadoresServicios,related_name='idPresServContacto',on_delete=models.CASCADE, blank=True, null=False,db_column='id_presserv')
    id_org = models.ForeignKey(PrestadoresServicios,related_name='idOrgContacto',on_delete=models.CASCADE, blank=True, null=False,db_column='id_org')
    class Meta:
        managed = True
        db_table = 'contactos'

##########################################################################
# OBRAS DE TOMA
#-------------------------------------------------------------------------
class ObrasToma(models.Model):
    TIPOLOGIA_OBRA_TOMA =(
    ("ESTACION FIJA", "ESTACIÓN DE BOMBEO  CON BATERIA DE BOMBAS DE COTA FIJA"),
    ("PONTON", "PONTÓN : ESTACIÓN DE BOMBEO  CON BATERIA DE BOMBAS DE COTA VARIABLE SEGÚN NA"))
    SERVICIO = (("PERMANTENTE","PERMENENTE: Obra que presta un servicio permanente."),
                ("TRANSITORIA","TRANSITORIA: Obra que presta un servicio temporalmente."))
    USO = (("CONSUMO","CONSUMO"),
            ("INDUSTRIAL","INDUSTRIAL"),
            ("RIEGO","RIEGO"))            
    ESTADO = (("FUNCIONAMIENTO PLENO","FUNCIONAMIENTO PLENO: Funcionamiento sin limitaciones"),
              ("FUNCIONAMIENTO PARCIAL","FUNCIONAMIENTO PARCIAL: Funcionamiento con limitaciones "),
              ("INACTIVA","INACTIVA: Desafectada del Sevicio")
    )
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    nombre = models.TextField(default=None,blank=False)
    descripcion = models.TextField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    id_presserv = models.ForeignKey(PrestadoresServicios,related_name='idPresServObra',on_delete=models.CASCADE, blank=True, null=False,db_column='id_presserv')
    tipo =  models.TextField(blank=False, null=False,choices=TIPOLOGIA_OBRA_TOMA)
    servicio = models.TextField(blank=False, null=False,choices=SERVICIO)
    uso = models.TextField(blank=False, null=False,choices=USO)
    estado = models.TextField(blank=False, null=False,choices=ESTADO)
    cynr = HStoreField() # cotas y niveles de referencia
    class Meta:
        managed = True
        db_table = 'obras_toma'
       # constraints = [
       #     models.CheckConstraint(check=models.Q(tipo='ESTACION FIJA' | tipo ='PONTON'), name='tipologia_ot'),
       #     models.CheckConstraint(check=models.Q(servicio='PERMANENTE' | servicio ='TRANSITORIA'), name='servicio_ot'),
       #     models.CheckConstraint(check=models.Q(uso='CONSUMO' | uso ='INDUSTRIAL' | uso ='RIEGO'), name='uso_ot'),
       #     models.CheckConstraint(check=models.Q(estado='FUNCIONAMIENTO PLENO' | estado ='FUNCIONAMIENTO PARCIAL' | estado ='INACTIVA'), name='estado_ot'),
       # ]
        #db_constraints = {
        #    'tipologia': 'check (tipo=\'ESTACION FIJA\'::text OR tipo=\'PONTON\'::text)',
        #    'servicio': 'check (servicio=\'PERMANENTE\'::text OR servicio=\'TRANSITORIA\'::text)',
        #    'uso': 'check (uso=\'CONSUMO\'::text OR uso=\'INDUSTRIAL\'::text,uso=\'RIEGO\'::text)',
        #    'estado': 'check (estado=\'FUNCIONAMIENTO PLENO\'::text OR estado=\'FUNCIONAMIENTO PARCIAL\'::text,estado=\'INACTIVA\'::text)'
        #}

##########################################################################
# OBSERVACIONES
#-------------------------------------------------------------------------
class Observaciones(models.Model):
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    obs = models.JSONField()
    class Meta:
        managed = True
        db_table = 'observaciones'
##########################################################################
# ENTREVISTAS
#-------------------------------------------------------------------------
class Entrevistas(models.Model):
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    entrevista = models.JSONField()
    class Meta:
        managed = True
        db_table = 'entrevistas'
##########################################################################
# INFORMES
#-------------------------------------------------------------------------