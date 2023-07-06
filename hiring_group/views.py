from django.http import HttpResponse
from django.shortcuts import render, redirect
from Aplicaciones.HG_APPS.models import *

# 1 forma de hacerlo 
def index(request):
    titulo = "Hiring Group"
    
    return render(request, "index.html", {"titulo": titulo})

# 2 forma de hacerlo
def plantillaParametros(request):
    titulo = "Hiring Group"
     
    return render(request, 'plantillaParametros.html', {"titulo": titulo})

# permite a los usuarios iniciar sesión con su correo electrónico y contraseña
def inicio_sesion(request):
    # Aquí puedes agregar el código para manejar la vista de inicio de sesión
    return render(request, "inicio_sesion.html")

# permite a los usuarios registrarse
def registro_postulantes(request):
    if request.method == 'POST':
        cedula = request.POST['cedula']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        correo = request.POST['correo']
        contrasena = request.POST['contrasena']
        sexo = request.POST['sexo']
        telefono = request.POST['telefono']
        tipo_sangre = request.POST['tipo_sangre']
        contacto = request.POST['contacto']
        numero_emergencia = request.POST['numero_emergencia']

        usuario = UTrabajador(
            cedula=cedula,
            nombre=nombre,
            apellido=apellido,
            correo=correo,
            contraseña=contrasena,
            sexo=sexo,
            telefono=telefono,
            rol=2,
            tipo_de_sangre=tipo_sangre,
            persona_de_contacto=contacto,
            numero_de_emergencia=numero_emergencia)

        usuario.save()

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
    if request.method == 'POST':
        nombre = request.POST['Nombre_empresa']
        sector = request.POST['Sector_empresa']
        
        # Verificar si ya existe una empresa con el mismo nombre
        if Empresa.objects.filter(nombre=nombre).exists():
            error_message = 'Ya existe una empresa con ese nombre.'
            ListaEmpresa = Empresa.objects.all()
            return render(request, "ListaEmpresa.html", {"Empresas": ListaEmpresa, "error_message": error_message})
        
        ultimo_id = Empresa.objects.latest('id').id if Empresa.objects.exists() else 0
        nueva_empresa = Empresa(id=ultimo_id + 1, nombre=nombre, sector=sector)
        nueva_empresa.save()
    
    ListaEmpresa = Empresa.objects.all()
    return render(request, "ListaEmpresa.html", {"Empresas": ListaEmpresa})



