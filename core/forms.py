from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

tiposUsuario=(("bodeguero", "Bodeguero"), ("jefe de Inventario","Jefe de Inventario"))
class CustomUserCreationForm(UserCreationForm):
	username=forms.CharField(label="Ingrese su nombre de usuario" ,required=True, widget=forms.TextInput(attrs={"class":"form-control form-control-user"}))
	email = forms.EmailField(label="Ingrese su Email", required=True, widget=forms.EmailInput(attrs={"class":"form-control form-control-user", "aria-describedby":"emailHelp"}))
	first_name=forms.CharField(label="Ingrese su primer nombre",required=True, widget=forms.TextInput(attrs={"class":"form-control form-control-user"}))
	last_name=forms.CharField(label="Ingrese su segundo nombre",required=True, widget=forms.TextInput(attrs={"class":"form-control form-control-user"}))
	ocupacion=forms.ChoiceField(choices=tiposUsuario, required=True)
	password1=forms.CharField(label="Ingrese su contraseña", required=True, widget=forms.PasswordInput(attrs={"class":"form-control form-control-user"}))
	password2=forms.CharField(label="Reingrese su contraseña", required=True, widget=forms.PasswordInput(attrs={"class":"form-control form-control-user"}))

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'ocupacion']
	def clean_email(self):
		email = self.cleaned_data['email']

		if User.objects.filter(email=email).exists():
			raise forms.ValidationError('Este correo electrónico ya está registrado')
		return email
