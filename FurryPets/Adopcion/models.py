from django.db import models


# Create your models here.

class Dueño(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=100)
    apellidos= models.CharField(max_length=100)
    telefono= models.CharField(max_length=12)
    correo= models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Mascotas(models.Model):
    nombre= models.CharField(max_length=100)
    foto= models.ImageField(upload_to='mascotas',null=True,blank=True)
    tipo_mascota= models.CharField(max_length=100)
    dueño= models.ForeignKey(Dueño,models.CASCADE,null=True)
    ciudad= models.CharField(max_length=200)
    descripcion= models.TextField()

    def __str__(self):
        return self.nombre
        return self.dueño

