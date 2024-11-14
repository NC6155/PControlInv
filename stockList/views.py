from django.shortcuts import render, redirect
from .models import Tables
from django.core.paginator import Paginator
from .forms import TablesCreateForm


# Create your views here.

def tables(request):
    tablesEntries=Tables.objects.all()
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