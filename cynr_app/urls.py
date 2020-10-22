from django.urls import path
from django.views.generic import TemplateView
from . import views
app_name = 'cynr_app'

urlpatterns = [
    # Inicio
    #path('index', views.Index.as_view(), name='index'),
    path('index', views.BasePaginas.as_view(template_name="cynr_app/index.html"), name='index'),
    path('', views.BasePaginas.as_view(template_name="cynr_app/index.html")),
]
