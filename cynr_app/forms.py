from django.contrib.gis import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.postgres.forms import SimpleArrayField
from .models import *
#from django.forms import MultiWidget, TextInput
#from django import forms as forms2
#import pickle
#import json
#class MultiWidgetBasic(forms2.widgets.MultiWidget):
#    def __init__(self, attrs=None):
#        widgets = [forms2.TextInput(),
#                   forms2.TextInput()]
#        super(MultiWidgetBasic, self).__init__(widgets, attrs)

#    def decompress(self, value):
#        if value:
#            return pickle.loads(value)
#        else:
#            return ['', '']

#class WidgetDoc(forms2.widgets.MultiWidget):
#    def __init__(self, attrs=None):
#        widgets = {'titulo':forms2.TextInput(attrs={'required': False,'class':"form-control",'name':"titulo"}),
#                   'contenido':forms2.TextInput(attrs={'required': False,'class':"form-control",'name':"contenido"})
#                  }
#        super(WidgetDoc, self).__init__(widgets, attrs)

#    def decompress(self, value):
#        if value:
#            return json.dumps(value) # trasnforma un diccionario python en json
#        else:
#            return ["", ""]

#class DocField(forms2.fields.MultiValueField):
#    widget = WidgetDoc

#    def __init__(self, *args, **kwargs):
#        list_fields = [forms2.fields.CharField(max_length=31),
#                       forms2.fields.CharField(max_length=31)]
#        super(DocField, self).__init__(list_fields, *args, **kwargs)
#
#    def compress(self, values):
        ## compress list to single object                                               
        ## eg. date() >> u'31/12/2012'                                                  
        #return json.dumps(values)


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
# CREAR y EDITAR INSTITUCION.
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
     self.fields['nombre'].widget.attrs.update({'class': 'form-control','type':"text"})
     self.fields['presentacion'].widget.attrs.update({'class': 'form-control','row':3})
     self.fields['pag_web'].widget.attrs.update({'class': 'form-control'})
     self.fields['logo'].widget.attrs.update({'class': 'form-control-file'})
     self.fields['direccion'].widget.attrs.update({'class': 'form-control','row':3})
     self.fields['tel'].widget.attrs.update({'class': 'form-control'})
     self.fields['jurisdiccion'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Instituciones
        fields=['nombre','categoria','presentacion','pag_web','logo','direccion','tel','jurisdiccion']
#-----------------------------------------------------------------------------
# CREAR Y EDITAR DOCUMENTO SOBRE INSTITUCION.
#-----------------------------------------------------------------------------
class FormDocInstitucionales(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        categorias = GruposCategorias.objects.get(grupo='Documentos Institucionales').idGruposCategorias.values_list('categoria')
        CHOICE_CATEGORIAS = [] # diccionario del menu
        for choice in categorias:
            CHOICE_CATEGORIAS.append((choice[0],choice[0]))
        super(FormDocInstitucionales, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        self.fields['id_inst'].widget.attrs.update({'class': 'form-control'})
        self.fields['presentacion'].widget.attrs.update({'class': 'form-control','row':3})
        self.fields['categoria']=forms.CharField(label='Categoria', required=False, help_text='Seleccione la categoria',
        widget=forms.Select(attrs={'class':"form-control",'placeholder': 'Categoria','rows':1},choices=CHOICE_CATEGORIAS))
        self.fields['link_doc'].widget.attrs.update({'class': 'form-control'})
        self.fields['arch_doc'].widget.attrs.update({'class': 'form-control-file'})
        self.fields['jurisdiccion'].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = DocInstitucionales
        fields=['nombre','id_inst','presentacion','categoria','link_doc','arch_doc','jurisdiccion']

#-----------------------------------------------------------------------------
#  INFRAESTRUCTURA.
#-----------------------------------------------------------------------------
class FormInfraestructura(forms.ModelForm):
    #arch_geometria = forms.FileField()
    geometria = forms.CharField()
    def __init__(self, *args, **kwargs):
        categorias = GruposCategorias.objects.get(grupo='Infraestructura').idGruposCategorias.values_list('categoria')
        CHOICE_CATEGORIAS = [] # diccionario del menu
        for choice in categorias:
            CHOICE_CATEGORIAS.append((choice[0],choice[0]))
        super(FormInfraestructura, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        self.fields['id_inst'].widget.attrs.update({'class': 'form-control'})
        self.fields['descripcion'].widget.attrs.update({'class': 'form-control','row':3})
        self.fields['categoria']=forms.CharField(label='Categoria', required=False, help_text='Seleccione la categoria',
        widget=forms.Select(attrs={'class':"form-control",'placeholder': 'Categoria','rows':1},choices=CHOICE_CATEGORIAS))
        #self.fields['geom']=forms.GeometryField(srid='4326',widget=forms.Textarea)
        #self.fields['geometria'].widget.attrs.update({'class': 'form-control-file'})
        
        #self.fields['geom'].widget.attrs.update({'template_name':'cynr_app/geomFormItem.html','class': 'form-control'})
        #self.fields['geom'].widget.attrs.update({'map_width': 800,
        #       'map_height': 400,
        #       'default_lat': -31.747790,
       #        'default_lon': -60.511456,
        #       'default_zoom': 6,
        #       'map_srid':4326})
        self.fields['ficha_tec'].widget.attrs.update({'class': 'form-control-file'})
        
    class Meta:
        model = Infraestructura
        fields=['nombre','id_inst','descripcion','categoria','ficha_tec']

#-----------------------------------------------------------------------------
#  OBRA DE TOMA.
#-----------------------------------------------------------------------------
class FormObraToma(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        tipo = GruposCategorias.objects.get(grupo='Tipo Obra de Toma').idGruposCategorias.values_list('categoria')
        CHOICE_TIPO = [] 
        for choice in tipo:
            CHOICE_TIPO.append((choice[0],choice[0]))
        funcionamiento = GruposCategorias.objects.get(grupo='Funcionamiento de Obra').idGruposCategorias.values_list('categoria')
        CHOICE_FUNCIONAMIENTO = [] 
        for choice in funcionamiento:
            CHOICE_FUNCIONAMIENTO.append((choice[0],choice[0]))
        uso = GruposCategorias.objects.get(grupo='Uso Obra de Toma').idGruposCategorias.values_list('categoria')
        CHOICE_USO = [] 
        for choice in uso:
            CHOICE_USO.append((choice[0],choice[0]))
        estado = GruposCategorias.objects.get(grupo='Estado de Obra').idGruposCategorias.values_list('categoria')
        CHOICE_ESTADO = [] 
        for choice in estado:
            CHOICE_ESTADO.append((choice[0],choice[0]))

        super(FormObraToma, self).__init__(*args, **kwargs)

        self.fields['tipo']=forms.CharField(label='Tipo', required=False, help_text='Seleccione el Tipo',
            widget=forms.Select(attrs={'class':"form-control",'placeholder': 'Tipo','rows':1},choices=CHOICE_TIPO))
        self.fields['funcionamiento']=forms.CharField(label='Funcionamiento', required=False, help_text='Seleccione el Funcionamiento',
            widget=forms.Select(attrs={'class':"form-control",'placeholder': 'Funcionamiento','rows':1},choices=CHOICE_FUNCIONAMIENTO))
        self.fields['uso']=forms.CharField(label='Uso', required=False, help_text='Seleccione el Uso',
            widget=forms.Select(attrs={'class':"form-control",'placeholder': 'Uso','rows':1},choices=CHOICE_USO))
        self.fields['estado']=forms.CharField(label='Estado', required=False, help_text='Seleccione el Estado',
            widget=forms.Select(attrs={'class':"form-control",'placeholder': 'Estado','rows':1},choices=CHOICE_ESTADO))
        self.fields['desc_estado'].widget.attrs.update({'class': 'form-control','row':3})

        class Meta:
            model = ObrasToma
            fields=['tipo','funcionamiento','uso','estado','desc_estado']

#-----------------------------------------------------------------------------
# CREAR Y EDITAR COTAS Y NIVELES DE REFERENCIA.
#-----------------------------------------------------------------------------
class FormCyNR(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormCyNR, self).__init__(*args, **kwargs)
        self.fields['unid_meteo_est'].widget.attrs.update({'class': 'form-control'})
        self.fields['referencia'].widget.attrs.update({'class': 'form-control'})
        self.fields['valor'].widget.attrs.update({'class': 'form-control'})
        self.fields['descripcion'].widget.attrs.update({'class': 'form-control'})
        self.fields['id_infra'].widget.attrs.update({'class': 'form-control'})
 
    class Meta:
        model = CyNR
        fields=['unid_meteo_est','referencia','valor','descripcion','id_infra']

#-----------------------------------------------------------------------------
#  DOCUMENTOS.
#-----------------------------------------------------------------------------
class FormDoc(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        categorias = GruposCategorias.objects.get(grupo='Documentos').idGruposCategorias.values_list('categoria')
        CHOICE_CATEGORIAS = [] # diccionario del menu
        for choice in categorias:
            CHOICE_CATEGORIAS.append((choice[0],choice[0]))
        super(FormDoc, self).__init__(*args, **kwargs)
        self.fields['id_infra'].widget.attrs.update({'class': 'form-control'})
        self.fields['id_cynr'].widget.attrs.update({'class': 'form-control'})
        self.fields['categoria']=forms.CharField(label='Categoria', required=False, help_text='Seleccione la categoria',
        widget=forms.Select(attrs={'class':"form-control",'placeholder': 'Categoria','rows':1},choices=CHOICE_CATEGORIAS))
        self.fields['titulo'].widget.attrs.update({'class': 'form-control','type':"text"})
        self.fields['descripcion'].widget.attrs.update({'class': 'form-control','row':3})
        #self.fields['documento'].widget.attrs.update({'class': 'form-control','row':3})
        #self.fields['documento']=DocField()
        #self.fields['documento']=forms2.CharField(max_length=32, widget =forms2.MultiWidget(widgets=[forms2.TextInput,forms2.TextInput]))
                
    class Meta:
        model = Documentos
        fields=['id_infra','id_cynr','categoria','titulo','descripcion','documento']