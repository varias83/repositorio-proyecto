from django import forms
from .models import Notas, Docente, Estudiante, Asiganatura, Profile


class Formularionota(forms.ModelForm):
    class Meta:
        model = Notas
        fields = '__all__'

class Formulariodocente(forms.ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'

class FormularioEstudiante(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'

class Formularioasignatura(forms.ModelForm):
    class Meta:
        model = Asiganatura
        fields = '__all__'

class Formularioperfil(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'