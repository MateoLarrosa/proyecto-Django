from django.db import models

#Lo que esta en los modelos se guarda en la base de datos
#Cuando se hacen los cambios tenes que usar el comando: python manage.py makemigrate
# y despues usar el comando python manage.py migrate
#Se va a crear en la carpeta migrations un archivo por cada cambio que hagamos cuando hagamos el make y el migrations
# Create your models here.
class Animal(models.Model):
     nombre = models.CharField(max_length=20) #charfield si o si se le pasa el maxlenght del str
     edad =  models.IntegerField() #No es necesario pasarle valor

class Familiares(models.Model):
     nombre = models.CharField(max_length=20)
     apellido = models.CharField(max_length=20)
     fecha_nacimiento = models.CharField(max_length=10)
     documento = models.IntegerField()
     edad = models.IntegerField()