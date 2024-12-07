from django import forms
from .models import Tables
from django.forms import CharField, IntegerField

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

class TablesSearchForm(forms.ModelForm):
    codProd=IntegerField( label="Codigo" ,required=False)
    nomProd=CharField( label="Nombre",max_length=20, required=False)

    class Meta:
        model = Tables
        fields = ['codProd', 'nomProd']