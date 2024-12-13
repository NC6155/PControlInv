from django import forms
from .models import Tables
from django.forms import CharField, IntegerField

class TablesCreateForm(forms.ModelForm):
    codProd=IntegerField( label="Codigo del producto " ,required=True, widget=forms.NumberInput(attrs={'class':'form-control form-control-user bg-light small', 'aria-describedby':'basic-addon2'}))
    nomProd=CharField( label="Nombre del producto",max_length=20, required=True, widget=forms.TextInput(attrs={'class':'form-control form-control-user bg-light small', 'aria-describedby':'basic-addon2'}))
    tipoProd=CharField(label="Tipo del producto", max_length=13, required=True, widget=forms.TextInput(attrs={'class':'form-control form-control-user bg-light small', 'aria-describedby':'basic-addon2'}))
    stock=IntegerField(label="Stock del producto", required=True, widget=forms.NumberInput(attrs={'class':'form-control form-control-user bg-light small', 'aria-describedby':'basic-addon2'}))



    class Meta:
        model=Tables
        fields=['codProd', 'nomProd', 'calificacion', 'tipoProd', 'stock']
    def clean_codProd(self):
        codProd = self.cleaned_data['codProd']

        if Tables.objects.filter(codProd=codProd).exists():
            raise forms.ValidationError('Código de producto ya existente')
        return codProd



class TablesUpdateForm(forms.ModelForm):
    nomProd=CharField( label="Nombre del producto",max_length=20, required=True, widget=forms.TextInput(attrs={'class':'form-control form-control-user bg-light small', 'aria-describedby':'basic-addon2'}))
    tipoProd=CharField(label="Tipo del producto", max_length=13, required=True, widget=forms.TextInput(attrs={'class':'form-control form-control-user bg-light small', 'aria-describedby':'basic-addon2'}))
    stock=IntegerField(label="Stock del producto", required=True, widget=forms.NumberInput(attrs={'class':'form-control form-control-user bg-light small', 'aria-describedby':'basic-addon2'}))
    
    class Meta:
        model=Tables
        fields=['nomProd', 'calificacion', 'tipoProd', 'stock']

class TablesSearchForm(forms.ModelForm):
    codProd=IntegerField( label="Codigo" ,required=False, widget=forms.NumberInput(attrs={'class':'form-control form-control-user bg-light small', 'aria-describedby':'basic-addon2'}))
    nomProd=CharField( label="Nombre",max_length=20, required=False, widget=forms.TextInput(attrs={'class':'form-control form-control-user bg-light small', 'aria-describedby':'basic-addon2'}))

    class Meta:
        model = Tables
        fields = ['codProd', 'nomProd']

