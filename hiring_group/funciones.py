from Aplicaciones.HG_APPS.models import *
import random
import string

def registrar_Utrabajador(user):
    existe_cedula = Usuario.objects.filter(cedula=user[0]).exists()
    existe_correo = Usuario.objects.filter(correo=user[3]).exists()

    if existe_cedula or existe_correo:
        return False
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
        return True
    
def validar_login(correo, contraseña):
    try:
        usuario = Usuario.objects.get(correo=correo)

        if usuario.contraseña == contraseña:
            return 1
        else:
            return 2
    except Usuario.DoesNotExist:
            return 3
    
def identificar_rol(correo, contraseña):
    rol = Usuario.objects.get(rol=rol)
    
    # Si el usuario es de tipo Hiring Group
    if rol == 1:
        return 1
    
    # Si el usuario es de tipo postulante
    if rol == 2:
        return 2
    
    # Si el usuario es de tipo contratado
    if rol == 3:
        return 3

    # Si el usuario es de tipo empresa
    if rol == 4:
        return 4

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