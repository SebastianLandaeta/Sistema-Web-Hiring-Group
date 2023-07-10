from Aplicaciones.HG_APPS.models import *

def registrar_Utrabajador(user):
    existe = Usuario.objects.filter(cedula=user[0]).exists()

    if existe:
        print("usuario ya registrado")
       
    else:
        usuario = Usuario(
            cedula=user[0],
            nombre=user[1],
            apellido=user[2],
            correo=user[3],
            contraseña=user[4],
            sexo=user[5],
            telefono=user[6],
            rol=user[7]
        )

        utrabajador = UTrabajador(
            tipo_de_sangre=user[8],
            persona_de_contacto=user[9],
            numero_de_emergencia=user[10],
            usuario_id=user[0]                 
        )

        usuario.save()
        utrabajador.save()
        print("usuario registrado correctamente")