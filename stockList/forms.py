from django import forms
from .models import Tables

class TablesCreateForm(forms.ModelForm):
    class Meta:
        model=Tables
        fields=['codProd', 'nomProd', 'calificacion', 'tipoProd', 'stock']

class TablesUpdateForm(forms.ModelForm):
    class Meta:
        model=Tables
        fields=['nomProd', 'calificacion', 'tipoProd', 'stock']

class TablesReorderForm(forms.ModelForm):
	class Meta:
		model = Tables
		fields = ['stock'] #Número para trackear cuando tiene que ser ordenado otro producto