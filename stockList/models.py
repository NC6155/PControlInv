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
        if self.stock < 0:
            raise ValidationError("El stock no puede ser menor que 0.")

    def save(self, *args, **kwargs):
        self.clean()  # Llamamos al método clean para ejecutar la validación
        super().save(*args, **kwargs)
