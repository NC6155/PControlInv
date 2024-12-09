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
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('stockList/', include(('stockList.urls', 'stockList'), namespace='stockList')),
    path('admin/', admin.site.urls),
    path('', login_required(cViews.index), name='index'),
    path('register/', include('core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('tables/', login_required(sViews.tables), name='tables'),
    path('adding_stock/', login_required(sViews.add_stock), name='stockAdd'),
    path('reporte_excel/', login_required(sViews.ReporteExcel.as_view()), name='reporte_excel'),
    path('update_stock/<str:pk>/', login_required(sViews.update_stock), name="update_stock"),
    path('delete_stock/<str:pk>/', login_required(sViews.delete_stock), name="delete_stock"),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('reducir_stock/', login_required(sViews.reducir_stock), name='reducir_stock')
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
