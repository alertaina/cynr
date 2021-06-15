from django.shortcuts import render, redirect
from django.views import generic
from django.forms.models import inlineformset_factory
#from django.forms import formset_factory
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
#from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from django.views.generic import CreateView
from django.views.generic.edit import CreateView, UpdateView
from django.db import transaction
from django.urls import reverse_lazy

import json
from django.core.serializers.json import DjangoJSONEncoder

from .models import *
from .forms import *
from . import menu


#class Index(generic.TemplateView):
#    template_name = 'cynr_app/index.html'
#########################################################################
# CLASE BASE PARA TODAS LAS PAGINAS (COHERENTE CON EL TEMPLATE BASE)
#########################################################################
class BasePaginas(generic.TemplateView):

    def get_context_data(self, **kwargs):
        """ get_context_data let you fill the template context """
        context = super(BasePaginas, self).get_context_data(**kwargs)
        # Menu Principal
        context['menu_navegacion'] = menu.MENU_NAVEGACION
        return context
#########################################################################
# CLASE PARA LA PAGINA INICIO (COHERENTE CON EL TEMPLATE BASE)
#########################################################################
class PaginasInicioTemplateView(generic.TemplateView):

    def get_context_data(self, **kwargs):
        """ get_context_data let you fill the template context """
        context = super(PaginasInicioTemplateView, self).get_context_data(**kwargs)
        # Menu Principal
        context['menu_navegacion'] = menu.MENU_NAVEGACION
        context['carrusel'] = Carrusel.objects.all()
        return context
#########################################################################
# CLASE BASE PARA TODAS LOS FURMULARIOS DE CREACIÓN DE ITEMS
#########################################################################
class BaseCreateView(CreateView):

    def form_valid(self, form):
        f = form.save(commit=False)
        f.autor_id = self.request.user
        f.save()
        return super().form_valid(form)

#########################################################################
# CLASE BASE PARA TODOS LOS FURMULARIOS DE EDICION DE ITEMS
#########################################################################
class BaseUpdateView(LoginRequiredMixin, UpdateView):

    def form_valid(self, form):
        f = form.save(commit=False)
        f.autor_id = self.request.user
        f.save()
        return super().form_valid(form)
##########################################################################
# Clase para registrar usuario usando la aplicacion auth
##########################################################################
class SignUp(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


#########################################################################
# CLASE PARA LA CREACION DE OBRAS DE TOMA QUE CARGAN A LA VEZ
# OBJETOS INFRAESTRUCTURA Y OBRAS DE TOMA EMPARENTADOS POR UN FOREING KEY
#########################################################################
class BaseObraTomaCreateView(LoginRequiredMixin, CreateView):
    #model = Infraestructura
    template_name = 'cynr_app/modalFormItemObraToma.html'
    form_class = FormInfraestructura

    def get_context_data(self, **kwargs):
        data = super(BaseObraTomaCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['hijos'] = ObraTomaFormset(self.request.POST)       
        else:
            data['hijos'] = ObraTomaFormset()
        return data    

    def form_valid(self, form):
        context = self.get_context_data()
        hijos = context['hijos']
        form.instance.autor_id = self.request.user
        form.instance.ficha_tec = self.request.FILES["ficha_tec"]
        form.instance.geom = self.request.POST["geom"]
        self.object = form.save()
        if hijos.is_valid():           
            hijos.instance = self.object
            hijos.instance.autor_id = self.request.user
            hijos.save()
        return super(BaseObraTomaCreateView, self).form_valid(form) 

#########################################################################
# CLASE PARA LA CREACIÓN DE INSTITUCIONES
#########################################################################
#class InstitucionesCreateView(LoginRequiredMixin, CreateView):
#    def form_valid(self, form):
#        f = form.save(commit=False)
#        f.autor_id = self.request.user
#        #f.logo = self.request.FILES["logo"]
#        f.save()
#        return super().form_valid(form)
#########################################################################
# CLASE PARA LA CREACIÓN DE INFRAESTRUCTURA
#########################################################################
class BaseInfraestructuraCreateView(CreateView):

    def form_valid(self, form):
        f = form.save(commit=False)
        f.autor_id = self.request.user
        f.geom = self.request.POST["geom"]
        f.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['atributos_base']= AtributosPorDefectoInfra.objects.all()
        return context

#########################################################################
# CLASE PARA LA ACTUALIZACIÓN DE INFRAESTRUCTURA
#########################################################################
class BaseInfraestructuraUpdateView(LoginRequiredMixin, UpdateView):

    def form_valid(self, form):
        f = form.save(commit=False)
        f.autor_id = self.request.user
        f.geom = self.request.POST["geom"]
        f.save()
        return super().form_valid(form)
 



#########################################################################
# CLASE PARA LA ACTUALIZACIÓN DE DOCUMENTOS
#########################################################################
class BaseDocUpdateView(LoginRequiredMixin, UpdateView):
    
    def get_context_data(self, **kwargs):
        # we need to overwrite get_context_data
        # to make sure that our formset is rendered.
        # the difference with CreateView is that
        # on this view we pass instance argument
        # to the formset because we already have
        # the instance created
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["hijos"] = BaseContDocFormset(self.request.POST,self.request.FILES, instance=self.object)
        else:
            data["hijos"] = BaseContDocFormset(instance=self.object)
        return data
    def form_valid(self, form):
        context = self.get_context_data()
        children = context["hijos"]
        self.object = form.save()
        if children.is_valid():
            children.instance = self.object
            children.save()
        return super().form_valid(form)

##########################################################################
# VISTA QUE LISTA LOS CONTENIDOS DE UN DOCUMENTOS
##########################################################################
class ContDocView(LoginRequiredMixin,TemplateView):
    template_name = 'cynr_app/cont_doc_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contenido'] = Documentos.objects.get(pk=kwargs["pk_doc"]).idContDoc.values('titulo')
        return context
    #def get(self, request, *args, **kwargs):
     #either
    #    self.object_list = Documentos.objects.get(pk=kwargs["pk_doc"]).idContDoc.values_list('titulo')
    #    self.queryset = Documentos.objects.get(pk=kwargs["pk_doc"]).idContDoc.values_list('titulo')
     #   context = self.get_context_data()
     #   return self.render_to_response(context)
        #self.object_list = self.object_list.filter(lab__acronym=kwargs['lab'])
    #def get_queryset (self, **kwargs):
    #    return Documentos.objects.get(pk=kwargs["pk_doc"]).idContDoc.values_list('titulo') 

##########################################################################
# VISTA INSTITUCIONES
##########################################################################
#class InstitucionesListView(ListView):

    # model = Instituciones
    #template_name = 'cynr_app/base_paginas_crud.html'
    #paginate_by = 20  # if pagination is desired

