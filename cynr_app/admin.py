#from django.contrib import admin
from django.contrib.gis import admin
from .models import *

# Register your models here.
admin.site.register(GruposCategorias)
admin.site.register(Categorias)
admin.site.register(Instituciones)
admin.site.register(DocInstitucionales)
admin.site.register(Contactos)
admin.site.register(Infraestructura)
admin.site.register(CyNR)
admin.site.register(ObrasToma)
admin.site.register(Documentos)
admin.site.register(Archivos)
admin.site.register(Noticias)

#@admin.register(Categorias)
#class CategoriasAdmin(admin.ModelAdmin):
    #list_display = ('autor','id_grupo','categoria')
#    list_select_related = ('id_grupo')

#@admin.register(Categorias)
#class CategoriasAdmin(admin.ModelAdmin):
#    def formfield_for_foreignkey(self, db_field, request, **kwargs):
#        if db_field.name == "autor":

#       if db_field.name == "id_grupo":
#            kwargs["queryset"] = GruposCategorias.objects.values_list('grupo')
#            return super().formfield_for_foreignkey(db_field, request, **kwargs)



