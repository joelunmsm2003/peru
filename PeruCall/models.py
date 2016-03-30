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


class Acciones(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    accion = models.IntegerField()
    origen = models.CharField(max_length=20)
    destino = models.CharField(max_length=20)
    canal = models.CharField(max_length=100)
    ip = models.CharField(max_length=16)
    id_agente = models.IntegerField()
    id_campania = models.IntegerField()
    fechahora = models.DateTimeField()
    id_base = models.IntegerField()
    flag = models.IntegerField()
    id_gestion = models.IntegerField()
    id_llamada = models.IntegerField()
    empresa = models.CharField(max_length=50)
    accountcode = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'acciones'


class Agendados(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    base = models.ForeignKey('Base', db_column='base', blank=True, null=True)
    agente = models.ForeignKey('Agentes', db_column='agente', blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agendados'


class Agentebase(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    agente = models.ForeignKey('Agentes', db_column='agente', blank=True, null=True)
    base = models.ForeignKey('Base', db_column='base', blank=True, null=True)
    tiniciogestion = models.DateTimeField(blank=True, null=True)
    tfingestion = models.DateTimeField(blank=True, null=True)
    duracion = models.IntegerField(blank=True, null=True)
    comentario = models.TextField(blank=True)
    facuerdo = models.DateTimeField(blank=True, null=True)
    macuerdo = models.IntegerField(blank=True, null=True)
    status = models.ForeignKey('Estado', db_column='status', blank=True, null=True)
    tiniciollamada = models.DateTimeField(blank=True, null=True)
    tfinllamada = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agentebase'


class Agentecalificacion(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    pregunta = models.ForeignKey('PregExam', db_column='pregunta', blank=True, null=True)
    nota = models.ForeignKey('Nota', db_column='nota', blank=True, null=True)
    agente = models.ForeignKey('Agentes', db_column='agente', blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True)
    calificacion = models.IntegerField(blank=True, null=True)
    item = models.IntegerField(blank=True, null=True)
    atributo = models.ForeignKey('Atributo', db_column='atributo', blank=True, null=True)
    criterio = models.ForeignKey('Criterios', db_column='criterio', blank=True, null=True)
    categoria = models.ForeignKey('Categoria', db_column='categoria', blank=True, null=True)
    campania = models.ForeignKey('Campania', db_column='campania', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agentecalificacion'


class Agentes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    anexo = models.IntegerField(blank=True, null=True)
    fono = models.IntegerField(blank=True, null=True)
    tiempo = models.DateTimeField(blank=True, null=True)
    destino = models.IntegerField()
    duracion = models.TimeField()
    atendidas = models.IntegerField(blank=True, null=True)
    contactadas = models.IntegerField(blank=True, null=True)
    estado = models.ForeignKey('Estado', db_column='estado', blank=True, null=True)
    est_ag_predictivo = models.IntegerField()
    canal = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey('AuthUser', db_column='user', blank=True, null=True)
    supervisor = models.ForeignKey('Supervisor', db_column='supervisor', blank=True, null=True)
    disponible = models.IntegerField(blank=True, null=True)
    tiniciogestion = models.DateTimeField(blank=True, null=True)
    tfingestion = models.DateTimeField(blank=True, null=True)
    tiniciollamada = models.DateTimeField(blank=True, null=True)
    tfinllamada = models.DateTimeField(blank=True, null=True)
    tinicioespera = models.DateTimeField(blank=True, null=True)
    tfinespera = models.DateTimeField(blank=True, null=True)
    tiniciotipeo = models.DateTimeField(blank=True, null=True)
    wordstipeo = models.IntegerField(blank=True, null=True)

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


class AjxProAcd(models.Model):
    id_ori_acd = models.IntegerField(primary_key=True)
    did_campana = models.CharField(db_column='DID_Campana', max_length=45)  # Field name made lowercase.
    numero_llamado = models.CharField(db_column='Numero_Llamado', max_length=45)  # Field name made lowercase.
    numero_entrante = models.CharField(db_column='Numero_Entrante', max_length=45)  # Field name made lowercase.
    channel_entrante = models.CharField(db_column='Channel_Entrante', max_length=50)  # Field name made lowercase.
    tiempo = models.CharField(db_column='Tiempo', max_length=15)  # Field name made lowercase.
    flag = models.IntegerField()
    uniqueid = models.CharField(max_length=30)
    fin = models.IntegerField()
    age_nombre = models.CharField(max_length=100, blank=True)
    tie_ing = models.DateTimeField()
    tie_acd = models.DateTimeField()
    tie_tra = models.DateTimeField()
    tie_con = models.DateTimeField()
    tie_fin = models.DateTimeField()
    tie_acw = models.DateTimeField()
    id_ori_campana = models.IntegerField()
    sql = models.IntegerField()
    codhu = models.IntegerField(db_column='CodHU')  # Field name made lowercase.
    bill = models.IntegerField()
    asterisk = models.IntegerField()
    audio = models.CharField(max_length=100)
    valorllamada = models.CharField(max_length=200)
    id_ori_usuario = models.IntegerField()
    llam_estado = models.IntegerField()
    anexo = models.IntegerField()
    duration = models.IntegerField()
    espera = models.IntegerField()
    pais = models.CharField(max_length=10)
    g_id1 = models.CharField(max_length=100)
    g_id2 = models.CharField(max_length=100)
    g_id3 = models.CharField(max_length=100)
    g_id4 = models.CharField(max_length=100)
    g_id5 = models.CharField(max_length=100)
    g_id6 = models.CharField(max_length=100)
    g_id7 = models.CharField(max_length=100)
    g_id8 = models.CharField(max_length=100)
    g_id9 = models.CharField(max_length=100)
    g_id10 = models.CharField(max_length=100)
    accountcode = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ajx_pro_acd'


class AjxProBas(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ti01 = models.IntegerField()
    ti02 = models.IntegerField()
    ti03 = models.IntegerField()
    ti04 = models.IntegerField()
    ti05 = models.IntegerField()
    ti06 = models.IntegerField()
    ti07 = models.IntegerField()
    ti08 = models.IntegerField()
    ti09 = models.IntegerField()
    ti10 = models.IntegerField()
    bi01 = models.IntegerField()
    bi02 = models.IntegerField()
    bi03 = models.IntegerField()
    bi04 = models.IntegerField()
    bi05 = models.IntegerField()
    bi06 = models.IntegerField()
    bi07 = models.IntegerField()
    bi08 = models.IntegerField()
    bi09 = models.IntegerField()
    bi10 = models.IntegerField()
    ts01 = models.CharField(max_length=100)
    ts02 = models.CharField(max_length=100)
    ts03 = models.CharField(max_length=100)
    ts04 = models.CharField(max_length=100)
    ts05 = models.CharField(max_length=100)
    ts06 = models.CharField(max_length=100)
    ts07 = models.CharField(max_length=100)
    ts08 = models.CharField(max_length=100)
    ts09 = models.CharField(max_length=100)
    ts10 = models.CharField(max_length=100)
    bs01 = models.CharField(max_length=500)
    bs02 = models.CharField(max_length=500)
    bs03 = models.CharField(max_length=500)
    bs04 = models.CharField(max_length=500)
    bs05 = models.CharField(max_length=500)
    bs06 = models.CharField(max_length=500)
    bs07 = models.CharField(max_length=500)
    bs08 = models.CharField(max_length=500)
    bs09 = models.CharField(max_length=500)
    bs10 = models.CharField(max_length=500)
    dt01 = models.DateTimeField()
    dt02 = models.DateTimeField()
    dt03 = models.DateTimeField()
    dt04 = models.DateTimeField()
    dt05 = models.DateTimeField()
    dt06 = models.DateTimeField()
    dt07 = models.DateTimeField()
    dt08 = models.DateTimeField()
    dt09 = models.DateTimeField()
    dt10 = models.DateTimeField()
    g_id1 = models.CharField(max_length=100)
    g_id2 = models.CharField(max_length=100)
    g_id3 = models.CharField(max_length=100)
    g_id4 = models.CharField(max_length=100)
    g_id5 = models.CharField(max_length=100)
    g_id6 = models.CharField(max_length=100)
    g_id7 = models.CharField(max_length=100)
    g_id8 = models.CharField(max_length=100)
    g_id9 = models.CharField(max_length=100)
    g_id10 = models.CharField(max_length=100)
    g_id11 = models.CharField(max_length=200)
    g_id12 = models.CharField(max_length=200)
    g_id13 = models.CharField(max_length=200)
    g_id14 = models.CharField(max_length=200)
    g_id15 = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'ajx_pro_bas'


class AjxProLla(models.Model):
    id_ori_llamadas = models.IntegerField(primary_key=True)
    age_ip = models.CharField(max_length=20, blank=True)
    age_codigo = models.CharField(max_length=10, blank=True)
    cam_codigo = models.IntegerField(blank=True, null=True)
    llam_numero = models.CharField(max_length=20, blank=True)
    llam_estado = models.IntegerField(blank=True, null=True)
    llam_flag = models.IntegerField(blank=True, null=True)
    llam_uniqueid = models.CharField(max_length=45, blank=True)
    tipo = models.IntegerField(blank=True, null=True)
    f_origen = models.DateTimeField()
    canal1 = models.CharField(max_length=50, blank=True)
    canal2 = models.CharField(max_length=50, blank=True)
    flagfin = models.IntegerField(db_column='flagFIN', blank=True, null=True)  # Field name made lowercase.
    v_tring = models.IntegerField(blank=True, null=True)
    v_retry = models.IntegerField(blank=True, null=True)
    ring = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    bill = models.IntegerField(blank=True, null=True)
    tregistro = models.IntegerField()
    gestion_editid1 = models.CharField(max_length=100, blank=True)
    gestion_editid2 = models.CharField(max_length=100, blank=True)
    gestion_editid3 = models.CharField(max_length=100, blank=True)
    f_llam_fin = models.DateTimeField()
    f_llam_discador = models.DateTimeField()
    f_llam_resuelve = models.DateTimeField()
    id_ori_campana = models.IntegerField()
    f_fingestion = models.DateTimeField()
    id_cliente = models.IntegerField(db_column='ID_Cliente')  # Field name made lowercase.
    coderr = models.IntegerField(db_column='CodErr')  # Field name made lowercase.
    audio = models.CharField(max_length=200)
    audio2 = models.CharField(max_length=200)
    sql = models.IntegerField()
    gestion_editid4 = models.CharField(max_length=100)
    gestion_editid5 = models.CharField(max_length=100)
    gestion_editid6 = models.CharField(max_length=100)
    gestion_editid7 = models.CharField(max_length=100)
    gestion_editid8 = models.CharField(max_length=100)
    gestion_editid9 = models.CharField(max_length=100)
    gestion_editid10 = models.CharField(max_length=100)
    gestion_editid11 = models.CharField(max_length=100)
    id_ori_seg_cola = models.IntegerField()
    age_nombre = models.CharField(max_length=100)
    anexo = models.IntegerField()
    espera = models.IntegerField()
    troncal = models.CharField(max_length=50)
    timbrado1 = models.IntegerField()
    timbrado2 = models.IntegerField()
    prefijo = models.CharField(max_length=20)
    grabacion = models.IntegerField()
    in_id = models.IntegerField(db_column='IN_ID')  # Field name made lowercase.
    v_tipbusc = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ajx_pro_lla'


class Atributo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'atributo'


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
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField(blank=True, null=True)
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=75, blank=True)
    is_staff = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    date_joined = models.DateTimeField(blank=True, null=True)
    empresa = models.ForeignKey('Empresa', db_column='empresa', blank=True, null=True)
    nivel = models.ForeignKey('Nivel', db_column='nivel')
    telefono = models.IntegerField(blank=True, null=True)
    anexo = models.IntegerField(blank=True, null=True)

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
    telefono = models.CharField(max_length=100, blank=True)
    orden = models.CharField(max_length=100, blank=True)
    cliente = models.CharField(max_length=100, blank=True)
    id_cliente = models.CharField(max_length=100, blank=True)
    status_a = models.CharField(max_length=100, blank=True)
    status_b = models.CharField(max_length=100, blank=True)
    status_c = models.CharField(max_length=100, blank=True)
    status_d = models.CharField(max_length=100, blank=True)
    status_e = models.CharField(max_length=100, blank=True)
    status_f = models.CharField(max_length=100, blank=True)
    status_g = models.CharField(max_length=100, blank=True)
    status_h = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=100, blank=True)
    campania = models.ForeignKey('Campania', db_column='campania', blank=True, null=True)
    resultado = models.ForeignKey('Resultado', db_column='resultado', blank=True, null=True)
    telefonomarcado2 = models.IntegerField(db_column='TelefonoMarcado2', blank=True, null=True)  # Field name made lowercase.
    proflag = models.IntegerField(db_column='ProFlag')  # Field name made lowercase.
    proestado = models.IntegerField(db_column='ProEstado')  # Field name made lowercase.
    filtrohdec = models.IntegerField(db_column='FiltroHdeC')  # Field name made lowercase.
    agente = models.ForeignKey(Agentes, db_column='agente', blank=True, null=True)
    duracion = models.IntegerField(blank=True, null=True)
    audio = models.CharField(max_length=120, blank=True)
    detalle = models.CharField(max_length=100, blank=True)
    monto = models.CharField(max_length=100, blank=True)
    fecha = models.DateTimeField(blank=True, null=True)
    tiniciogestion = models.DateTimeField(blank=True, null=True)
    tfingestion = models.DateTimeField(blank=True, null=True)
    tiniciollamada = models.DateTimeField(blank=True, null=True)
    tfinllamada = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base'


class Calificacion(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    preg_exam = models.ForeignKey('PregExam', db_column='preg_exam')
    agente = models.ForeignKey(Agentes, db_column='agente')
    campania = models.ForeignKey('Campania', db_column='campania')
    empresa = models.ForeignKey('Empresa', db_column='empresa', blank=True, null=True)
    respuesta = models.CharField(max_length=1000, blank=True)
    llamada = models.ForeignKey(AjxProLla, db_column='llamada')

    class Meta:
        managed = False
        db_table = 'calificacion'


class Campania(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fecha_cargada = models.DateTimeField(db_column='fecha cargada', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    usuario = models.ForeignKey(AuthUser, db_column='usuario', blank=True, null=True)
    estado = models.TextField(blank=True)
    nombre = models.CharField(max_length=100, blank=True)
    tipo = models.IntegerField(blank=True, null=True)
    discado = models.IntegerField(blank=True, null=True)
    factor = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    prefijo = models.IntegerField(blank=True, null=True)
    troncal = models.IntegerField(blank=True, null=True)
    timbrado1 = models.IntegerField(blank=True, null=True)
    timbrado2 = models.IntegerField(blank=True, null=True)
    grabacion = models.IntegerField(blank=True, null=True)
    t1 = models.IntegerField(blank=True, null=True)
    t2 = models.IntegerField(blank=True, null=True)
    t3 = models.IntegerField(blank=True, null=True)
    o_error_cnt = models.IntegerField(blank=True, null=True)
    o_nocontesto_cnt = models.IntegerField(blank=True, null=True)
    canales = models.IntegerField(blank=True, null=True)
    timbrados = models.IntegerField(blank=True, null=True)
    htinicio = models.TimeField(blank=True, null=True)
    htfin = models.TimeField(blank=True, null=True)
    mxllamada = models.IntegerField(blank=True, null=True)
    llamadaxhora = models.IntegerField(blank=True, null=True)
    hombreobjetivo = models.IntegerField(blank=True, null=True)
    archivo = models.CharField(max_length=100, blank=True)
    supervisor = models.ForeignKey('Supervisor', db_column='supervisor', blank=True, null=True)
    cartera = models.ForeignKey('Cartera', db_column='cartera', blank=True, null=True)
    tgestion = models.IntegerField(blank=True, null=True)

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
    privilegio = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carteraempresa'


class Categoria(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'categoria'


class Criterios(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'criterios'


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
    mascaras = models.ForeignKey('Mascara', db_column='mascaras', blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=100, blank=True)
    licencias_adi = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresa'


class Estado(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=100)
    flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado'


class Examen(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'examen'


class Filtro(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    campania = models.ForeignKey(Campania, db_column='campania', blank=True, null=True)
    ciudad = models.CharField(max_length=1000, blank=True)
    segmento = models.CharField(max_length=1000, blank=True)
    grupo = models.CharField(max_length=1000, blank=True)
    resultado = models.CharField(max_length=1000, blank=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filtro'


class Header(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    campania = models.ForeignKey(Campania, db_column='campania', blank=True, null=True)
    statusa = models.CharField(max_length=100, blank=True)
    statusb = models.CharField(max_length=100, blank=True)
    statusc = models.CharField(max_length=100, blank=True)
    statusd = models.CharField(max_length=100, blank=True)
    statuse = models.CharField(max_length=100, blank=True)
    statusf = models.CharField(max_length=100, blank=True)
    statusg = models.CharField(max_length=100, blank=True)
    statush = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'header'


class LicenciasTmp(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    lic_tmp = models.IntegerField(blank=True, null=True)
    finicio = models.DateTimeField(blank=True, null=True)
    ffin = models.DateTimeField(blank=True, null=True)
    empresa = models.ForeignKey(Empresa, db_column='empresa', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'licencias_tmp'


class Mascara(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    tipo = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'mascara'


class Monitorserver(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    d_uso = models.CharField(max_length=100, blank=True)
    d_disponible = models.CharField(max_length=100, blank=True)
    m_total = models.CharField(max_length=100, blank=True)
    m_usada = models.CharField(max_length=100, blank=True)
    s_total = models.CharField(max_length=100, blank=True)
    s_usada = models.CharField(max_length=100, blank=True)
    cpu = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monitorserver'


class Nivel(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'nivel'


class Nota(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    tipo = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'nota'


class PregExam(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    pregunta = models.CharField(max_length=100, blank=True)
    examen = models.ForeignKey(Examen, db_column='examen')
    valor = models.FloatField()

    class Meta:
        managed = False
        db_table = 'preg_exam'


class Resultado(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100, blank=True)
    codigo = models.CharField(max_length=100, blank=True)
    tipo = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'resultado'


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
