from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile (models.Model):
    genero=((1,"M"),
            (2,"F"),
            (3,"Otro"),)
    documento=models.CharField(max_length=50)
    telefono=models.CharField(max_length=50)
    fechanacimiento=models.DateField()
    genero=models.SmallIntegerField(choices=genero)
    user=models.OneToOneField(User, on_delete=models.PROTECT)
    class Meta:
        db_table='profile'

    def __str__(self):
        return self.documento

    def __str__(self):
        return self.telefono

class Estudiante(models.Model):
    observador=models.CharField(max_length=500)
    user=models.OneToOneField(User, on_delete=models.PROTECT)
    class Meta:
        db_table='estudiante'

    def __str__(self):
        return self.observador

class Docente(models.Model):
    Profesion= ((1,"Licenciatura En Musica"),
                (2,"Director de orquesta"),)
    Profesion=models.SmallIntegerField(choices=Profesion)
    estdiante=models.ForeignKey(Estudiante, on_delete=models.PROTECT)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    class Meta:
        db_table='docente'


class Asiganatura(models.Model):
    Instrumento= ((1,"de cuerda"),
                  (2,"de percusion"),
                  (3,"de teclado"),)
    Instrumento=models.SmallIntegerField(choices=Instrumento)
    docente=models.ForeignKey(Docente, on_delete=models.PROTECT)
    estdiante=models.ForeignKey(Estudiante, on_delete=models.PROTECT)
    class Meta:
        db_table='asigantura'

class Notas(models.Model):
     nota1 = models.CharField(max_length=20)
     nota2 = models.CharField(max_length=20)
     nota3 = models.CharField(max_length=20)
     nota4 = models.CharField(max_length=20)
     docente = models.ForeignKey(Docente, on_delete=models.PROTECT)
     asignatura = models.ForeignKey(Asiganatura, on_delete=models.PROTECT)
     class Meta:
         db_table = 'notas'
     def __str__(self):
         return self.nota1

     def __str__(self):
         return self.nota2

     def __str__(self):
         return self.nota3

     def __str__(self):
         return self.nota4
