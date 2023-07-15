from django.http import HttpResponse
from django.shortcuts import render, redirect
from Aplicaciones.HG_APPS.models import *
from hiring_group.funciones import *
from django.contrib.auth import authenticate,login,logout,get_user
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# 1 forma de hacerlo
def index(request):
    if request.user.is_authenticated:
        User = request.user.nombre
        print(User)
    return render(request, "index.html")

def inicio_sesion(request):
    next_page = request.GET.get('next')

    if request.method == "POST":
        correo = request.POST["correo"]
        contraseña = request.POST["contraseña"]
        user = authenticate(correo=correo, contraseña=contraseña)

        if user is not None:
            login(request, user)

            if next_page:
                return redirect(next_page)  # Redirigir al usuario a la página 'next' después de iniciar sesión
            else:
                return redirrecion(user.rol)  # Redirigir al usuario a la página de inicio válida

        else:
            error_message = 'Credenciales inválidas. Por favor, inténtalo de nuevo.'
            return render(request, 'inicio_sesion.html', {'error_message': error_message})

    return render(request, 'inicio_sesion.html', {'next_page': next_page})


def cerrar_sesion(request):
    logout(request)
    return render(request, 'index.html')

def inicio_valido(request):
    return render(request, 'inicio_valido.html')

def registro_postulantes(request):
    if request.method == "POST":
        user = list()
        user.append(request.POST["correo"])
        user.append(request.POST["contrasena"])
        user.append(request.POST["cedula"])
        user.append(request.POST["nombre"])
        user.append(request.POST["apellido"])
        user.append(request.POST["sexo"])
        user.append(request.POST["telefono"])
        user.append(2)
        user.append(request.POST["tipo_sangre"])
        user.append(request.POST["contacto"])
        user.append(request.POST["numero_emergencia"])

        if verificar_cedula(user[2]):
            error_message = 'Cédula ya existente.'
            return render(request, "registro_postulantes.html", {'error_message': error_message})
    
        elif verificar_correo(user[0]):
            error_message = 'Correo ya existente.'
            return render(request, "registro_postulantes.html", {'error_message': error_message})
        else:
            registrar_Utrabajador(user)
            return render(request, "index.html")

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


def registro_empresa(request):
    if request.method == "POST":
        nombre = request.POST["Nombre_empresa"]
        sector = request.POST["Sector_empresa"]
        cedula_u = request.POST["cedula"]
        nombre_u = request.POST["nombre"]
        apellido_u = request.POST["apellido"]
        telefono_u = request.POST["telefono"]
        sexo_u = request.POST["sexo"]

        # Verificar si ya existe una empresa con el mismo nombre
        if verificar_existencia_empresa(nombre):
            error_message = "Ya existe una empresa con ese nombre."
            ListaEmpresa = Empresa.objects.all()
            if not ListaEmpresa:
                ListaEmpresa=None
            return render(
                request, "registro_empresa.html",
                {"Empresas": ListaEmpresa, "error_message": error_message},
            )
        elif verificar_cedula(cedula_u):
            error_message = "Cedula esta ocupada por otro Usuario"
            ListaEmpresa = Empresa.objects.all()
            if not ListaEmpresa:
                ListaEmpresa=None
            return render(
            request, "registro_empresa.html",
            {"Empresas": ListaEmpresa, "error_message": error_message},
            )
        else:
            empresa=registrar_empresa(nombre, sector)
            clave = generar_contraseña()
            
            usuario_nuevo = Usuario(
            cedula=cedula_u,
            nombre=nombre_u,
            apellido=apellido_u,
            correo=generar_correo(empresa.nombre,cedula_u,nombre_u,apellido_u),
            password=clave,
            sexo=sexo_u,
            telefono=telefono_u,
            rol=4
            )
            
            usuario_empresa = UEmpresa(
            usuario=usuario_nuevo,
            empresa=empresa,
            )

            registrar_Uempresa(usuario_nuevo, usuario_empresa)

            mensaje_felicidades = f"Felicidades, Empresa '{empresa.nombre}' Creada y registrada con éxito"
            ListaEmpresa = Empresa.objects.all()
            if not ListaEmpresa:
                ListaEmpresa=None
            return render(
            request, "registro_empresa.html",
            {"Empresas": ListaEmpresa, "mensaje_felicidades": mensaje_felicidades, 'correo':usuario_nuevo.correo, 'contraseña':clave},
            )
        
    ListaEmpresa = Empresa.objects.all()
    return render(request, "registro_empresa.html", {"Empresas": ListaEmpresa},)


def panel_usuarios(request): #VISTA USUARIO HIRING GROUP
    # Obtener todos los usuarios trabajadores
    trabajadores = UTrabajador.objects.all()

    if not trabajadores:
        trabajadores = None

    # Obtener todos los usuarios empresas
    empresas = UEmpresa.objects.all()

    if not empresas:
        empresas = None

    # Renderizar la plantilla 'panel_usuarios.html' con los datos de los usuarios
    return render(request, 'panel_usuarios(vista_HG).html', {'trabajadores': trabajadores, 'empresas': empresas})

def registro_area_conocimiento(request):
    if request.method == "POST":
        nombre_a = request.POST["Nombre_area"]
        descripcion = request.POST["Descripcion_area"]
        if verificar_existencia_area(nombre_a):
                error_message = "Ya existe esa area registrada."
                ListaArea = AreaDeConocimiento.objects.all()
                if not ListaArea:
                    ListaArea=None
                return render(
                    request, "registro_ac.html",
                    {"Areas": ListaArea, "error_message": error_message},
                )
        else:
            registrar_area(nombre_a,descripcion)
            mensaje_felicidades = f" Area '{nombre_a}' Creada y registrada con éxito"
            ListaArea = AreaDeConocimiento.objects.all()
            return render(request, "registro_ac.html", {"Areas": ListaArea,"mensaje_felicidades": mensaje_felicidades},)

    ListaArea = AreaDeConocimiento.objects.all()
    return render(request, "registro_ac.html", {"Areas": ListaArea},)

def registro_banco(request):
    if request.method == "POST":
        nro_banco= request.POST["nro_banco"]
        nombre_b = request.POST["Nombre_banco"]
        if verificar_existencia_banco(nro_banco):
                error_message = "Ya existe ese numero de cuenta."
                ListaBanco = Banco.objects.all()
                if not ListaBanco:
                    ListaBanco=None
                return render(
                    request, "registro_banco.html",
                    {"Bancos": ListaBanco, "error_message": error_message},
                )
        else:
            registrar_banco(nro_banco,nombre_b)
            mensaje_felicidades = f"Numero bancario '{nro_banco}' en el banco: '{nombre_b}', Creado y registrada con éxito"
            ListaBanco = Banco.objects.all()
            return render(request, "registro_banco.html", {"Bancos": ListaBanco,"mensaje_felicidades": mensaje_felicidades},)
    
    ListaBanco = Banco.objects.all()
    return render(request, "registro_banco.html", {"Bancos": ListaBanco},)

@login_required(login_url='login')
def inicio_uempresa(request):
    user = request.user
    if user.is_authenticated:
        if user.rol != 4:
            messages.error(request, 'Usted no tiene acceso a esa página. Debe ser un usuario con el rol de Usuario Empresa.', extra_tags='access_denied')
            return redirrecion(user.rol)
    
    return render(request, 'inicio_uempresa.html')

@login_required(login_url='login')
def inicio_upostulante(request):
    user = request.user
    if user.is_authenticated:
        if user.rol != 2:
            messages.error(request, 'Usted no tiene acceso a esa página. Debe ser un usuario con el rol de Usuario postulante.', extra_tags='access_denied')
            return redirrecion(user.rol)
    
    return render(request, 'inicio_upostulante.html')

#@login_required(login_url='login')
def inicio_uhg(request):
    user = request.user
    if user.is_authenticated:
        if user.rol != 1:
            messages.error(request, 'Usted no tiene acceso a esa página. Debe ser un usuario con el rol de Usuario Hiring Group.', extra_tags='access_denied')
            return redirrecion(user.rol)
    
    return render(request, 'inicio_uhg.html')

def inicio_ucontratado(request):
    user = request.user
    if user.is_authenticated:
        if user.rol != 3:
            messages.error(request, 'Usted no tiene acceso a esa página. Debe ser un usuario con el rol de Usuario contratado.', extra_tags='access_denied')
            return redirrecion(user.rol)
    
    return render(request, 'inicio_ucontratado.html')

