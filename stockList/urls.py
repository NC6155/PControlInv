from django.urls import path
from . import views

app_name = 'stockList'

urlpatterns = [
    path('reporte_excel/', views.ReporteExcel.as_view(), name='reporte_excel'),
]
