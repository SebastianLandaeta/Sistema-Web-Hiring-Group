from Aplicaciones.HG_APPS.models import *
from django.shortcuts import redirect
import random
import string

    # Si el usuario es de tipo Hiring Group = 1
    # Si el usuario es de tipo postulante = 2
    # Si el usuario es de tipo contratado = 3
    # Si el usuario es de tipo empresa = 4


def verificar_correo(correo_u):
    existe_correo = Usuario.objects.filter(correo=correo_u).exists()
    if existe_correo:
        return True
    else:
        return False
    
def registrar_Utrabajador(user):
    
    usuario = Usuario(
    correo=user[0],
    password=user[1],
    cedula=user[2],
    nombre=user[3],
    apellido=user[4],
    sexo=user[5],
    telefono=user[6],
    rol=user[7],
    )

    utrabajador = UTrabajador(
    tipo_de_sangre=user[8],
    persona_de_contacto=user[9],
    numero_de_emergencia=user[10],
    usuario_id=user[2]                 
    )

    usuario.save()
    Usuario.objects.create_user(correo=user[0], contraseña=user[1])
    utrabajador.save()
    return utrabajador
    
def verificar_existencia_empresa(nombre):
    existe_empresa = Empresa.objects.filter(nombre=nombre).exists()
    if existe_empresa:
        return True
    else:
        return False

def verificar_cedula(cedula_u):
    existe_cedula = Usuario.objects.filter(cedula=cedula_u).exists()
    if existe_cedula:
        return True
    else:
        return False

def registrar_empresa(nombre,sector):
    ultimo_id = Empresa.objects.latest("id").id if Empresa.objects.exists() else 0
    nueva_empresa = Empresa(id=ultimo_id + 1, nombre=nombre, sector=sector)
    nueva_empresa.save()
    return nueva_empresa    

def registrar_Uempresa(user = Usuario,u_empresa = UEmpresa):
    user.save()
    Usuario.objects.create_user(correo=user.correo, contraseña=user.password)
    u_empresa.save()
    
def correo_existe(correo):
    existe_correo=Usuario.objects.filter(correo=correo).exists()
    if existe_correo:
        return True
    else:
        return False

def generar_correo(nombre_empresa, cedula, nombre, apellido):
    dominio = nombre_empresa.lower().replace(' ', '') + ".com"
    apellido_inicial = apellido[0]  # Obtiene la inicial del apellido
    numeros_cedula = str(cedula)[-3:]  # Obtiene los últimos 3 dígitos de la cédula
    
    # Generar correo inicial
    correo = f"{nombre.lower().replace(' ', '')}.{apellido_inicial}{numeros_cedula}@{dominio}"
    
    # Verificar si el correo ya existe
    while correo_existe(correo):  # Reemplaza "correo_existe" con tu propia lógica de verificación
        # Generar un correo aleatorio con otros datos del usuario
        letras_aleatorias = random.choices(string.ascii_lowercase, k=3)  # Generar 3 letras aleatorias
        numeros_aleatorios = random.choices(string.digits, k=3)  # Generar 3 números aleatorios
        
        # Construir un correo aleatorio con los datos del usuario
        correo = f"{nombre.lower().replace(' ', '')}.{apellido_inicial}{numeros_cedula}{letras_aleatorias}{numeros_aleatorios}@{dominio}"
    
    return correo

def generar_contraseña():
    longitud = random.randint(4, 8)  # Genera una contraseña aleatoria de 4 a 8 caracteres
    caracteres = string.ascii_lowercase + string.digits  # Solo letras minúsculas y dígitos
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def verificar_existencia_area(nombre_area):
    existe_area = AreaDeConocimiento.objects.filter(nombre=nombre_area).exists()
    if existe_area:
        return True
    else:
        return False
    
def registrar_area(nombre_a,descripcion):
    ultimo_id = AreaDeConocimiento.objects.latest("id").id if AreaDeConocimiento.objects.exists() else 0
    nueva_area= AreaDeConocimiento(id=ultimo_id + 1, nombre=nombre_a, descripcion=descripcion)
    nueva_area.save()

def verificar_existencia_banco(nro_banco):
    existe_banco= Banco.objects.filter(nro_de_cuenta=nro_banco).exists()
    if existe_banco:
        return True
    else:
        return False
    
def registrar_banco(nro_banco,nombre_b):
    nuevo_banco= Banco(nro_de_cuenta=nro_banco, nombre=nombre_b)
    nuevo_banco.save()

def redirecion(rol):
    if rol==1:
        return redirect('inicio hg')   
    elif rol==2:
        return redirect('inicio postulante')
    elif rol==3:
        return redirect('inicio contratado')
    elif rol==4: 
        return redirect('inicio empresa')
    
def registrar_ac(area_id,trabajador_n):
    ultimo_id = AreaTrabajador.objects.latest("id").id if AreaTrabajador.objects.exists() else 0
    area_trabajador = AreaTrabajador(id=ultimo_id+1,trabajador=trabajador_n, area_de_conocimiento_id=area_id)
    area_trabajador.save()

def actualizar_usuario(cedula, nuevo_correo, nueva_contraseña):
    try:
        usuario = Usuario.objects.get(cedula=cedula)
        usuario.correo = nuevo_correo
        usuario.set_password(nueva_contraseña)
        usuario.save()
        return True
    except Usuario.DoesNotExist:
        return False
