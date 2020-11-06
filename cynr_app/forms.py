from django.contrib.gis import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.postgres.forms import SimpleArrayField
from .models import *

#-----------------------------------------------------------------------------
# REGISTRARSE.
#-----------------------------------------------------------------------------
class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Usuario',max_length=30, required=True,
    help_text='Requerido. 30 characters o menos. Letras, digitos y @/./+/-/_ solamente.',
    widget=forms.TextInput(attrs={'class':"form-control",'placeholder': 'Usuario',
                                   'type':"text"}))
    first_name = forms.CharField(label='Nombre',max_length=30, required=False, help_text='Opcional.',
    widget=forms.TextInput(attrs={'class':"form-control",'placeholder': 'Nombres',
                                   'type':"text"}))
    last_name = forms.CharField(label='Apellido',max_length=30, required=False, help_text='Opcional.',
    widget=forms.TextInput(attrs={'class':"form-control",'placeholder': 'Apellido',
                                   'type':"text"}))
    email = forms.EmailField(label='Correo Electrónico',max_length=254, help_text='Requerido. Informar una casilla de correo válida.',
    widget=forms.TextInput(attrs={'class':"form-control",'placeholder': 'casilla@dominio',
                                   'type':"email"}))
    password1 = forms.CharField(label='Contraseña',max_length=30, required=False,
    help_text='Requerido.',
    widget=forms.TextInput(attrs={'class':"form-control",'placeholder': 'Contraseña',
                                   'type':"password"}))
    password2 = forms.CharField(label='Confirmación de Contraseña',max_length=30, required=False,
    help_text='Requerido.',
    widget=forms.TextInput(attrs={'class':"form-control",'placeholder': 'Contraseña',
                                   'type':"password"}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

#-----------------------------------------------------------------------------
# CREAR INSTITUCION.
#-----------------------------------------------------------------------------
class FormInstitucion(forms.ModelForm):
    def __init__(self, *args, **kwargs):
     # CHOICE INSTITUCIONES -----------------------------------------------------------------------------
     inst_categorias = GruposCategorias.objects.get(grupo='Instituciones').idGruposCategorias.values_list('categoria')
     CHOICE_INSTITUCIONES = [] # diccionario del menu
     for choice in inst_categorias:
        CHOICE_INSTITUCIONES.append((choice[0],choice[0])) # (seleccion,valor) ponemos lo mismo
     super(FormInstitucion, self).__init__(*args, **kwargs)
     self.fields['categoria'] = forms.CharField(label='Categoria', required=False, help_text='Seleccione la categoria',
        widget=forms.Select(attrs={'class':"form-control",'placeholder': 'Categoria','rows':5},choices=CHOICE_INSTITUCIONES))
        
    class Meta:
        model = Instituciones
        fields=['razon_social','categoria','presentacion','pag_web','logo','direccion','tel','jurisdiccion']

#-----------------------------------------------------------------------------
# CREAR DOCUMENTO SOBRE INSTITUCION.
#-----------------------------------------------------------------------------
class CrearDocInstitucion(forms.ModelForm):
    def __init__(self, *args, **kwargs):
     # CHOICE INSTITUCIONES -----------------------------------------------------------------------------
     list_query_inst = Instituciones.objects.all().order_by('razon_social').values_list('id','razon_social')
     CHOICE_INSTITUCIONES =[]
     for choice in list_query_inst:
        CHOICE_INSTITUCIONES.append((choice[0],choice[1])) # (seleccion,valor) ponemos lo mismo
     super(CrearDocInstitucion, self).__init__(*args, **kwargs)
     #self.fields['id_inst'] = forms.MultipleChoiceField(label='Institución', required=False, help_text='Seleccione la Institución',
     #   widget=forms.SelectMultiple(attrs={'class':"form-control",'placeholder': 'Institución','rows':5},choices=CHOICE_INSTITUCIONES))
     self.fields['id_inst'] = forms.ModelMultipleChoiceField(queryset=Instituciones.objects.all())
    class Meta:
        model = DocInstituciones
        fields=['id_inst','doc','conclusion']
