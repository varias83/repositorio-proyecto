from django.contrib import admin
from .models import Profile, Docente, Estudiante, Asiganatura, Notas
# Register your models here.

@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ('id', 'genero','documento','fechanacimiento',)
    list_filter = ('genero',)

@admin.register(Estudiante)
class AdminEstudiante(admin.ModelAdmin):
    list_display = ('id','observador',)


@admin.register(Docente)
class AdminDocente(admin.ModelAdmin):
    list_display = ('id', 'Profesion',)
    list_filter = ('Profesion',)


@admin.register(Asiganatura)
class Adminasignatura(admin.ModelAdmin):
    list_display = ('id', 'Instrumento',)
    list_filter = ('Instrumento',)


@admin.register(Notas)
class Adminnotas(admin.ModelAdmin):
    list_display = ('id', 'nota1', 'nota2', 'nota3', 'nota4',)