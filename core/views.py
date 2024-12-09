from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .models import UserClass
from django.contrib.auth.models import User
# Create your views here.


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
            username=user_creation_form.cleaned_data.get('username') #crea una variable con el nombre de usuario sacado del formulario
            user= User.objects.get(username=username) #instancia un usuario usando el nombre de usuario anterior
            ocupacion=user_creation_form.cleaned_data.get("ocupacion") #lo mismo que el nombre de usuario pero para la ocupacion
            user_data = UserClass.objects.create(user=user,ocupacion=ocupacion) #se instancia el modelo userclass usando al usuario y la ocupación declaradas anteriormente
            user_data.save() #se guardan los datos entregados
            #user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            #login(request, user)
            return redirect('/')
        else:
            data['form'] = user_creation_form

    return render(request, 'registration/register.html', data)


def logout_view(request):
    logout(request)
    return redirect('core/index.html')

