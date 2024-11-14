from django import forms
from .models import Tables

class TablesCreateForm(forms.ModelForm):
    class Meta:
        model=Tables
        fields=['codProd', 'nomProd', 'calificacion', 'tipoProd', 'stock']