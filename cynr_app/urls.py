from django.urls import path
from django.urls import reverse , reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
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
        extra_context={'contenido': contenidos.contextoPagInst,
                      },
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
                      },
        template_name = 'cynr_app/base_paginas_crud.html',
                                ) , 
        name='doc_instituciones_crud'
        ),
    # CREAR DOC INSTITUCION
        path('doc_instituciones_crud_crear',views.BaseCreateView.as_view(
        success_url = reverse_lazy('cynr_app:doc_instituciones_crud'),
        extra_context={'contenido': contenidos.contextoDocPagInst,
                      },
        form_class = forms.CrearDocInstitucion,
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
        form_class = forms.CrearDocInstitucion,
        template_name = 'cynr_app/modalFormItem.html',
                                ) , 
        name='doc_instituciones_crud_editar'
        ),

]
