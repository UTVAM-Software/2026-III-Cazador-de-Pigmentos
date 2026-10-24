from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group, Permission

# FORMULARIO DE REGISTRO DE USUARIOS 
class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo Electrónico")

    class Meta:
        model = User
        fields = ['username', 'email']


# FORMULARIO DE PERMISOS 
class PermisoForm(forms.ModelForm):
    class Meta:
        model = Permission
        fields = ['name', 'codename', 'content_type']
        labels = {
            'name': 'Nombre Descriptivo',
            'codename': 'Código del Permiso',
            'content_type': 'Modelo Asociado',
        }


# FORMULARIO DE ROLES 
class RolForm(forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        
    )

    class Meta:
        model = Group
        fields = ['name', 'permissions']
        labels = {
            'name': 'Nombre del Rol',
        }


# FORMULARIO DE ASIGNACIÓN DE ROLES 
class AsignarRolUsuarioForm(forms.ModelForm):
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Seleccionar los roles "
    )

    class Meta:
        model = User
        fields = ['groups']

class PermisoLimpioField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        traducciones = {
            'add': 'Crear',
            'change': 'Editar',
            'delete': 'Eliminar',
            'view': 'Ver',
        }   
        accion_ingles = obj.codename.split('_')[0]
        accion_espanol = traducciones.get(accion_ingles, accion_ingles).capitalize()
        modelo = obj.content_type.name.capitalize()
        categoria = obj.content_type.app_label.upper()
        return f"[{categoria}] {accion_espanol} {modelo}"
