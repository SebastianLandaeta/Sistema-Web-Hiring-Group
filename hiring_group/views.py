from django.http import HttpResponse
from django.shortcuts import render, redirect
from Aplicaciones.HG_APPS.models import *
from hiring_group.funciones import *
import warnings
from django.contrib.auth import authenticate, login

# 1 forma de hacerlo
def index(request):
    warnings.warn("¡ventana de prueba!")
    return render(request, "index.html")


# permite a los usuarios iniciar sesión con su correo electrónico y contraseña
def inicio_sesion(request):
    if request.method == "POST":
        correo = request.POST["correo"]
        contraseña = request.POST["contraseña"]
        
        respuesta = validar_login(correo, contraseña)

        # En caso de que haya hecho el login correctamente
        if respuesta == 1:
            return render(request, 'inicio_valido.html')
        
        # En caso de que exista el correo pero la clave sea invalida
        if respuesta == 2:
            error_message = 'Contraseña invalida.'
            return render(request, 'inicio_sesion.html', {'error_message': error_message})
        
        # En caso de que el correo no exista
        if respuesta == 3:
            error_message = 'El correo no existe.'
            return render(request, 'inicio_sesion.html', {'error_message': error_message})
    
    return render(request, 'inicio_sesion.html')

    
def inicio_valido(request):
    return render(request, 'inicio_valido.html')

# permite a los usuarios registrarse
def registro_postulantes(request):
    if request.method == "POST":
        user = list()
        user.append(request.POST["cedula"])
        user.append(request.POST["nombre"])
        user.append(request.POST["apellido"])
        user.append(request.POST["correo"])
        user.append(request.POST["contrasena"])
        user.append(request.POST["sexo"])
        user.append(request.POST["telefono"])
        user.append(2)
        user.append(request.POST["tipo_sangre"])
        user.append(request.POST["contacto"])
        user.append(request.POST["numero_emergencia"])
    
        if registrar_Utrabajador(user):
            return render(request, "inicio_sesion.html")
        else:
            error_message = 'Cédula o correo ya existentes.'
            return render(request, "registro_postulantes.html", {'error_message': error_message})

    return render(request, "registro_postulantes.html")


# muestra una lista de todas las ofertas disponibles
def lista_ofertas(request):
    # Aquí puedes agregar el código para manejar la vista de lista de ofertas
    return HttpResponse("Listado de ofertas")


# muestra información detallada sobre una oferta
def detalle_oferta(request, oferta_id):
    # Aquí puedes agregar el código para manejar la vista de detalle de oferta
    return HttpResponse(f"Vista de detalle de oferta {oferta_id}")


# permite a los usuarios postularse a una oferta
def postulacion(request, oferta_id):
    # Aquí puedes agregar el código para manejar la vista de postulación
    return HttpResponse(f"Vista de postulación {oferta_id}")


# muestra una lista de todas las postulaciones realizadas por un usuario
def lista_postulaciones(request):
    # Aquí puedes agregar el código para manejar la vista de lista de postulaciones
    return HttpResponse("Vista de lista de postulaciones")


# permite a los usuarios ver información sobre su contratación en una oferta
def contratacion(request, oferta_id):
    # Aquí puedes agregar el código para manejar la vista de contratación
    return HttpResponse(f"Vista de contratación {oferta_id}")


# muestra información sobre la nómina de una empresa
def nomina(request, empresa_id):
    # Aquí puedes agregar el código para manejar la vista de nómina
    return HttpResponse(f"Vista de nómina {empresa_id}")


def Registro_empresa(request):
    if request.method == "POST":
        nombre = request.POST["Nombre_empresa"]
        sector = request.POST["Sector_empresa"]

        # Verificar si ya existe una empresa con el mismo nombre
        if Empresa.objects.filter(nombre=nombre).exists():
            error_message = "Ya existe una empresa con ese nombre."
            ListaEmpresa = Empresa.objects.all()
            return render(
                request,
                "registro_empresa.html",
                {"Empresas": ListaEmpresa, "error_message": error_message},
            )

        ultimo_id = Empresa.objects.latest("id").id if Empresa.objects.exists() else 0
        nueva_empresa = Empresa(id=ultimo_id + 1, nombre=nombre, sector=sector)
        nueva_empresa.save()

    ListaEmpresa = Empresa.objects.all()
    return render(request, "registro_empresa.html", {"Empresas": ListaEmpresa})
