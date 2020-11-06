from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.list import ListView
#from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from django.views.generic import CreateView
from django.views.generic.edit import CreateView, UpdateView

from django.urls import reverse_lazy

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
# CLASE BASE PARA TODAS LOS FURMULARIOS DE CREACIÓN DE ITEMS
#########################################################################
class BaseCreateView(LoginRequiredMixin, CreateView):

    def form_valid(self, form):
        f = form.save(commit=False)
        f.autor = self.request.user
        f.save()
        return super().form_valid(form)

#########################################################################
# CLASE BASE PARA TODOS LOS FURMULARIOS DE EDICION DE ITEMS
#########################################################################
class BaseUpdateView(LoginRequiredMixin, UpdateView):

    def form_valid(self, form):
        f = form.save(commit=False)
        f.autor = self.request.user
        f.save()
        return super().form_valid(form)
##########################################################################
# Clase para registrar usuario usando la aplicacion auth
##########################################################################
class SignUp(BaseCreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'




##########################################################################
# VISTA INSTITUCIONES
##########################################################################
#class InstitucionesListView(ListView):

    # model = Instituciones
    #template_name = 'cynr_app/base_paginas_crud.html'
    #paginate_by = 20  # if pagination is desired
