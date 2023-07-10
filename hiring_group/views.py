from django.http import HttpResponse
from django.shortcuts import render, redirect
from Aplicaciones.HG_APPS.models import *
from hiring_group.procesamiento import *
import warnings

# 1 forma de hacerlo
def index(request):
    warnings.warn("¡ventana de prueba!")
    return render(request, "index.html")


# permite a los usuarios iniciar sesión con su correo electrónico y contraseña
def inicio_sesion(request):
    # Aquí puedes agregar el código para manejar la vista de inicio de sesión
    return render(request, "inicio_sesion.html")


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
        registrar_Utrabajador(user)

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
                "ListaEmpresa.html",
                {"Empresas": ListaEmpresa, "error_message": error_message},
            )

        ultimo_id = Empresa.objects.latest("id").id if Empresa.objects.exists() else 0
        nueva_empresa = Empresa(id=ultimo_id + 1, nombre=nombre, sector=sector)
        nueva_empresa.save()

    ListaEmpresa = Empresa.objects.all()
    return render(request, "ListaEmpresa.html", {"Empresas": ListaEmpresa})
