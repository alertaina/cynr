from .models import *
##########################################################################
# CONTENIDO PARA LAS PÁGINAS
#-------------------------------------------------------------------------


# PÁGINA INSTITUCIONES -----------------------------------------------------------------------------
# Datos para la Tabla
querysetPagInst= Instituciones.objects.all().order_by('razon_social').values('autor__username','id','razon_social','categoria','jurisdiccion')
contextoPagInst ={
                    'titulo': 'Instituciones',
                    'encabezados':['Autor','Razón Social','Categoria','Jurisdicción'],
                    'url_crear':'cynr_app:instituciones_crud_crear',
                    'url_editar':'cynr_app:instituciones_crud_editar',
                    'url_eliminar':'cynr_app:instituciones_crud_eliminar'
                 }   
# --------------------------------------------------------------------------------------------------

# PÁGINA DOC INSTITUCIONES -----------------------------------------------------------------------------
# Datos para la Tabla
querysetPagDocInst= DocInstituciones.objects.all().order_by('id_inst__razon_social').values('autor__username','id','id_inst__razon_social','doc','conclusion')
contextoDocPagInst ={
                    'titulo': 'Documentos Sobre Instituciones',
                    'encabezados':['Autor','Razón Social','Documento','Conclusión'],
                    'url_crear':'cynr_app:doc_instituciones_crud_crear',
                    'url_editar':'cynr_app:doc_instituciones_crud_editar',
                    'url_eliminar':'cynr_app:doc_instituciones_crud_eliminar'
                 }   
# --------------------------------------------------------------------------------------------------