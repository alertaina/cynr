from django.urls import path
from django.urls import reverse , reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.gis import forms as gisforms
from . import views
from . import menu
from .models import *
from . import forms
from . import contenidos
app_name = 'cynr_app'

urlpatterns = [
    # Inicio
    #path('index', views.Index.as_view(), name='index'),
    path('index', views.BasePaginas.as_view(template_name="cynr_app/index.html"), name='index'),
    path('', views.BasePaginas.as_view(template_name="cynr_app/index.html")),

    # Registro de Usuarios
    path('signup/', views.SignUp.as_view(), name='signup'),

    # CRUD INSTITUCIONES
    path('instituciones_crud/',ListView.as_view(
        #model = Instituciones,
        queryset = contenidos.querysetPagInst,
        paginate_by = 4,
        extra_context={'menu_navegacion':menu.MENU_NAVEGACION,
                        'contenido': contenidos.contextoPagInst,
                        'total_registros': contenidos.querysetPagInst.count(),
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
        template_name = 'cynr_app/modalFormItem.html',
                                ) , 
        name='instituciones_crud_crear'
        ),
    # EDITAR INSTITUCION
        path('instituciones_crud_editar/<int:pk>', UpdateView.as_view(
        model = Instituciones,
        context_object_name = 'obj',
        success_url = reverse_lazy('cynr_app:instituciones_crud'),
        form_class = forms.FormInstitucion,
        template_name = 'cynr_app/modalFormItem.html',
                                ) , 
        name='instituciones_crud_editar'
        ),
    # CRUD DOC INSTITUCIONES
    path('doc_instituciones_crud/',ListView.as_view(
        queryset = contenidos.querysetPagDocInst,
        paginate_by = 4,
        extra_context={'menu_navegacion':menu.MENU_NAVEGACION,
                        'contenido': contenidos.contextoDocPagInst,
                        'total_registros': contenidos.querysetPagDocInst.count(),
                      },
        template_name = 'cynr_app/base_paginas_crud.html',
                                ) , 
        name='doc_instituciones_crud'
        ),
    # CREAR DOC INSTITUCION
        path('doc_instituciones_crud_crear',views.BaseCreateView.as_view(
        success_url = reverse_lazy('cynr_app:doc_instituciones_crud'),
        extra_context={'contenido': contenidos.contextoDocPagInst,
                       'total_registros': contenidos.querysetInfraestructura.count(),
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
        queryset = contenidos.querysetInfraestructura,
        paginate_by = 4,
        extra_context={'menu_navegacion':menu.MENU_NAVEGACION,
                        'contenido': contenidos.contextoInfraestructura,
                        'total_registros': contenidos.querysetInfraestructura.count(),
                        'geoformmedia':gisforms.OSMWidget().media.render(),
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
    path('obra_de_toma_crud/',ListView.as_view(
        queryset = contenidos.querysetObraToma,
        paginate_by = 4,
        extra_context={'menu_navegacion':menu.MENU_NAVEGACION,
                        'contenido': contenidos.contextoObraToma,
                        'total_registros': contenidos.querysetObraToma.count(),
                        'geoformmedia':gisforms.OSMWidget().media.render(),
                      },
        template_name = 'cynr_app/base_paginas_crud.html',
                                ) , 
        name='obra_de_toma_crud'
        ),    
    # CREAR OBRA DE TOMA
        path('obra_de_toma_crud_crear',views.BaseObraTomaCreateView.as_view(
        success_url = reverse_lazy('cynr_app:obra_de_toma_crud'),
        extra_context={'contenido': contenidos.contextoObraToma,
                      },
        form_class = forms.FormInfraestructura,
        template_name = 'cynr_app/modalFormItemPadreHijo.html',
                                ) , 
        name='obra_de_toma_crud_crear'
        ),
    # EDITAR OBRA DE TOMA
        path('obra_de_toma_crud_editar/<int:pk>', UpdateView.as_view(
        model = Instituciones,
        context_object_name = 'obj',
        success_url = reverse_lazy('cynr_app:obra_de_toma_crud'),
        extra_context={'contenido': contenidos.contextoObraToma,
                      },
        form_class = forms.FormObraToma,
        template_name = 'cynr_app/modalFormItemPadreHijo.html',
                                ) , 
        name='obra_de_toma_crud_editar'
        ),
   #----------------------------------------------------------------------------
   # CRUD CYNR
    path('cynr_crud/',ListView.as_view(
        #model = Instituciones,
        queryset = contenidos.querysetCyNR,
        paginate_by = 4,
        extra_context={'menu_navegacion':menu.MENU_NAVEGACION,
                        'contenido': contenidos.contextoCyNR,
                        'total_registros': contenidos.querysetCyNR.count(),
                      },
        template_name = 'cynr_app/base_paginas_crud.html',
                                ) , 
        name='cynr_crud'
        ),
    # CREAR CYNR
        path('cynr_crud_crear',views.BaseCreateView.as_view(
        success_url = reverse_lazy('cynr_app:cynr_crud'),
        extra_context={'contenido': contenidos.contextoCyNR,
                      },
        form_class = forms.FormCyNR,
        template_name = 'cynr_app/modalFormItem.html',
                                ) , 
        name='cynr_crud_crear'
        ),
    # EDITAR CYNR
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
        #model = Instituciones,
        queryset = contenidos.querysetDoc,
        paginate_by = 4,
        extra_context={'menu_navegacion':menu.MENU_NAVEGACION,
                        'contenido': contenidos.contextoDoc,
                        'total_registros': contenidos.querysetDoc.count(),
                      },
        template_name = 'cynr_app/base_paginas_crud.html',
                                ) , 
        name='documentos_crud'
        ),
    # CREAR DOCUMENTOS
    #    path('documentos_crud_crear',views.BaseCreateView.as_view(
    #    success_url = reverse_lazy('cynr_app:documentos_crud'),
    #    extra_context={'contenido': contenidos.contextoDoc,
    #                  },
    #    form_class = forms.FormDoc,
    #    template_name = 'cynr_app/modalFormItem.html',
    #                            ) , 
    #    name='documentos_crud_crear'
    #    ),
    # CREAR DOCUMENTOS
        path('documentos_crud_crear',views.BaseCreateDoc.as_view(
        success_url = reverse_lazy('cynr_app:documentos_crud'),
        extra_context={'contenido': contenidos.contextoDoc,
                      },
        form_class = forms.FormDoc,
        template_name = 'cynr_app/modalFormItemPadreHijo.html',
                                ) , 
        name='documentos_crud_crear'
        ),
    # EDITAR DOCUMENTOS
        path('documentos_crud_editar/<int:pk>', UpdateView.as_view(
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
    # PAGINA GEOMANIO
    path('geomanio', views.BasePaginas.as_view(
        template_name="cynr_app/base_pagina_geomanio.html",
        extra_context={'contenido': contenidos.contextoGeomanio,}
        ), name='geomanio'),
   #----------------------------------------------------------------------------
   # CRUD NOTICIAS
    path('noticias_crud/',ListView.as_view(
        queryset = contenidos.querysetNot,
        paginate_by = 4,
        extra_context={'menu_navegacion':menu.MENU_NAVEGACION,
                        'contenido': contenidos.contextoNot,
                        'total_registros': contenidos.querysetNot.count(),
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

