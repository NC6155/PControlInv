
from .models import UserClass
def user_type(request):
    if request.user.is_authenticated:
        try:
            perfil = UserClass.objects.get(user=request.user)
            return {'perfil_usuario': perfil}
        except UserClass.DoesNotExist:
            return {}
    return {}