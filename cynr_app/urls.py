from django.urls import path
from django.urls import reverse , reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from . import views
from . import menu
from .models import *
from . import forms
from . import contenidos
app_name = 'cynr_app'
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Inicio
    path('index', views.PaginasInicioTemplateView.as_view(template_name="cynr_app/index.html"), name='index'),
    path('', views.PaginasInicioTemplateView.as_view(template_name="cynr_app/index.html")),

    # Registro de Usuarios
    path('signup', views.SignUp.as_view(), name='signup'),

    ####################################################################
    #- INSTITUCIONES
    ####################################################################
    # CRUD INSTITUCIONES
    path('instituciones_crud/',ListView.as_view(
        queryset = Instituciones.objects.all().order_by('nombre').values('autor_id__username','id','nombre','categoria','alc_geografico'),
        paginate_by = 4,
        extra_context={'menu_navegacion':menu.MENU_NAVEGACION,
                        'contenido': contenidos.contextoPagInst,
                      },
        template_name = 'cynr_app/base_paginas_crud.html',
                                ) , 
        name='instituciones_crud'
        ),

    # CREAR INSTITUCION
        path('instituciones_crud_crear',views.BaseCreateView.as_view(
        success_url = reverse_lazy('cynr_app:instituciones_crud'),
        extra_context={'contenido': contenidos.contextoPagInst,
                      },
        form_class = forms.FormInstitucion,
        template_name = 'cynr_app/modalCreateItemWithFile.html',
                                ) , 
        name='instituciones_crud_crear'
        ),
    # VER INSTITUCION
        path('instituciones_crud_ver/<int:pk>',DetailView.as_view(
        model = Instituciones,
        context_object_name = 'obj',
        template_name = 'cynr_app/modalVerItemInstituciones.html',
                                ) , 
        name='instituciones_crud_ver'
        ),
    
    # EDITAR INSTITUCION
        path('instituciones_crud_editar/<int:pk>', UpdateView.as_view(
        model = Instituciones,
        context_object_name = 'obj',
        success_url = reverse_lazy('cynr_app:instituciones_crud'),
        extra_context={'contenido': contenidos.contextoPagInst,
                      },
        form_class = forms.FormInstitucion,
        template_name = 'cynr_app/modalUpdateItemWithFile.html',
                                ) , 
        name='instituciones_crud_editar'
        ),
    # ELIMINAR INSTITUCION
        path('instituciones_crud_eliminar/<int:pk>', DeleteView.as_view(
        model = Instituciones,
        context_object_name = 'obj',
        success_url = reverse_lazy('cynr_app:instituciones_crud'),
        extra_context={'contenido': contenidos.contextoPagInst,
                    },
        template_name = 'cynr_app/modalDeleteItem.html',
                            ) , 
        name='instituciones_crud_eliminar'
    ),
    ####################################################################
    #- DOCUMENTOS INSTITUCIONES
    ####################################################################
    # CRUD DOC INSTITUCIONES
    path('doc_instituciones_crud/',ListView.as_view(
        #queryset = contenidos.querysetPagDocInst,
        queryset = DocInstitucionales.objects.all().values('autor_id__username','id','nombre','presentacion','categoria','alc_geografico'),
        paginate_by = 4,
        extra_context={'menu_navegacion':menu.MENU_NAVEGACION,
                        'contenido': contenidos.contextoDocPagInst,
                        #'total_registros': contenidos.querysetPagDocInst.count(),
                      },
        template_name = 'cynr_app/base_paginas_crud.html',
                                ) , 
        name='doc_instituciones_crud'
        ),
    # CREAR DOC INSTITUCION
        path('doc_instituciones_crud_crear',views.BaseCreateView.as_view(
        success_url = reverse_lazy('cynr_app:doc_instituciones_crud'),
        extra_context={'contenido': contenidos.contextoDocPagInst,
                       #'total_registros': contenidos.querysetInfraestructura.count(),
                      },
        form_class = forms.FormDocInstitucionales,
        template_name = 'cynr_app/modalFormItem.html',
                                ) , 
        name='doc_instituciones_crud_crear'
        ),

    # EDITAR DOC INSTITUCION
        path('doc_instituciones_crud_editar/<int:pk>', UpdateView.as_view(
        model = Instituciones,
        context_object_name = 'obj',
        success_url = reverse_lazy('cynr_app:doc_instituciones_crud'),
        extra_context={'contenido': contenidos.contextoDocPagInst,
                      },
        form_class = forms.FormDocInstitucionales,
        template_name = 'cynr_app/modalFormItem.html',
                                ) , 
        name='doc_instituciones_crud_editar'
        ),
    #----------------------------------------------------------------------
    # CRUD INFRAESTRUCTURA
    path('infraestructura_crud/',ListView.as_view(
        #queryset = contenidos.querysetInfraestructura,
        queryset =  Infraestructura.objects.all().order_by('nombre').values('autor_id__username','id','categoria','nombre','descripcion','id_inst__nombre'),
        paginate_by = 4,
        extra_context={'menu_navegacion':menu.MENU_NAVEGACION,
                        'contenido': contenidos.contextoInfraestructura,
                        #'total_registros': contenidos.querysetInfraestructura.count(),
                      },
        template_name = 'cynr_app/base_paginas_crud.html',
                                ) , 
        name='infraestructura_crud'
        ),    
    # CREAR INFRAESTRUCTURA
        path('infraestructura_crud_crear',views.BaseInfraestructuraCreateView.as_view(
        success_url = reverse_lazy('cynr_app:infraestructura_crud'),
        extra_context={'contenido': contenidos.contextoInfraestructura,
                      },
        form_class = forms.FormInfraestructura,
        template_name = 'cynr_app/modalFormItemGeo.html',
                                ) , 
        name='infraestructura_crud_crear'
        ),
    # EDITAR INFRAESTRUCTURA
        path('infraestructura_crud_editar/<int:pk>', views.BaseInfraestructuraUpdateView.as_view(
        model = Infraestructura,
        context_object_name = 'obj',
        success_url = reverse_lazy('cynr_app:infraestructura_crud'),
        extra_context={'contenido': contenidos.contextoInfraestructura,
                      },
        form_class = forms.FormInfraestructura,
        template_name = 'cynr_app/modalFormItemGeo.html',
                                ) , 
        name='infraestructura_crud_editar'
        ),
    #----------------------------------------------------------------------
    # CRUD OBRA DE TOMA
    path('obras_de_toma_crud/',ListView.as_view(
        #queryset = contenidos.querysetObraToma,
        queryset = ObrasToma.objects.all().order_by('id_infra__nombre').values('autor_id__username','id','id_infra__nombre','estado'),
        paginate_by = 4,
        extra_context={'menu_navegacion':menu.MENU_NAVEGACION,
                        'contenido': contenidos.contextoObraToma,
                        #'total_registros': contenidos.querysetObraToma.count(),
                      },
        template_name = 'cynr_app/base_paginas_crud.html',
                                ) , 
        name='obras_de_toma_crud'
        ),    
    # CREAR OBRA DE TOMA
        path('obras_de_toma_crud_crear',views.BaseObraTomaCreateView.as_view(
        success_url = reverse_lazy('cynr_app:obras_de_toma_crud'),
        extra_context={'contenido': contenidos.contextoObraToma,
                      },
        #form_class = forms.FormInfraestructura,
        #template_name = 'cynr_app/modalFormItemObraToma.html',
                                ) , 
        name='obras_de_toma_crud_crear'
        ),
    # EDITAR OBRA DE TOMA
        path('obras_de_toma_crud_editar/<int:pk>', UpdateView.as_view(
        model = Infraestructura,
        context_object_name = 'obj',
        success_url = reverse_lazy('cynr_app:obras_de_toma_crud'),
        extra_context={'contenido': contenidos.contextoObraToma,
                      },
        form_class = forms.FormObraToma,
        template_name = 'cynr_app/modalFormItemPadreHijo.html',
                                ) , 
        name='obras_de_toma_crud_editar'
        ),
   #----------------------------------------------------------------------------
   # CRUD CYNR
    path('cynr_crud/',ListView.as_view(
        #model = Instituciones,
        #queryset = contenidos.queryset1,
        queryset = CyNR.objects.all().order_by('id_infra__nombre').values('autor_id__username','id','id_infra__nombre','referencia','valor','unid_meteo_est'),
        paginate_by = 4,
        extra_context={'menu_navegacion':menu.MENU_NAVEGACION,
                        'contenido': contenidos.contextoCyNR,
                       # 'total_registros': contenidos.queryset1.count(),
                      },
        template_name = 'cynr_app/base_paginas_crud.html',
                                ) , 
        name='cynr_crud'
        ),
    # CREAR 1
        path('cynr_crud_crear',views.BaseCreateView.as_view(
        success_url = reverse_lazy('cynr_app:cynr_crud'),
        extra_context={'contenido': contenidos.contextoCyNR,
                      },
        form_class = forms.FormCyNR,
        template_name = 'cynr_app/modalFormItem.html',
                                ) , 
        name='cynr_crud_crear'
        ),
    # EDITAR 1
        path('cynr_crud_editar/<int:pk>', UpdateView.as_view(
        model = CyNR,
        context_object_name = 'obj',
        success_url = reverse_lazy('cynr_app:cynr_crud'),
        extra_context={'contenido': contenidos.contextoCyNR,
                      },
        form_class = forms.FormCyNR,
        template_name = 'cynr_app/modalFormItem.html',
                                ) , 
        name='cynr_crud_editar'
        ),
   #----------------------------------------------------------------------------
   # CRUD DOCUMENTOS
    path('documentos_crud/',ListView.as_view(
        #queryset = contenidos.querysetDoc,
        queryset = Documentos.objects.all().order_by('fecha_hora').values('autor_id__username','id','fecha_hora','categoria','titulo','descripcion'),
        paginate_by = 4,
        extra_context={'menu_navegacion':menu.MENU_NAVEGACION,
                        'contenido': contenidos.contextoDoc,
                        #'total_registros': contenidos.querysetDoc.count(),
                      },
        template_name = 'cynr_app/base_paginas_crud_doc.html',
                                ) , 
        name='documentos_crud'
        ),
     # CREAR DOCUMENTOS
        path('documentos_crud_crear',views.BaseCreateView.as_view(
        success_url = reverse_lazy('cynr_app:documentos_crud'),
        extra_context={'contenido': contenidos.contextoDoc,
                      },
        form_class = forms.FormDoc,
        template_name = 'cynr_app/modalFormItemPadreHijo.html',
                                ) , 
        name='documentos_crud_crear'
        ),
    # EDITAR DOCUMENTOS
        path('documentos_crud_editar/<int:pk>', views.BaseUpdateView.as_view(
        model = Documentos,
        context_object_name = 'obj',
        success_url = reverse_lazy('cynr_app:documentos_crud'),
        extra_context={'contenido': contenidos.contextoDoc,
                      },
        form_class = forms.FormDoc,
        template_name = 'cynr_app/modalFormItem.html',
                                ) , 
        name='documentos_crud_editar'
        ),
   #----------------------------------------------------------------------------
   # CRUD CONTENIDO DOCUMENTO
    path('cont_documento_crud/<int:pk_doc>',views.ContDocView.as_view(), 
        name='cont_documento_crud'
        ),
 
    # PAGINA GEOMANIO
    path('geomanio', views.BasePaginas.as_view(
        template_name='cynr_app/crud_geomanio.html',
        extra_context={'contenido': contenidos.contextoGeomanio,}
        ), name='geomanio'),
   #----------------------------------------------------------------------------
   # CRUD NOTICIAS
    path('noticias_crud/',ListView.as_view(
        #queryset = contenidos.querysetNot,
        queryset = Noticias.objects.all().order_by('fecha_hora').values('autor_id__username','id','fecha_hora','id_infra__nombre','encabezado'),
        paginate_by = 4,
        extra_context={'menu_navegacion':menu.MENU_NAVEGACION,
                        'contenido': contenidos.contextoNot,
                        #'total_registros': contenidos.querysetNot.count(),
                      },
        template_name = 'cynr_app/base_paginas_crud.html',
                                ) , 
        name='noticias_crud'
        ),
    # CREAR NOTICIAS
        path('noticias_crud_crear',views.BaseCreateView.as_view(
        success_url = reverse_lazy('cynr_app:noticias_crud'),
        extra_context={'contenido': contenidos.contextoNot,
                      },
        form_class = forms.FormNot,
        template_name = 'cynr_app/modalFormItem.html',
                                ) , 
        name='noticias_crud_crear'
        ),
    # EDITAR NOTICIAS
        path('noticias_crud_editar/<int:pk>', UpdateView.as_view(
        model = Noticias,
        context_object_name = 'obj',
        success_url = reverse_lazy('cynr_app:noticas_crud'),
        extra_context={'contenido': contenidos.contextoNot,
                      },
        form_class = forms.FormNot,
        template_name = 'cynr_app/modalFormItem.html',
                                ) , 
        name='noticias_crud_editar'
        ),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)