from django.contrib.auth.backends import BaseBackend
from Aplicaciones.HG_APPS.models import Usuario


class TuBackendDeAutenticacion(BaseBackend):
    def authenticate(self, request,correo=None, contraseña=None):
        try:
            usuario = Usuario.objects.get(correo=correo)
            if usuario.check_password(contraseña):
                return usuario
        except Usuario.DoesNotExist:
            return None
    
    def get_user(self, user_id):
        try:
            return Usuario.objects.get(cedula=user_id)
        except Usuario.DoesNotExist:
            return None