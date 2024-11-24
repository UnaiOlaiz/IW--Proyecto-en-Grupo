from django import forms
from .models import Pais, Aeropuerto, Aerolinea

class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ['nombre', 'capital', 'codigo', 'imagen', 'descripcion']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4, 'cols': 40, 'placeholder': 'Añade una descripción'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class AeropuertoForm(forms.ModelForm):
    class Meta:
        model = Aeropuerto
        fields = ['codigo', 'nombre', 'pais', 'tlf', 'imagen']
        widgets = {
            'codigo': forms.TextInput(attrs={'maxlength': 3, 'placeholder': 'Código (3 letras)'}),
            'tlf': forms.NumberInput(attrs={'placeholder': 'Teléfono del aeropuerto'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class AerolineaForm(forms.ModelForm):
    class Meta:
        model = Aerolinea
        fields = ['nombre', 'pais', 'aeropuertos', 'tlf', 'fundacion', 'descripcion', 'flota', 'imagen']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4, 'cols': 40, 'placeholder': 'Descripción de la aerolínea'}),
            'fundacion': forms.DateInput(attrs={'type': 'date'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'aeropuertos': forms.CheckboxSelectMultiple(),
        }
