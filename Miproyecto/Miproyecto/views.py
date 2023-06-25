from django.http import HttpResponse
from django.template import Template, Context

def index(request):
    titulo="Hiring Group"
    
    # se abrio el documento en donde esta la plantilla 
    plantillaExterna = open("C:\Miproyecto\Miproyecto\plantillas/index.html")
    
    # cargo el documento en una variable tipo Template
    template = Template(plantillaExterna.read())
    
    # cierro el documento
    plantillaExterna.close()
    
    #  crea un contexto xd
    contexto = Context( {"nombrePagina": titulo} )
    
    # Renderiza el documento y lo retorna
    return HttpResponse( template.render(contexto) )

# permite a los usuarios iniciar sesión con su correo electrónico y contraseña
def inicio_sesion(request):
    # Aquí puedes agregar el código para manejar la vista de inicio de sesión
    return HttpResponse("Vista de inicio de sesión")

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