#from .models import *
##########################################################################
# MENU DE NAVEGACION
#-------------------------------------------------------------------------


# MENU INFRAESTRUCTURA -----------------------------------------------------------------------------
#infra_categorias = GruposCategorias.objects.get(grupo='Infraestructura').idGruposCategorias.values()
#infra_categorias = []
#dict_infra = {'Infraestructura':'/cynr_app/infraestructura_crud'} # diccionario del menu
#for item in infra_categorias:
# dict_infra[item['categoria']] = '/cynr_app/{}_crud'.format(item['categoria'].lower().replace(" ", "_")) # cargamos el url de navegacion   
# --------------------------------------------------------------------------------------------------

# MENU INSTITUCIONES -------------------------------------------------------------------------------
#dict_inst = {'Instituciones':'/cynr_app/instituciones_crud','Documentos':'/cynr_app/doc_instituciones_crud'}

# MENU DOCUEMNTOS -----------------------------------------------------------------------------
#doc_categorias = GruposCategorias.objects.get(grupo='Documentos').idGruposCategorias.values()
#doc_categorias =[]
#dict_docs = {} # diccionario del menu
#for item in doc_categorias:
# dict_docs[item['categoria']] = '/cynr_app/{}_crud'.format(item['categoria'].lower().replace(" ", "_")) # cargamos el url de navegacion   
# --------------------------------------------------------------------------------------------------
# El LINK AL EDITOR VECTORIAL GEOMAN PARA OBTENER EL GEOJSO DE LA GEOMETRIA DE LA 
# INFRAESTRUCTURA SE CARGA APARTE
#MENU_NAVEGACION = {
#                   'Infraestructura': {'menu': dict_infra},
#                   'Instituciones': {'menu': dict_inst},
#                   'Documentos':'/cynr_app/documentos_crud',
#                   'Noticias': '/cynr_app/noticias_crud',
#                   'CyNR':'/cynr_app/cynr_crud',
#                  }
MENU_NAVEGACION = {
                   'Infraestructura': {'menu': {'Obras de Toma':'/cynr_app/obras_de_toma_crud'}},
                   'Instituciones': {'menu': {'Instituciones':'/cynr_app/instituciones_crud',
                                             'Documentos':'/cynr_app/instituciones_crud'}},
                   'Capas GeoJson': {'menu': {'Capas':'/cynr_app/capas_geojson_crud',
                                              'Geoman.io':'/cynr_app/geomanio'}},
                   'Documentos':'/cynr_app/documentos_crud',
                   'Noticias': '/cynr_app/noticias_crud',
                   'CyNR':'/cynr_app/cynr_crud',
                  }