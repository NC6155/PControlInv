from django.db import models
from django.contrib.auth.models import User

# Create your models here.
tiposUsuario=(("Bodeguero", "Bodeguero"), ("Jefe de Inventario","Jefe de Inventario"))

class UserClass(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #crea una variable usuario que actúa como foránea del usuario principal
    ocupacion=models.TextField(max_length=20, blank=False, null=False, choices=tiposUsuario, verbose_name="Ocupación") #Crea la variable de la ocupación del usuario

    class Meta:
        verbose_name="Ocupación de usuario"
        verbose_name_plural="Ocupaciones de usuario"
    
    def __str__(self):
        return self.ocupacion