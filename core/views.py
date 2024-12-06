from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, "core/login.html")

def register(request):
    return render(request, "core/register.html")
    
def index(request):
    return render(request, "core/index.html")
