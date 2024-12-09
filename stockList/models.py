from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

tiposDeProducto = (("Original", "Original"), ("Marca alterna", "Marca alterna"))

class Tables(models.Model):
    codProd = models.IntegerField(default=0, blank=False, null=False)
    nomProd = models.CharField(max_length=20, blank=False, null=False)
    calificacion = models.TextField(max_length=20, blank=False, null=False, choices=tiposDeProducto, verbose_name="Calificación")
    tipoProd = models.TextField(max_length=13, blank=False, null=False)
    stock = models.IntegerField(default=0, blank=False, null=False)

    class Meta:
        verbose_name = "Table"
        verbose_name_plural = "Tables"
    
    def __str__(self):
        return self.nomProd

    def clean(self):
        #valida que solo Stock 
        if self.stock < 0:
            raise ValidationError("El stock no puede ser menor que 0.")
        #valida que solo sean numeros con isdigit
        if not str(self.codProd).isdigit:
            raise ValidationError("El código del producto debe contener solo números.")

    def save(self, *args, **kwargs):
        self.clean()  
        super().save(*args, **kwargs)
