from django.shortcuts import render, redirect
from django.views import generic
#from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from django.views.generic import CreateView
from django.views.generic.edit import CreateView

from django.urls import reverse_lazy

from .models import *

from . import menu

class Index(generic.TemplateView):
    template_name = 'cynr_app/index.html'

# CLASE BASE PARA TODAS LAS PAGINAS (COHERENTE CON EL TEMPLATE BASE)
class BasePaginas(generic.TemplateView):
    #template_name = "book.html"
    def get_context_data(self, **kwargs):
        """ get_context_data let you fill the template context """
        context = super(BasePaginas, self).get_context_data(**kwargs)
        # Get Related publishers
        context['menu_navegacion'] = menu.MENU_NAVEGACION
        return context

# Create your views here.
