from django.contrib.gis import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.postgres.forms import SimpleArrayField
from .models import *

from django.forms.models import inlineformset_factory

from django.forms.models import BaseInlineFormSet


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
     self.fields['alc_geografico'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Instituciones
        fields=['nombre','categoria','presentacion','pag_web','logo','direccion','tel','alc_geografico']
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
        self.fields['alc_geografico'].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = DocInstitucionales
        fields=['nombre','id_inst','presentacion','categoria','link_doc','arch_doc','alc_geografico']

#-----------------------------------------------------------------------------
#  INFRAESTRUCTURA.
#-----------------------------------------------------------------------------
class FormInfraestructura(forms.ModelForm):
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
        funcionamiento = GruposCategorias.objects.get(grupo='Funcionamiento Obra de Toma').idGruposCategorias.values_list('categoria')
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
            #fields=['tipo','funcionamiento','uso','estado','desc_estado']
            exclude = ()
#--------------------------------------------------------------------------------
# FORMSETS PARA CARGAR REGISTROS PADRES E HIJOS: INFRAESTRUCTURA - OBRAS DE TOMA
#--------------------------------------------------------------------------------
ObraTomaFormset = inlineformset_factory(
    Infraestructura, ObrasToma,form=FormObraToma,
    fields=['tipo','funcionamiento','uso','estado','desc_estado'],
    extra=1,can_delete=False)
#-----------------------------------------------------------------------------
# CREAR Y EDITAR COTAS Y NIVELES DE REFERENCIA.
#-----------------------------------------------------------------------------
class FormCyNR(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Form1, self).__init__(*args, **kwargs)
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
        self.fields['id_contacto'].widget.attrs.update({'class': 'form-control'})
        self.fields['categoria']=forms.CharField(label='Categoria', required=False, help_text='Seleccione la categoria',
        widget=forms.Select(attrs={'class':"form-control",'placeholder': 'Categoria','rows':1},choices=CHOICE_CATEGORIAS))
        self.fields['titulo'].widget.attrs.update({'class': 'form-control','type':"text"})
        self.fields['descripcion'].widget.attrs.update({'class': 'form-control','row':3})
        self.fields['fecha_hora']=forms.DateTimeField(help_text='Fecha y Hora de creación',widget=forms.DateTimeInput(attrs={'type': 'datetime-local','class': 'form-control'}))
        self.fields['fecha_hora'].input_formats = ["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"]
                
    class Meta:
        model = Documentos
        fields=['id_contacto','categoria','titulo','descripcion','fecha_hora']

#-----------------------------------------------------------------------------
#  IMÁGENES DE CONTENIDOS.
#-----------------------------------------------------------------------------
class ImgContDoc(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super(ImgContDoc, self).__init__(*args, **kwargs)
       #self.fields['id_doc'].widget.attrs.update({'class': 'form-control'})
       self.fields['categoria'].widget.attrs.update({'class': 'form-control'})
       self.fields['descripcion'].widget.attrs.update({'class': 'form-control'})
       self.fields['ilustracion'].widget.attrs.update({'class': 'form-control'})
       self.fields['imagen'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Imagenes
        exclude = ()

ContImgContFormSet = inlineformset_factory(
    ContDocumentos, Imagenes, form=ImgContDoc, 
    fields=['categoria','descripcion','ilustracion','imagen'], extra=1, can_delete=True
    )   
#-----------------------------------------------------------------------------
#  CONTENIDOS DOCUMENTOS.
#-----------------------------------------------------------------------------
class FormContDoc(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super(FormContDoc, self).__init__(*args, **kwargs)
       #self.fields['id_doc'].widget.attrs.update({'class': 'form-control'})
       self.fields['id_infra'].widget.attrs.update({'class': 'form-control'})
       self.fields['id_cynr'].widget.attrs.update({'class': 'form-control'})
       self.fields['titulo'].widget.attrs.update({'class': 'form-control'})
       self.fields['contenido'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = ContDocumentos
        exclude = ()
        #fields=['id_infra','id_cynr','titulo','contenido']
        
class BaseContDocFormset(BaseInlineFormSet):
    def add_fields(self, form, index):
        super(BaseContDocFormset, self).add_fields(form, index)

        # save the formset in the 'nested' property
        form.nested = ContImgContFormSet(
                        instance=form.instance,
                        data=form.data if form.is_bound else None,
                        files=form.files if form.is_bound else None,
                        prefix='imagen-%s-%s' % (
                            form.prefix,
                            ContImgContFormSet.get_default_prefix()),
                        #extra=1)
                        )

DocContDocFormSet = inlineformset_factory(
    Documentos, ContDocumentos, form=FormContDoc, formset=BaseContDocFormset, 
    fields=['id_infra','id_cynr','titulo','contenido'], extra=1, can_delete=True
    ) 





#-----------------------------------------------------------------------------
# CREAR Y EDITAR NOTICIAS.
#-----------------------------------------------------------------------------
class FormNot(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormNot, self).__init__(*args, **kwargs)
        self.fields['id_infra'].widget.attrs.update({'class': 'form-control'})
        self.fields['id_inst'].widget.attrs.update({'class': 'form-control'})
        self.fields['encabezado'].widget.attrs.update({'class': 'form-control'})
        self.fields['presentacion'].widget.attrs.update({'class': 'form-control'})
        self.fields['fecha_hora']=forms.DateTimeField(help_text='Fecha y Hora de creación',widget=forms.DateTimeInput(attrs={'type': 'datetime-local','class': 'form-control'}))
        self.fields['link_not'].widget.attrs.update({'class': 'form-control'})
        self.fields['arch_not'].widget.attrs.update({'class': 'form-control'})
 
    class Meta:
        model = Noticias
        fields=['id_infra','id_inst','encabezado','presentacion','fecha_hora','link_not','arch_not']
