"""PControlInv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views as cViews
from stockList import views as sViews
from django.conf import settings

urlpatterns = [
    path('stockList/', include(('stockList.urls', 'stockList'), namespace='stockList')),
    path('admin/', admin.site.urls),
    path('', cViews.login, name='login'),
    path('index/', cViews.index, name='index'),
    path('register/', cViews.register, name='register'),
    path('tables/', sViews.tables, name='tables'),
    path('adding_stock/', sViews.add_stock, name='stockAdd'),
    path('reporte_excel/', sViews.ReporteExcel.as_view(), name='reporte_excel'),
    path('update_stock/<str:pk>/', sViews.update_stock, name="update_stock"),
    path('delete_stock/<str:pk>/', sViews.delete_stock, name="delete_stock"),
    path('reorder_stock/<str:pk>/', sViews.reorder_stock, name="reorder_stock"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
