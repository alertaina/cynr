from .models import *
##########################################################################
# CONTENIDO PARA LAS PÁGINAS
#-------------------------------------------------------------------------


# PÁGINA INSTITUCIONES -----------------------------------------------------------------------------
# Datos para la Tabla
querysetPagInst= Instituciones.objects.all().order_by('nombre').values('autor__username','id','nombre','categoria','jurisdiccion')
contextoPagInst ={
                    'titulo': 'Instituciones',
                    'encabezados':['Autor','Nombre','Categoria','Jurisdicción'],
                    'url_crear':'cynr_app:instituciones_crud_crear',
                    'url_editar':'cynr_app:instituciones_crud_editar',
                    'url_eliminar':'cynr_app:instituciones_crud_eliminar'
                 }   
# --------------------------------------------------------------------------------------------------

# PÁGINA DOC INSTITUCIONES -----------------------------------------------------------------------------
# Datos para la Tabla
querysetPagDocInst= DocInstitucionales.objects.all().values('autor__username','id','nombre','presentacion','categoria','jurisdiccion')
contextoDocPagInst ={
                    'titulo': 'Documentos Institucionales',
                    'encabezados':['Autor','Nombre','Presenttación','Categoría','Jurisdicción'],
                    'url_crear':'cynr_app:doc_instituciones_crud_crear',
                    'url_editar':'cynr_app:doc_instituciones_crud_editar',
                    'url_eliminar':'cynr_app:doc_instituciones_crud_eliminar'
                 }   
# --------------------------------------------------------------------------------------------------

# PÁGINA INFRAESTRUCTURA -----------------------------------------------------------------------------
# Datos para la Tabla
querysetInfraestructura= Infraestructura.objects.all().order_by('nombre').values('autor__username','id','categoria','nombre','descripcion','id_inst__nombre')
contextoInfraestructura ={
                    'titulo': 'Infraestructura',
                    'encabezados':['Autor','Categoría','Nombre','Descripción','Institución'],
                    'url_crear':'cynr_app:infraestructura_crud_crear',
                    'url_editar':'cynr_app:infraestructura_crud_editar',
                    'url_eliminar':'cynr_app:infraestructura_crud_eliminar'
                 }   
# --------------------------------------------------------------------------------------------------

# PÁGINA OBRAS DE TOMA -----------------------------------------------------------------------------
# Datos para la Tabla
querysetObraToma= ObrasToma.objects.all().order_by('id_infra__nombre').values('autor__username','id','id_infra__nombre','estado')
contextoObraToma ={
                    'titulo': 'Obras de Toma',
                    'encabezados':['Autor','Nombre','Estado'],
                    'url_crear':'cynr_app:obra_de_toma_crud_crear',
                    'url_editar':'cynr_app:obra_de_toma_crud_editar',
                    'url_eliminar':'cynr_app:obra_de_toma_crud_eliminar'
                 }   
# --------------------------------------------------------------------------------------------------

# PÁGINA OBRAS DE TOMA -----------------------------------------------------------------------------
# Datos para la Tabla
querysetCyNR= CyNR.objects.all().order_by('id_infra__nombre').values('autor__username','id','id_infra__nombre','referencia','valor','unid_meteo_est')
contextoCyNR ={
                    'titulo': 'Cotas y Niveles de Referencia',
                    'encabezados':['Autor','Infraestructura','referencia','valor','Id Estación'],
                    'url_crear':'cynr_app:cynr_crud_crear',
                    'url_editar':'cynr_app:cynr_crud_editar',
                    'url_eliminar':'cynr_app:cynr_crud_eliminar'
                 }   
# --------------------------------------------------------------------------------------------------

# PÁGINA DOCUEMNTOS -----------------------------------------------------------------------------
# Datos para la Tabla
querysetDoc= Documentos.objects.all().order_by('id_infra__nombre').values('autor__username','id','id_infra__nombre','categoria','titulo','descripcion')
contextoDoc ={
                    'titulo': 'Documentos',
                    'encabezados':['Autor','Infraestructura','Categoria','Titulo','Descripción'],
                    'url_crear':'cynr_app:documentos_crud_crear',
                    'url_editar':'cynr_app:documentos_crud_editar',
                    'url_eliminar':'cynr_app:documentos_crud_eliminar'
                 }   
# --------------------------------------------------------------------------------------------------

# PÁGINA GEOMANIO -----------------------------------------------------------------------------
contextoGeomanio ={
                    'titulo': 'Geomanio.io',
                  }