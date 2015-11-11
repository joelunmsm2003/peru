# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Agentes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    anexo = models.IntegerField(blank=True, null=True)
    fono = models.IntegerField(blank=True, null=True)
    tiempo = models.TimeField(blank=True, null=True)
    atendidas = models.IntegerField(blank=True, null=True)
    contactadas = models.IntegerField(blank=True, null=True)
    estado = models.ForeignKey('Estado', db_column='estado', blank=True, null=True)
    user = models.ForeignKey('AuthUser', db_column='user', blank=True, null=True)
    supervisor = models.IntegerField(blank=True, null=True)
    disponible = models.IntegerField(blank=True, null=True)
    calificacion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agentes'


class Agentescampanias(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    agente = models.ForeignKey(Agentes, db_column='agente')
    campania = models.ForeignKey('Campania', db_column='campania')

    class Meta:
        managed = False
        db_table = 'agentescampanias'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    empresa = models.ForeignKey('Empresa', db_column='empresa')
    nivel = models.ForeignKey('Nivel', db_column='nivel')

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class Base(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    telefono = models.IntegerField(blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)
    cliente = models.CharField(max_length=100, blank=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    producto = models.CharField(max_length=100, blank=True)
    tarjeta = models.CharField(max_length=100, blank=True)
    deuda = models.CharField(max_length=100, blank=True)
    descuento = models.CharField(max_length=100, blank=True)
    diasmora = models.IntegerField(blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True)
    segmento = models.CharField(max_length=100, blank=True)
    grupo = models.CharField(max_length=100, blank=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base'


class Calificacion(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    tipo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'calificacion'


class Campania(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fecha_cargada = models.DateTimeField(db_column='fecha cargada')  # Field renamed to remove unsuitable characters.
    usuario = models.ForeignKey(AuthUser, db_column='usuario')
    estado = models.TextField()
    nombre = models.CharField(max_length=100)
    troncal = models.IntegerField()
    canales = models.IntegerField()
    timbrados = models.IntegerField()
    htinicio = models.TimeField()
    htfin = models.TimeField()
    mxllamada = models.IntegerField()
    llamadaxhora = models.IntegerField()
    hombreobjetivo = models.IntegerField()
    archivo = models.CharField(max_length=100)
    supervisor = models.ForeignKey('Supervisor', db_column='supervisor', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campania'


class Cartera(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cartera'


class Carteraempresa(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    cartera = models.ForeignKey(Cartera, db_column='cartera')
    empresa = models.ForeignKey('Empresa', db_column='empresa')

    class Meta:
        managed = False
        db_table = 'carteraempresa'


class Ciudad(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'ciudad'


class Data(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    author = models.CharField(max_length=11)
    text = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'data'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empresa(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    licencias = models.CharField(max_length=100)
    mascaras = models.CharField(max_length=100)
    telefono = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'empresa'


class Estado(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'estado'


class Grupo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'grupo'


class Nivel(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'nivel'


class Segmento(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'segmento'


class Supervisor(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, db_column='user')

    class Meta:
        managed = False
        db_table = 'supervisor'


class Supervisorcartera(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    cartera = models.ForeignKey(Cartera, db_column='cartera')
    supervisor = models.ForeignKey(Supervisor, db_column='supervisor')

    class Meta:
        managed = False
        db_table = 'supervisorcartera'


class Troncales(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'troncales'


class Troncalesagentes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    empresa = models.ForeignKey(Empresa, db_column='empresa')
    troncal = models.ForeignKey(Troncales, db_column='troncal')

    class Meta:
        managed = False
        db_table = 'troncalesagentes'
