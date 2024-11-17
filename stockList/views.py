from django.shortcuts import render, redirect
from .models import Tables
from django.core.paginator import Paginator
from .forms import TablesCreateForm
from django.views.generic import TemplateView
from openpyxl import Workbook
from django.http import HttpResponse




# Create your views here.

def tables(request):
    tablesEntries=Tables.objects.all().order_by('id')
    paginator = Paginator(tablesEntries, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "stockList/tables.html",
                  {"page_obj": page_obj})

def add_stock(request):
    form = TablesCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/adding_stock/')
    context = {
		"form": form,
		"title": "Add Item",
	}
    return render(request, "stockList/add_stock.html", context)

class ReporteExcel(TemplateView):
    def get(self, request, *args, **kwargs):
        productos = Tables.objects.all()
        wb = Workbook()
        ws = wb.active
        ws['B1'] = 'Productos de Bodega'
        ws.merge_cells('B1:E1')
        ws['B3'] = 'CodPro'
        ws['C3'] = 'NomPro'
        ws['D3'] = 'Calificacion'
        ws['E3'] = 'TipoProd'
        ws['F3'] = 'Stock'
        cont = 5
        for producto in productos:
            ws.cell(row=cont, column=2).value = producto.codProd
            ws.cell(row=cont, column=3).value = producto.nomProd
            ws.cell(row=cont, column=4).value = producto.calificacion
            ws.cell(row=cont, column=5).value = producto.tipoProd
            ws.cell(row=cont, column=6).value = producto.stock
            cont += 1
        nombre_archivo = "Productos_Bodega.xlsx"
        response = HttpResponse(content_type='application/ms-excel')
        content = "attachment; filename={0}".format(nombre_archivo)
        response['Content-Disposition'] = content
        wb.save(response)
        return response
