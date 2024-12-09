from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
# Create your views here.

def login(request):
    return render(request, "registration/login.html")

#def register(request):
    #return render(request, "registration/register.html")

@login_required
def index(request):
    return render(request, "core/index.html")

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            #user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            #login(request, user)
            return redirect('index')
        else:
            data['form'] = user_creation_form

    return render(request, 'registration/register.html', data)


def logout_view(request):
    logout(request)
    return redirect('core/index.html')

