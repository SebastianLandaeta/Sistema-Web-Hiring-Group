from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.contrib.auth import get_user_model

class UsuarioManager(BaseUserManager):
    def create_user(self, correo, contraseña, **extra_fields):
        existing_user = get_user_model().objects.get(correo=correo)
        usuario = self.model(
            correo=existing_user.correo,
            cedula=existing_user.cedula,
            nombre=existing_user.nombre,
            apellido=existing_user.apellido,
            sexo=existing_user.sexo,
            telefono=existing_user.telefono,
            rol=existing_user.rol,
            **extra_fields
        )
        usuario.set_password(contraseña)
        usuario.save(using=self._db)
        return usuario


    def create_superuser(self, cedula, nombre, apellido, correo, contraseña, sexo, telefono, rol):
        usuario = self.create_user(
            cedula=cedula,
            nombre=nombre,
            apellido=apellido,
            correo=correo,
            contraseña=contraseña,
            sexo=sexo,
            telefono=telefono,
            rol=rol,
        )
        usuario.is_staff = True
        usuario.is_superuser = True
        usuario.save(using=self._db)
        return usuario



class Usuario(AbstractBaseUser):
    cedula = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.CharField(max_length=70, unique=True)  # Agregar unique=True
    sexo = models.CharField(max_length=1)
    telefono = models.BigIntegerField()
    rol = models.SmallIntegerField()
    # Otros campos y métodos de tu modelo
    USERNAME_FIELD = "correo"
    REQUIRED_FIELDS = ["rol"]

    objects = UsuarioManager() 
    class Meta:
        db_table = 'Usuario'
    
    def get_nombre_empresa(self):
        if self.rol == 4:
            try:
                uempresa = UEmpresa.objects.get(usuario=self)
                return uempresa.empresa.nombre
            except UEmpresa.DoesNotExist:
                return ""
        else:
            return ""
    objects = UsuarioManager()


class UTrabajador(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True, default=1)
    tipo_de_sangre = models.CharField(max_length=2)
    persona_de_contacto = models.BigIntegerField()
    numero_de_emergencia = models.BigIntegerField()

    class Meta:
        db_table = 'U_Trabajador'

class AreaDeConocimiento(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=255)

    class Meta:
        db_table = 'Area de conocimiento'


class AreaTrabajador(models.Model):
    id = models.IntegerField(primary_key=True)
    trabajador = models.ForeignKey('UTrabajador', on_delete=models.CASCADE)
    area_de_conocimiento = models.ForeignKey(AreaDeConocimiento, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Area_Trabajador'


class Banco(models.Model):
    nro_de_cuenta = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    #trabajador = models.ForeignKey('UTrabajador', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Banco'


class Contrato(models.Model):
    id = models.IntegerField(primary_key=True)
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField(null=True)
    salario = models.FloatField()
    trabajador = models.ForeignKey('UTrabajador', on_delete=models.CASCADE)
    oferta = models.ForeignKey('Oferta', on_delete=models.CASCADE)
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Contrato'


class Empresa(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    sector = models.CharField(max_length=255)

    class Meta:
        db_table = 'Empresa'


class ExperienciaLaboral(models.Model):
    id = models.IntegerField(primary_key=True)
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()
    cargo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    trabajador = models.ForeignKey('UTrabajador', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Experiencia Laboral'


class Oferta(models.Model):
    id = models.IntegerField(primary_key=True)
    area_de_conocimiento = models.ForeignKey(AreaDeConocimiento, on_delete=models.CASCADE)
    cargo_vacante = models.CharField(max_length=255)
    descripcion_del_cargo = models.CharField(max_length=255, null=True)
    salario = models.FloatField()
    estado = models.BooleanField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Oferta'


class Postulacion(models.Model):
    id = models.IntegerField(primary_key=True)
    trabajador = models.ForeignKey(UTrabajador, on_delete=models.CASCADE)
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Postulacion'


class Recibo(models.Model):
    id = models.IntegerField(primary_key=True)
    monto = models.FloatField()
    fecha_de_pago = models.DateField()
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Recibo'


class UEmpresa(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True, default=1)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    class Meta:
        db_table = 'U_Empresa'