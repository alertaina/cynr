from .models import *
##########################################################################
# CONTENIDO PARA LAS PÁGINAS
#-------------------------------------------------------------------------


# PÁGINA INSTITUCIONES -----------------------------------------------------------------------------
# Datos para la Tabla
#querysetPagInst= Instituciones.objects.all().order_by('nombre').values('autor_id__username','id','nombre','categoria','alc_geografico')
contextoPagInst ={
                    'titulo': 'Instituciones',
                    'encabezados':['Autor','Nombre','Categoria','Alcance Geográfico'],
                    'url_crear':'cynr_app:instituciones_crud_crear',
                    'url_ver':'cynr_app:instituciones_crud_ver',
                    'url_editar':'cynr_app:instituciones_crud_editar',
                    'url_eliminar':'cynr_app:instituciones_crud_eliminar'
                 }   
# --------------------------------------------------------------------------------------------------

# PÁGINA DOC INSTITUCIONES -----------------------------------------------------------------------------
# Datos para la Tabla
#querysetPagDocInst= DocInstitucionales.objects.all().values('autor_id__username','id','nombre','presentacion','categoria','alc_geografico')
contextoDocPagInst ={
                    'titulo': 'Documentos Institucionales',
                    'encabezados':['Autor','Nombre','Institución','Categoría','Jurisdicción'],
                    'url_crear':'cynr_app:doc_instituciones_crud_crear',
                    'url_ver':'cynr_app:doc_instituciones_crud_ver',
                    'url_editar':'cynr_app:doc_instituciones_crud_editar',
                    'url_eliminar':'cynr_app:doc_instituciones_crud_eliminar'
                 }   
# --------------------------------------------------------------------------------------------------

# PÁGINA INFRAESTRUCTURA -----------------------------------------------------------------------------
# Datos para la Tabla
#querysetInfraestructura= Infraestructura.objects.all().order_by('nombre').values('autor_id__username','id','categoria','nombre','descripcion','id_inst__nombre')
contextoInfraestructura ={
                    'titulo': 'Infraestructura',
                    'encabezados':['autor_id','Categoría','Nombre','Descripción','Institución'],
                    'url_crear':'cynr_app:infraestructura_crud_crear',
                    'url_ver':'cynr_app:infraestructura_crud_ver',
                    'url_editar':'cynr_app:infraestructura_crud_editar',
                    'url_eliminar':'cynr_app:infraestructura_crud_eliminar'
                 }   
# --------------------------------------------------------------------------------------------------

# PÁGINA OBRAS DE TOMA -----------------------------------------------------------------------------
# Datos para la Tabla
#querysetObraToma= ObrasToma.objects.all().order_by('id_infra__nombre').values('autor_id__username','id','id_infra__nombre','estado')
contextoObraToma ={
                    'titulo': 'Obras de Toma',
                    'encabezados':['autor_id','Nombre','Estado'],
                    'url_crear':'cynr_app:obras_de_toma_crud_crear',
                    'url_editar':'cynr_app:obras_de_toma_crud_editar',
                    'url_eliminar':'cynr_app:obras_de_toma_crud_eliminar'
                 }   
# --------------------------------------------------------------------------------------------------

# PÁGINA OBRAS DE TOMA -----------------------------------------------------------------------------
# Datos para la Tabla
#querysetCyNR= CyNR.objects.all().order_by('id_infra__nombre').values('autor_id__username','id','id_infra__nombre','referencia','valor','unid_meteo_est')
contextoCyNR ={
                    'titulo': 'Cotas y Niveles de Referencia',
                    'encabezados':['autor_id','Infraestructura','referencia','valor','Id Estación'],
                    'url_crear':'cynr_app:cynr_crud_crear',
                    'url_editar':'cynr_app:cynr_crud_editar',
                    'url_eliminar':'cynr_app:cynr_crud_eliminar'
                 }   
# --------------------------------------------------------------------------------------------------

# PÁGINA DOCUMENTOS -----------------------------------------------------------------------------
# Datos para la Tabla
#querysetDoc= Documentos.objects.all().order_by('fecha_hora').values('autor_id__username','id','fecha_hora','categoria','titulo','descripcion')
contextoDoc ={
                    'titulo': 'Documentos',
                    'encabezados':['autor_id','Fecha','Categoria','Titulo','Descripción'],
                    'url_crear':'cynr_app:documentos_crud_crear',
                    'url_editar':'cynr_app:documentos_crud_editar',
                    'url_eliminar':'cynr_app:documentos_crud_eliminar',
                    'url_cont':'cynr_app:cont_documento_crud'
                 }   
# --------------------------------------------------------------------------------------------------

# PÁGINA GEOMANIO -----------------------------------------------------------------------------
contextoGeomanio ={
                    'titulo': 'Geomanio.io',
                  }

# PÁGINA NOTICIAS -----------------------------------------------------------------------------
# Datos para la Tabla
#querysetNot= Noticias.objects.all().order_by('fecha_hora').values('autor_id__username','id','fecha_hora','id_infra__nombre','encabezado')
contextoNot ={
                    'titulo': 'Noticia',
                    'encabezados':['autor_id','Fecha','Infraestructura','Encabezado'],
                    'url_crear':'cynr_app:noticias_crud_crear',
                    'url_editar':'cynr_app:noticias_crud_editar',
                    'url_eliminar':'cynr_app:noticias_crud_eliminar'
                 }   
# -------------------------------------------------------------------------------------------------