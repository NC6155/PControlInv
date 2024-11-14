from django.contrib import admin
from .models import Tables
from .forms import TablesCreateForm

# Register your models here.

class BodegueroIngresaStock(admin.ModelAdmin):
    list_display = ['codProd', 'nomProd', 'calificacion', 'stock']
    form = TablesCreateForm
    list_filter = ['codProd', 'stock']
    search_fields = ['codProd', 'nomProd']

admin.site.register(Tables, BodegueroIngresaStock)