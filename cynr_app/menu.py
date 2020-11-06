from .models import *
##########################################################################
# MENU DE NAVEGACION
#-------------------------------------------------------------------------


# MENU INFRAESTRUCTURA -----------------------------------------------------------------------------
infra_categorias = GruposCategorias.objects.get(grupo='Infraestructura').idGruposCategorias.values()
dict_infra = {} # diccionario del menu
for item in infra_categorias:
 dict_infra[item['categoria']] = '/cynr_app/{}_crud'.format(item['categoria'].lower().replace(" ", "_")) # cargamos el url de navegacion   
# --------------------------------------------------------------------------------------------------

# MENU INSTITUCIONES -------------------------------------------------------------------------------
dict_inst = {'Instituciones':'/cynr_app/instituciones_crud','Documentos':'/cynr_app/doc_instituciones_crud'}

# MENU DOCUEMNTOS -----------------------------------------------------------------------------
doc_categorias = GruposCategorias.objects.get(grupo='Documentos').idGruposCategorias.values()
dict_docs = {} # diccionario del menu
for item in doc_categorias:
 dict_docs[item['categoria']] = '/cynr_app/{}_crud'.format(item['categoria'].lower().replace(" ", "_")) # cargamos el url de navegacion   
# --------------------------------------------------------------------------------------------------

MENU_NAVEGACION = {
                   'Infraestructura': {'menu': dict_infra},
                   'Instituciones': {'menu': dict_inst},
                   'Documentos':{'menu': dict_docs},
                   'Noticias': 'noticias'
                  }
