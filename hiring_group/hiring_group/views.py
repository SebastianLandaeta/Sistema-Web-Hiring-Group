from django.http import HttpResponse
from django.shortcuts import render

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
def registro(request):
    # Aquí puedes agregar el código para manejar la vista de registro
    return HttpResponse("Vista de registro")

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