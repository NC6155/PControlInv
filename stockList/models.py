from django.db import models

# Create your models here.

class Tables(models.Model):
    codProd=models.IntegerField(max_length=4)
    nomProd=models.CharField(max_length=20)
    calificacion=models.TextField()
    tipoProd=models.TextField()
    stock=models.IntegerField()

    class Meta:
        verbose_name="Table"
        verbose_name_plural="Tables"
    
    def __str__(self):
        return self.codProd