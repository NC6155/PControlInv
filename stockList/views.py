from django.shortcuts import render
from .models import Tables
from django.core.paginator import Paginator


# Create your views here.

def tables(request):
    tablesEntries=Tables.objects.all()
    paginator = Paginator(tablesEntries, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "stockList/tables.html",
                  {"page_obj": page_obj})