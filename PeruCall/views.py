from django.shortcuts import *
from django.template import RequestContext
from django.contrib.auth import *
from django.contrib.auth.models import Group, User
from django.contrib.sessions.models import Session
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.core.urlresolvers import reverse
from django.db.models import Max,Count
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from PeruCall.models import *
from django.http import HttpRequest

from django.db import transaction
from django.contrib.auth.hashers import *
from django.core.mail import send_mail
from django.db import connection
from django.utils.six.moves import range
from django.http import StreamingHttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_exempt
from ws4redis.redis_store import RedisMessage
from ws4redis.publisher import RedisPublisher
from django.db.models import Count, Min, Sum, Avg
import collections
import random
import time
import xlrd
import json 
import csv
import simplejson
import xlwt
import requests
import os
import mad

from datetime import datetime,date
from django.contrib.auth import authenticate
from django.db.models.signals import pre_save
from django.contrib.auth.signals import user_logged_in

from django.dispatch import receiver
from ws4redis.publisher import RedisPublisher
from ws4redis.redis_store import RedisMessage
from datetime import datetime,timedelta



def audio(request):
    return render(request, 'audio.html')

@login_required(login_url="/ingresar")
def audios(request):

    id = request.user.id

    nivel = AuthUser.objects.get(id=id).nivel.id

    if nivel == 4:

	empresas = Empresa.objects.all().values('id','nombre','licencias','mascaras__tipo','telefono','contacto','mail','url').order_by('-id')

    else:

	empresa = AuthUser.objects.get(id=id).empresa.id

	empresas = Empresa.objects.filter(id=empresa).values('id','nombre','licencias','mascaras__tipo','telefono','contacto','mail','url').order_by('-id')

    data = json.dumps(ValuesQuerySetToDict(empresas))

    if request.method == 'POST':

	tipo = json.loads(request.body)['add']

	data = json.loads(request.body)['dato']

	if tipo == "New":

	    nombre = data['nombre']
	    contacto = data['contacto']
	    mail = data['mail']
	    licencias = data['licencias']
	    if data['mascara']==2:
		url =data['url']
	    else:
		url=""
	    
	    telefono = data['telefono']
	    mascara = data['mascara']

    

	    Empresa(mascaras_id=mascara,nombre=nombre,contacto=contacto,mail=mail,licencias=licencias,telefono=telefono,url=url).save()

	    return HttpResponse(nombre, content_type="application/json")


	if tipo=="Edit":

	    id= data['id']
	    empresa = Empresa.objects.get(id=id)
	    empresa.nombre =data['nombre']
	    empresa.contacto =data['contacto']
	    empresa.mail =data['mail']
	    empresa.licencias =data['licencias']
	    empresa.mascaras_id =data['mascaras__tipo']
	    if data['mascaras__tipo']==2:
		empresa.url =data['url']

	    

	    empresa.telefono =data['telefono']
	    empresa.save()


	if tipo=="Eliminar":

	    id= data['id']

    


	return HttpResponse(data['nombre'], content_type="application/json")


    return HttpResponse(data, content_type="application/json")



@login_required(login_url="/ingresar")
def changepass(request):

	id = request.user.id

	if request.method == 'POST':

		data = json.loads(request.body)['dato']

		password = data['password']
		id_user = data['id']

		u = User.objects.get(id=id_user)

		data = u.first_name

		u.set_password(password)

		u.save()

		return HttpResponse(data, content_type="application/json")

@csrf_exempt
def desconectados(request):

	os.system('rsync -a /var/spool/asterisk/ /var/www/html/')

	agentes = Estadocambio.objects.all().values('user','user__first_name').annotate(fecha=Max('fecha'))

	t = datetime.now()

	now = datetime.now()

	d = []

	for i in range(len(agentes)):

		t_estado = int((t-agentes[i]['fecha']).total_seconds()/60)

		if t_estado > 15:

			

			if Agentes.objects.filter(user_id=agentes[i]['user']):

				d.insert(i,str(agentes[i]['user__first_name'])+ '-' +str(t_estado))

				agente = Agentes.objects.get(user_id=agentes[i]['user'])
				agente.estado_id= 1
				agente.save()



	data = simplejson.dumps(d)

	return HttpResponse(data, content_type="application/json")


@receiver(user_logged_in)
def my_handler(sender,**kwargs):
	x = kwargs['request'].POST



def ingresar(request):

	if request.user.is_authenticated():

		
		id =request.user.id
		nivel = AuthUser.objects.get(id=id).nivel.id

		if nivel == 1:
			return HttpResponseRedirect("/campania")
		if nivel == 2:
			return HttpResponseRedirect("/campania")
		if nivel == 3:
			
			id_agente = Agentes.objects.get(user_id=id).id
			a = Agentes.objects.get(id=id_agente)
			a.est_ag_predictivo = 0
			a.save()

			return HttpResponseRedirect("/teleoperador/"+str(id_agente))
		if nivel == 4:
			return HttpResponseRedirect("/usuario")
		if nivel == 5:
			return HttpResponseRedirect("/campania")
			

		return HttpResponseRedirect("/empresa")

	else:

		if request.method == 'POST':

			user = request.POST['user']
			
			psw = request.POST['password']

			user = authenticate(username=user, password=psw)

		
			if user is not None:

				if user.is_active:

					login(request, user)
		
					nivel = AuthUser.objects.get(username=user).nivel.id

					Estadocambio(user_id=request.user.id,estado_id=2).save()

					empresa = AuthUser.objects.get(id=request.user.id).empresa.id

					nameempresa = AuthUser.objects.get(id=request.user.id).empresa.nombre

					licencias = Empresa.objects.get(id=empresa).licencias

					nl = 0

					ageactivos = Agentes.objects.filter(user__empresa_id=empresa)

					for a in ageactivos:

						

						if a.estado_id > 1:

							nl =nl+1
				
					

					if int(nl) > int(licencias):

						

						f = open('/var/www/html/licencias.txt', 'a')
						f.write('Numero de licencias excedido ' +str(nameempresa)+'-'+str(nl)+'-'+str(licencias)+'\n')
						f.close()

						send_mail('Licencias','La empresa ' +str(nameempresa)+' requiere mas licencias, Numero de licencias actual : '+licencias,'andyjo@xiencias.org', ['ginorel@gmail.com','panelcontrol7@gmail.com','panelcontrol6@gmail.com'], fail_silently=False)

					if nivel == 1:

						return HttpResponseRedirect("/campania")

					if nivel == 2:

						return HttpResponseRedirect("/campania")

					if nivel == 3:

						agente= Agentes.objects.get(user_id=user)
						id_agente = agente.id
						agente.estado_id='2'
						agente.wordstipeo = 0
						agente.tinicioespera = datetime.now()-timedelta(hours=5)
						agente.save()

						
						if int(nl) > int(licencias):

							data = simplejson.dumps('No tiene Licencias')

							return HttpResponse(data, content_type="application/json")	
						
						else:

							return HttpResponseRedirect("/teleoperador/"+str(id_agente))

					if nivel == 4:



						return HttpResponseRedirect("/empresa")

					if nivel == 5:

						return HttpResponseRedirect("/campania")

			else:

				return HttpResponseRedirect("/ingresar")
		
		else:

			return render(request, 'signin.html',{})


@login_required(login_url="/ingresar")
def home(request):
	return render(request, 'index.html',{})

@login_required(login_url="/ingresar")
def menu(request):
	return render(request, 'menu.html',{})


#####Asterisk y APP Monitoring#####
@csrf_exempt
def astapp(request):



	activeCall= str(request.POST['activeCall'])
	dsk_use= str(request.POST['dsk_use']).replace("G", "")
	dsk_tot= str(request.POST['dsk_tot']).replace("G", "")
	total_mem= str(request.POST['total_mem'])
	use_mem= str(request.POST['use_mem'])
	total_swap= str(request.POST['total_swap'])
	use_swap= str(request.POST['use_swap'])
	CPU= str(request.POST['CPU'])
	astCpuUse= str(request.POST['astCpuUse'])
	astMemUse= str(request.POST['astMemUse'])
	pytCpuUse= str(request.POST['pytCpuUse'])
	pytMemUse= str(request.POST['pytMemUse'])
	sqlCpuUse= str(request.POST['sqlCpuUse'])
	sqlMemUse= str(request.POST['sqlMemUse'])

	date =datetime.now()


	Monitorserver(activecall=activeCall,dsk_use=dsk_use,dsk_tot=dsk_tot,total_mem=total_mem,use_mem=use_mem,total_swap=total_swap,use_swap=use_swap,cpu=CPU,astcpuuse=astCpuUse,astmemuse=astMemUse,pytcpuuse=pytCpuUse,pytmemuse=pytMemUse,sqlcpuuse=sqlCpuUse,sqlmemuse=sqlMemUse).save()

	data = {'activecall':activeCall,'dsk_use':dsk_use,'dsk_tot':dsk_tot,'total_mem':total_mem,'m_usada':use_mem,'dsk_use':dsk_use,'dsk_tot':dsk_tot,'total_mem':total_mem,'total_swap':total_swap,'use_swap':use_swap,'cpu':CPU,'astCpuUse':astCpuUse,'astMemUse':astMemUse,'pytCpuUse':pytCpuUse,'pytMemUse':pytMemUse,'sqlCpuUse':sqlCpuUse,'sqlMemUse':sqlMemUse}

	data =json.dumps(data)

	redis_publisher = RedisPublisher(facility='foobar', users=['manager'])

	message = RedisMessage(data)

	redis_publisher.publish_message(message)

	return HttpResponse(data, content_type="application/json")




@login_required(login_url="/ingresar")
def teleoperador(request,id_agente):

	id=request.user.id

	base = Base.objects.filter(agente_id=id_agente,status=1).order_by('-id').values('id','telefono','orden','cliente','id_cliente','status_a','status_b','status_c','status_d','status_e','status_f','status_g','status_h','status','campania__nombre','resultado__name','resultado','campania__mxllamada','campania__mxllamada','campania__hombreobjetivo','campania__cartera__nombre')



	dni = ''

	if base:

		dni = base[0]['id_cliente']

	id_user = Agentes.objects.get(id=id_agente).user.id

	url = AuthUser.objects.get(id=id).empresa.url

	if id==id_user:

		return render(request, 'screenagent.html',{'url':url,'dni':dni})

	else:

		return HttpResponseRedirect("/")


@login_required(login_url="/ingresar")
def game(request):

	send_mail('Licencias','La empresa ' +str('nameempresa')+' requiere mas licencias, Numero de licencias actual :'+'licencias','andyjo@xiencias.org', ['joelunmsm@gmail.com'], fail_silently=False)

	return render(request, 'game.html',{})
	

@login_required(login_url="/ingresar")
def empresa(request):

	return render(request, 'empresa.html',{})

@login_required(login_url="/ingresar")
def dashboard(request,agente,examen):

	return render(request, 'dashboard.html')

@login_required(login_url="/ingresar")
def campaniaresult(request,campania,examen):

	return render(request, 'campaniaresult.html')


@login_required(login_url="/ingresar")
def monitorcpu(request):

	return render(request, 'monitorcpu.html',{})


@login_required(login_url="/ingresar")
def examenes(request):

	base = Examen.objects.all().values('id','nombre')

	data_dict = ValuesQuerySetToDict(base)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@login_required(login_url="/ingresar")
def accionmonitor(request,sup,anexo):

	id = request.user.id

	nivel = AuthUser.objects.get(id=id).nivel.id

	if nivel == 5 :

		sup = AuthUser.objects.get(id=id).anexo

	cmd = ('curl "http://localhost:81/xien/PROC_MONITOR.php?sup=%s&anx=%s" &' %(sup, anexo))
	os.system(cmd)

	return HttpResponse(' Monitor Activado', content_type="application/json")



@login_required(login_url="/ingresar")
def accionsusurro(request,sup,anexo):

	id = request.user.id

	nivel = AuthUser.objects.get(id=id).nivel.id

	if nivel == 5 :

		sup = AuthUser.objects.get(id=id).anexo

	cmd = ('curl "http://localhost:81/xien/PROC_SUSURRO.php?sup=%s&anx=%s" & ' %(sup, anexo))
	os.system(cmd)

	return HttpResponse('Susurro Activado', content_type="application/json")



@login_required(login_url="/ingresar")
def passcampania(request,campania):

	c = Campania.objects.filter(id=campania).values('password')

	data_dict = ValuesQuerySetToDict(c)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@login_required(login_url="/ingresar")
def getaudios(request):

	if request.method == 'POST':

		data= json.loads(request.body)

		filtro = {}

		for i in data:

			if i == 'origen':
			
				filtro['anexo'] =  data['origen']

			if i == 'destino':

				filtro['llam_numero']  = data['destino']

			if i == 'campania':

				filtro['cam_codigo']  = data['campania']

			if i == 'fecha':

				filtro['f_origen__gte']  = data['fecha']

			if i == 'fechafin':

				filtro['f_origen__lte']  = data['fechafin']


		filtro['llam_estado'] = 4

		data = AjxProLla.objects.filter(**filtro).values('duration','id_ori_llamadas','anexo','llam_numero','cam_codigo','age_codigo','llam_estado').order_by('-id_ori_llamadas')

		fmt = '%Y-%m-%d %H:%M:%S %Z'

		for i in range(len(data)):

			

			data[i]['fecha'] = AjxProLla.objects.get(id_ori_llamadas=data[i]['id_ori_llamadas']).f_origen.strftime(fmt)


			if data[i]['age_codigo'] != "":

				data[i]['name'] = Agentes.objects.get(id=data[i]['age_codigo']).user.first_name





	data_dict = ValuesQuerySetToDict(data)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@login_required(login_url="/ingresar")
def pausarcampania(request,campania):

	filtros = Filtro.objects.filter(campania_id=campania)

	for f in filtros:

		f.status = 1
		f.save()

	return HttpResponse('campania stop', content_type="application/json")

@csrf_exempt
def matarochenta(request):

	os.system('sudo netstat -nlp | grep 80')

	os.system('sudo netstat -nlp | grep 80 > matarochenta.txt')

	file = open('matarochenta.txt', 'r')

	for line in file:

	   port = int(line.split('ESCUCHAR    ')[1].split('/')[0])

	   os.system('kill -9 '+str(port))

	return HttpResponse('Killed :)', content_type="application/json")


	

@login_required(login_url="/ingresar")
def activarcampania(request,campania):

	filtros = Filtro.objects.filter(campania_id=campania)

	for f in filtros:

		f.status = 0
		f.save()

	return HttpResponse('campania stop', content_type="application/json")



@login_required(login_url="/ingresar")
def infocampania(request,campania):

	c = Campania.objects.filter(id=campania).values('password','nombre','cartera__nombre','supervisor__user__empresa__nombre','supervisor__user__first_name','supervisor__user__empresa__mascaras')

	data_dict = ValuesQuerySetToDict(c)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@login_required(login_url="/ingresar")
def uploaduser(request):

	id = request.user.id

	empresa = AuthUser.objects.get(id=id).empresa.id




	filex = request.FILES['process_file']

	Excel(archivo=filex).save()

	id_excel = Excel.objects.all().values('id').order_by('-id')[0]['id']

	archivo = Excel.objects.get(id=id_excel).archivo

	ruta = '/var/www/html/'+str(archivo)

	book = xlrd.open_workbook(ruta)

	sh = book.sheet_by_index(0)

	u=[]

	for rx in range(sh.nrows):

	

		if rx > 0:

			u=[]

			for col in range(sh.ncols):

				x = str(sh.row(rx)[col]).replace('text:u','').replace('number:','').replace("'","").replace('.0','')
				
				u.append(x)

			
			email = u[0]
			password = u[1]
			nombre = u[2]
			telefono = u[3]
			anexo = u[4]
			nivel =u[5]
			supervisor = u[6]


			users = User.objects.all()

			e = 1

			ui=0

			for users in users:

				if email == users.username:

					ui = 1

			if ui == 0:

				user = User.objects.create_user(username=email,password=password)

				user.save()

				id_user = AuthUser.objects.all().values('id').order_by('-id')[0]['id']

				usuario = AuthUser.objects.get(id=id_user)
			
				usuario.empresa_id = int(empresa)
				usuario.nivel_id = int(nivel)
				usuario.first_name = nombre
				usuario.anexo=int(anexo)
				usuario.telefono = int(telefono)
				usuario.save()

				if usuario.nivel_id == 2: 

					Supervisor(user_id=id_user).save()

				if usuario.nivel_id == 3: # Usuario Agente

					s =supervisor.split('|')

					Agentes(user_id=id_user).save()

					agente =Agentes.objects.get(user=id_user)
					
					agente.atendidas = 0
					agente.contactadas =0
					agente.anexo = int(anexo)					
					agente.estado_id = 1
					agente.save()

					id_agente = Agentes.objects.all().values('id').order_by('-id')[0]['id']
					
					for i in s:

						id_sup = Supervisor.objects.get(user_id=i).id

						Agentesupervisor(agente_id=id_agente,supervisor_id=id_sup).save()

					

	
	return HttpResponseRedirect("/usuario")


@login_required(login_url="/ingresar")
def kpi(request,agente):

	today = datetime.now()

	user = Agentes.objects.get(id=agente).user.id

	fmt1 = '%Y-%m-%d'

	today =  today.strftime(fmt1)

	

	base = Estadocambio.objects.filter(fecha__gte=today,user_id=user,estado_id=2).values('id','estado__nombre','user__first_name','user').order_by('id')[:1]

	
		
	fmt = '%H:%M'

	for i in range(len(base)):

		base[i]['fecha'] = Estadocambio.objects.get(id=base[i]['id']).fecha.strftime(fmt)

	

	horainicio = float(base[0]['fecha'].split(':')[0]) + float(base[0]['fecha'].split(':')[1])/60

	

	now = datetime.now()

	fmt2='%H:%M'

	now = now.strftime(fmt2)

	horafin = float(now.split(':')[0]) + float(now.split(':')[1])/60



	a = (horafin-horainicio)*80/100



	today1 = datetime.now()



	ajax = AjxProLla.objects.filter(age_codigo=agente).order_by('-id_ori_llamadas')



	t=0

	for i in ajax:

		if str(i.f_origen).split(" ")[0] == today:

			t = t + i.duration 
		#t = int(ajax.duration) + t

	
	b = float(t)/3600



	kpi =0

	if b>0:

		kpi = (b*100)/a




	#kpicolor='red'

	if kpi <= 65:
		kpicolor = 'rgb(239, 83, 80)'
		kpic = '#fff'
	if kpi>65 and kpi<=85:
		kpicolor = 'rgb(244, 242, 54)'
		kpic = '#284058'
	if kpi>85:
		kpicolor = 'rgb(136, 229, 66)'
		kpic = '#284058'

	kpi = str(format(kpi, '.2f'))

	data = {'kpicolor':kpicolor,'kpi':kpi,'kpic':kpic}
	data = simplejson.dumps(data)

	return HttpResponse(data, content_type="application/json")



@login_required(login_url="/ingresar")
def getexamen(request,examen):


	base = Examen.objects.filter(id=examen).values('id','nombre')

	data_dict = ValuesQuerySetToDict(base)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@login_required(login_url="/ingresar")
def getcamp(request,campania):

	data = Campania.objects.filter(id=campania).values('id','usuario','estado','nombre','cartera__nombre','supervisor__user__empresa__nombre')

	data_dict = ValuesQuerySetToDict(data)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@login_required(login_url="/ingresar")
def estllamada(request,campania):


	total = AjxProLla.objects.filter(cam_codigo=campania).count()

	barridos = AjxProLla.objects.filter(cam_codigo=campania,llam_estado=1).count()

	errados = AjxProLla.objects.filter(cam_codigo=campania,llam_estado=2).count()

	correctos = AjxProLla.objects.filter(cam_codigo=campania,llam_estado=4).count()

	porbarrer = total-barridos

	data = {'total':total,'barridos':barridos,'porbarrer':porbarrer,'errados':errados,'correctos':correctos}

	data = simplejson.dumps(data)



	return HttpResponse(data, content_type="application/json")


@login_required(login_url="/ingresar")
def enviar(request):


	if request.method == 'POST':

		msj= json.loads(request.body)['msj']

		user=json.loads(request.body)['username']

		

		redis_publisher = RedisPublisher(facility='foobar', users=[user])

		message = RedisMessage('Cali'+msj)

		redis_publisher.publish_message(message)


	return HttpResponse('data', content_type="application/json")

@csrf_exempt
def cpuestado(request):



	memoriausada= str(request.POST['memoriausada'])
	d_usado= str(request.POST['d_usado']).replace("G", "")
	d_disponible= str(request.POST['d_disponible']).replace("G", "")
	memoriatotal= str(request.POST['memoriatotal'])
	memoriausada= str(request.POST['memoriausada'])
	swaptotal= str(request.POST['swaptotal'])
	swapusada= str(request.POST['swapusada'])
	cpu= str(request.POST['cpu'])


	date =datetime.now()

	Monitorserver(d_uso=d_usado,d_disponible=d_disponible,m_total=memoriatotal,m_usada=memoriausada,s_total=swaptotal,s_usada=swapusada,cpu=cpu,date=date).save()

	data = {'memoriausada':memoriausada,'d_usado':d_usado,'d_disponible':d_disponible,'memoriatotal':memoriatotal,'memoriausada':memoriausada,'swaptotal':swaptotal,'swapusada':swapusada,'cpu':cpu}

	data =json.dumps(data)

	redis_publisher = RedisPublisher(facility='foobar', users=['manager'])

	message = RedisMessage(data)

	redis_publisher.publish_message(message)

	return HttpResponse(data, content_type="application/json")


@login_required(login_url="/ingresar")
def notificar(request):


	if request.method == 'POST':

		msj= json.loads(request.body)['msj']

		user=json.loads(request.body)['username']

		name = AuthUser.objects.get(id=request.user.id).first_name

		redis_publisher = RedisPublisher(facility='foobar', users=[user])

		msj = msj.encode('utf-8')

		message = RedisMessage('Noti'+name+ ' dice: '+msj)

		redis_publisher.publish_message(message)


	return HttpResponse('data', content_type="application/json")


@login_required(login_url="/")
def usuario(request):
	return render(request, 'usuario.html',{})

@login_required(login_url="/ingresar")
def campania(request):

	id = request.user.id

	nivel = AuthUser.objects.get(id=id).nivel.id
	empresa = AuthUser.objects.get(id=id).empresa.id

	troncales = Troncales.objects.all()

	if nivel == 1:

		supervisor = Supervisor.objects.all()
		cartera = Carteraempresa.objects.filter(empresa_id=empresa)


	if nivel == 2:

		supervisor = Supervisor.objects.filter(user=id)
		cartera = Supervisorcartera.objects.filter(supervisor__user__id=id)


	if nivel == 4:

		supervisor = Supervisor.objects.all()
		cartera = Cartera.objects.all()

	if nivel == 5:

		supervisor = Supervisor.objects.all()
		cartera = Carteraempresa.objects.filter(empresa_id=empresa)

	password = random.randint(0, 100005)
	
	return render(request, 'campania.html',{'supervisor':supervisor,'troncales':troncales,'cartera':cartera,'password':password})

@login_required(login_url="/ingresar")
def base(request):

	id = request.user.id

	nivel = AuthUser.objects.get(id=id).nivel.id
	empresa = AuthUser.objects.get(id=id).empresa.id

	if nivel == 1:

		base = Base.objects.filter(agente__user__empresa_id=empresa).values('id','telefono','orden','status','campania__nombre','resultado__name','agente__user__first_name','duracion')
		
	if nivel == 2:

		supervisor = Campania.objects.filter(supervisor__user__id=id)

		ca =[]

		for s in supervisor:

			ca.append(s.id)


		base = Base.objects.filter(pk__in=ca).values('id','telefono','orden','status','campania__nombre','resultado__name','agente__user__first_name','duracion')
		
	if nivel == 3:

		pass

	if nivel == 4:

		base = Base.objects.all().values('id','telefono','orden','status','campania__nombre','resultado__name','agente__user__first_name','duracion')
		
	
	data_dict = ValuesQuerySetToDict(base)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")




@login_required(login_url="/ingresar")
def filtros(request,id):
	campania = Campania.objects.get(id=id)
	return render(request, 'filtros.html',{'campania':campania})

@login_required(login_url="/ingresar")
def pregunta(request):

	return render(request, 'pregunta.html',{})

@login_required(login_url="/ingresar")
def cartera(request):
	
	return render(request, 'cartera.html',{})


@login_required(login_url="/ingresar")
def reportedetallado(request):
	
	return render(request, 'reportedetallado.html',{})


@login_required(login_url="/ingresar")
def reporteg(request,campania):
	
	return render(request, 'reporteg.html',{})

@login_required(login_url="/ingresar")
def licencia(request):
	
	return render(request, 'licencia.html',{})


@login_required(login_url="/ingresar")
def supervisorcartera(request,id_supervisor):
	
	return render(request, 'carterasupervisor.html',{})

@login_required(login_url="/ingresar")
def detallesupervisormant(request,user):
	
	return render(request, 'detallesupervisor.html',{})

@login_required(login_url="/ingresar")
def adminCampania(request,id_campania):
	campania = Campania.objects.get(id=id_campania)
	return render(request, 'admincampania.html',{'campania':campania})

@login_required(login_url="/ingresar")
def monitoreo(request,id):
	campania = Campania.objects.get(id=id)
	return render(request, 'monitoreo.html',{'campania':campania})

@login_required(login_url="/ingresar")
def reportes(request,id):
	campania = Campania.objects.get(id=id)
	return render(request, 'reportes.html',{'campania':campania})

@login_required(login_url="/ingresar")
def menu(request):
	
	return render(request, 'menu.html',{})


@login_required(login_url="/ingresar")
def agentes(request,id_campania):

	id = request.user.id

	ti =0

	tges = Campania.objects.get(id=id_campania).tgestion

	user = Agentescampanias.objects.filter(campania=id_campania).values('id','agente__wordstipeo','agente','agente__user__username','agente__user__first_name','agente__fono','agente__anexo','agente__atendidas','agente__contactadas','agente__estado','agente__estado__nombre','campania__supervisor__user__anexo').order_by('agente__user__first_name','agente__anexo','agente__estado__nombre')

	fmt = '%Y-%m-%d %H:%M:%S %Z'
	fmt1 = '%Y-%m-%d %H:%M:%S'
	fmt2='%H:%M:%S'

	for i in range(len(user)):

		agente = Agentes.objects.get(id=user[i]['agente'])

		L = str(AjxProLla.objects.filter(age_codigo=user[i]['agente']).values('id_ori_llamadas').order_by('-id_ori_llamadas')[:1])

		user[i]['idllamada'] = L.replace("[{","").replace("'","").replace("id_ori_llamadas:","").replace("L}]","").replace(" ","")

		user[i]['atendidas'] = AjxProLla.objects.filter(cam_codigo=id_campania,age_codigo=user[i]['agente'],llam_estado=4).count()

		user[i]['total'] =  AjxProLla.objects.filter(cam_codigo=id_campania,age_codigo=user[i]['agente']).count()

		if Base.objects.filter(status=1,agente_id=user[i]['agente']):

			user[i]['fono'] =  str(Base.objects.filter(status=1,agente_id=user[i]['agente']).values('telefono')[:1]).replace("[{'telefono':",'').replace('L}]','').replace("None}]",'').replace("u'",'').replace("'}]",'')

		if agente.estado.id == 2:

			ti = agente.tinicioespera

		if agente.estado.id == 3:

			ti = agente.tiniciollamada

		if agente.estado.id == 6:

			ti = agente.tiniciogestion

		if agente.estado.id == 5:

			ti = agente.tiniciopausa

		if agente.estado.id == 8:

			ti = agente.tiniciobreak

		if agente.estado.id == 9:

			ti = agente.tinicioservicio

		if agente.estado.id > 1:

			

			ti= str(ti)[0:19]
			ti = datetime.strptime(ti,fmt1)
			tf= str(datetime.now())[0:19]
			tf = datetime.strptime(tf,fmt1)

			user[i]['tgestion'] = str(tf-ti)
	
			sec = str(tf-ti).split(':')
			
			user[i]['secgestion'] = int(sec[2])*2

			if int(sec[1]) > 0  :

				sec[2] = 165
				user[i]['secgestion'] = 180

			if int(sec[2]) > 0 and int(sec[2])< 30:
				user[i]['color'] = '#81C784'
			if int(sec[2]) > 30 and int(sec[2])< 55:
				user[i]['color'] = '#2196F3'
			if int(sec[2]) > 55 :
				user[i]['color'] = '#EF5350'

		'''

		if Agentescampanias.objects.filter(id=user[i]['id']).agente.tiempo:

			user[i]['agente__tiempo'] = Agentescampanias.objects.get(id=user[i]['id']).agente.tiempo.strftime(fmt)
		
		'''

		if user[i]['agente__atendidas'] > 0:

			user[i]['performance'] =  (user[i]['agente__contactadas']*100/user[i]['agente__atendidas'])

		else:

			user[i]['performance'] = 0

	data_dict = ValuesQuerySetToDict(user)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@login_required(login_url="/ingresar")
def agentescalifica(request,agente):

		data = Calificacion.objects.filter(agente_id=agente).values('id','preg_exam__pregunta').order_by('-id')

		data_dict = ValuesQuerySetToDict(data)

		data = simplejson.dumps(data_dict)

		return HttpResponse(data, content_type="application/json")

@login_required(login_url="/ingresar")
def getestado(request,agente):

		data = Agentes.objects.get(id=agente).estado.id

		return HttpResponse(data, content_type="application/json")

@login_required(login_url="/ingresar")
def agentesall(request,empresa):

		data = Agentes.objects.filter(user__empresa_id=empresa).values('id','user__first_name','user__empresa__nombre').order_by('-id')

		data_dict = ValuesQuerySetToDict(data)

		data = simplejson.dumps(data_dict)

		return HttpResponse(data, content_type="application/json")


@login_required(login_url="/ingresar")
def resultadoagente(request,agente,examen):

	
		preg = PregExam.objects.filter(examen_id=examen).values('id','examen__nombre','pregunta')

		for i in range(len(preg)):

			

			preg[i]['respsi']=Calificacion.objects.filter(agente_id=agente,preg_exam__examen=examen,preg_exam_id=preg[i]['id'],respuesta='Si').count()
			preg[i]['respno']=Calificacion.objects.filter(agente_id=agente,preg_exam__examen=examen,preg_exam_id=preg[i]['id'],respuesta='No').count()

		
		data_dict = ValuesQuerySetToDict(preg)

		data = simplejson.dumps(data_dict)

		return HttpResponse(data, content_type="application/json")


@login_required(login_url="/ingresar")
def resultadocampania(request,campania,examen):

	
		preg = PregExam.objects.filter(examen_id=examen).values('id','examen__nombre','pregunta')

		for i in range(len(preg)):

			
			preg[i]['respsi']=Calificacion.objects.filter(campania_id=campania,preg_exam__examen=examen,preg_exam_id=preg[i]['id'],respuesta='Si').count()
			preg[i]['respno']=Calificacion.objects.filter(campania_id=campania,preg_exam__examen=examen,preg_exam_id=preg[i]['id'],respuesta='No').count()

		
		data_dict = ValuesQuerySetToDict(preg)

		data = simplejson.dumps(data_dict)

		return HttpResponse(data, content_type="application/json")


@login_required(login_url="/ingresar")
def botonexterno(request):

		if request.method == 'POST':

			data = json.loads(request.body)

			#{u'agente': u'14', u'done': False, u'boton': 18, u'cliente': {u'status': u'1', u'orden': None, u'resultado': 5, u'status_d': None, u'campania__nombre': u'Pastillas LSD', u'status_h': u'SCORE C', u'status_g': u'NUEVO', u'status_f': u'LIMA', u'id_cliente': None, u'resultado__name': u'Acuerdo con fecha de pago', u'status_c': None, u'status_b': None, u'status_a': None, u'id': 2, u'status_e': None, u'tiniciollamada': u'2016-04-13 23:34:34 UTC', u'telefono': None, u'cliente': None}}

			resultado = data['boton']
			base = data['cliente']['id']
			agente = data['agente']

			rbase = Base.objects.get(id=base)
			rbase.fecha = datetime.now()-timedelta(hours=5)
			rbase.tfingestion = datetime.now()-timedelta(hours=5)
			rbase.save()

			age = Agentes.objects.get(id=agente)

			

			if age.checabreak:

				if int(age.checabreak) == 1:

					age.estado_id = 8
					age.save()

			if age.checa:

				if int(age.checa) == 1:

					age.estado_id = 5
					age.save()

			if age.checaser:

				if int(age.checaser) == 1:

					age.estado_id = 9
					age.save()



			resultado_name = Resultado.objects.get(id=resultado).name

		
	

			b = Base.objects.get(id=base)
			if resultado_name == 'No Contacto':
				
				cliente = b.id_cliente
				Base.objects.filter(id_cliente=cliente).update(bloqueocliente=0) 

			b.resultado_id = resultado
			b.resultadotxt = resultado_name
			b.save()


		data_dict = ValuesQuerySetToDict(data)

		data = simplejson.dumps(data_dict)

		return HttpResponse(data, content_type="application/json")

@login_required(login_url="/ingresar")
def nota(request):

		data = Nota.objects.all().values('id','tipo').order_by('-id')

		data_dict = ValuesQuerySetToDict(data)

		data = simplejson.dumps(data_dict)

		return HttpResponse(data, content_type="application/json")


@login_required(login_url="/ingresar")
def agendar(request):

		fechaa= json.loads(request.body)['fecha']
		agente =  json.loads(request.body)['agente']
		base =  json.loads(request.body)['base']

		if request.method == 'POST':

			date = str(fechaa['date'])
			time = str(fechaa['time'])

			fechaag =  date + " " +time

			fmt = '%Y-%m-%d %H:%M'
	
			fecha = datetime.strptime(str(fechaag),fmt)-timedelta(hours=5)


			Agendados(base_id=base,fecha=fecha,agente_id=agente).save()

		return HttpResponse('data', content_type="application/json")



@login_required(login_url="/ingresar")
def examen(request):

		data = Examen.objects.all().values('id','nombre').order_by('id')

		data_dict = ValuesQuerySetToDict(data)

		data = simplejson.dumps(data_dict)


		return HttpResponse(data, content_type="application/json")


@login_required(login_url="/ingresar")
def totalestllam(request):

	
		data = AjxProLla.objects.all().values('llam_estado').annotate(total=Count('llam_estado'))

		data_dict = ValuesQuerySetToDict(data)

		data = simplejson.dumps(data_dict)


		return HttpResponse(data, content_type="application/json")


@login_required(login_url="/ingresar")
def getempresa(request):

		id = request.user.id

		id_empresa = AuthUser.objects.get(id=id).empresa.id

		data = Empresa.objects.filter(id=id_empresa).values('id','nombre')

		data_dict = ValuesQuerySetToDict(data)

		data = simplejson.dumps(data_dict)

		return HttpResponse(data, content_type="application/json")



@login_required(login_url="/ingresar")
def licencias(request):

		id = request.user.id

		id_empresa = AuthUser.objects.get(id=id).empresa.id

		numlic = Empresa.objects.get(id=id_empresa).licencias

		if request.method == 'POST':

			licencias = json.loads(request.body)['dato']

			lic_tmp = licencias['lictemporal']
			finicio = licencias['finicio']
			ffin = licencias['ffin']

			LicenciasTmp(lic_tmp=lic_tmp,finicio=finicio,ffin=ffin,empresa_id=id_empresa).save()


		return HttpResponse(numlic, content_type="application/json")


@login_required(login_url="/ingresar")
def lictmp(request):

		id = request.user.id

		id_nivel=AuthUser.objects.get(id=id).nivel.id
		id_empresa =AuthUser.objects.get(id=id).empresa.id

		if id_nivel == 4:

			licencias = LicenciasTmp.objects.all().values('id','lic_tmp','finicio','ffin','empresa__nombre')

		else:

			licencias = LicenciasTmp.objects.filter(empresa_id=id_empresa).values('id','lic_tmp','finicio','ffin','empresa__nombre')




		fmt = '%Y-%m-%d %H:%M:%S %Z'

		for i in range(len(licencias)):

			licencias[i]['finicio'] = LicenciasTmp.objects.get(id=licencias[i]['id']).finicio.strftime(fmt)
			licencias[i]['ffin'] = LicenciasTmp.objects.get(id=licencias[i]['id']).ffin.strftime(fmt)


		data_dict = ValuesQuerySetToDict(licencias)

		data = simplejson.dumps(data_dict)

		return HttpResponse(data, content_type="application/json")

@login_required(login_url="/ingresar")
def graphcpu(request):


	cpu = Monitorserver.objects.all().values('id','dsk_use','total_mem','use_mem','total_swap','use_swap','s_usada','cpu','astcpuuse','astmemuse','pytcpuuse','sqlcpuuse','sqlmemuse','activecall','dsk_tot').order_by('-id')[0:30]

	fmt = '%Y-%m-%d %H:%M:%S %Z'

	for i in range(len(cpu)):

		cpu[i]['date'] = Monitorserver.objects.get(id=cpu[i]['id']).date.strftime(fmt)
		

	data_dict = ValuesQuerySetToDict(cpu)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")



@login_required(login_url="/ingresar")

def agregarcartera(request):

	if request.method == 'POST':


		data= json.loads(request.body)['dato']
		user=json.loads(request.body)['user']

		id_user = user['id']
		id_supervisor=Supervisor.objects.get(user_id=id_user).id
		id_caem=data['id']
		id_cartera = Carteraempresa.objects.get(id=id_caem).cartera.id

		data = Cartera.objects.get(id=id_cartera).nombre

		Supervisorcartera(supervisor_id=id_supervisor,cartera_id=id_cartera).save()
		return HttpResponse(data, content_type="application/json")


@login_required(login_url="/ingresar")
def gestion(request):


	if request.method == 'POST':

		cliente = json.loads(request.body)['cliente']
		fecha= json.loads(request.body)['fechagestion']
		id_agente =json.loads(request.body)['agente']
		word =json.loads(request.body)['word']

		
		fmt = '%Y-%m-%dT%H:%M:%S.%fZ'
	
		fecha = datetime.strptime(str(fecha),fmt)

		id_cliente = cliente['id']

		fecha= fecha-timedelta(hours=10)

	

		agente = Agentes.objects.filter(id=id_agente)
		
		for agente in agente:
			agente.wordstipeo = word
			agente.save()

		base = Agentebase.objects.filter(base_id=id_cliente,agente_id=id_agente).order_by('-id')[:1]
		
		for base in base:
			base.estado_id = 6
			base.tinicio = fecha
			base.save()

	return HttpResponse('data', content_type="application/json")


@login_required(login_url="/ingresar")
def lanzaespera(request):

	if request.method == 'POST':

		data = json.loads(request.body)
		agente_id = data['agente']
		agente = Agentes.objects.get(id=agente_id)
		agente.tinicioespera = datetime.now()-timedelta(hours=5)

		if agente.estado_id !=3:

			agente.est_ag_predictivo = 0
			agente.estado_id= 2
			agente.save()

		return HttpResponse('data', content_type="application/json")



@login_required(login_url="/ingresar")
def gestionupdate(request):


	if request.method == 'POST':

		gestion = json.loads(request.body)['gestion']
		agente = json.loads(request.body)['agente']
		cliente = json.loads(request.body)['cliente']['id']

		age = Agentes.objects.get(id=agente)
		age.estado_id = 2
		age.save()

		age = Agentes.objects.get(id=agente)

		if int(age.checa) == 1:

			age.estado_id = 5
			age.save()

		if int(age.checaser) == 1:

			age.estado_id = 9
			age.save()

		if int(age.checabreak) == 1:

			age.estado_id = 8
			age.save()

		comentario = gestion['comentario']

		if len(gestion)>1:

			if gestion['fecha']:
				fecha = gestion['fecha']
			if gestion['monto']:
				monto = gestion['monto']

			base = Agentebase.objects.filter(base_id=cliente,agente_id=agente).order_by('-id')[:1]

			for base in base:

				base.facuerdo = fecha
				base.macuerdo = monto
				base.save()

			bax = Base.objects.get(id=cliente)

			resultado = bax.resultado_id

			flag_call = Resultado.objects.get(id=resultado).flag_call
			dni = bax.id_cliente

			if flag_call == 0:

				base = Base.objects.filter(id_cliente=dni)
				
				for b in base:
					b.bloqueocliente = 0
					b.save()

			if flag_call == 1:
				pass


			
			bax.detalle = comentario
			bax.monto = monto
			bax.fecha = fecha
			bax.tfingestion = datetime.now()-timedelta(hours=5)
			bax.save()


		user = Agentes.objects.get(id=agente).user.username
		
		redis_publisher = RedisPublisher(facility='foobar', users=[user])
		message = RedisMessage('llamada')
		redis_publisher.publish_message(message)

		agente = Agentes.objects.get(id=agente)
		agente.wordstipeo = 0
		agente.tinicioespera = datetime.now()-timedelta(hours=5)
		agente.save() 
		
		return HttpResponse('data', content_type="application/json")




@login_required(login_url="/ingresar")
def tgestion(request,id_agente):


	agentebase = Agentes.objects.filter(id=id_agente)

	for agente in agentebase:

		if agente.estado.id ==1:
			pass

		if agente.estado.id ==2:
			fecha = agente.tinicioespera

		if agente.estado.id ==3:
			fecha = agente.tiniciollamada

		if agente.estado.id ==6:
			fecha = agente.tiniciogestion

		if agente.estado.id ==5:
			fecha = agente.tiniciopausa
		if agente.estado.id ==8:
			fecha = agente.tiniciobreak
		if agente.estado.id ==9:
			fecha = agente.tinicioservicio

	

	ti= str(fecha)[0:19]
	tf= str(datetime.now())[0:19]

	fmt = '%Y-%m-%d %H:%M:%S'

	ti = datetime.strptime(ti,fmt)
	tf = datetime.strptime(tf,fmt)

	return HttpResponse(ti, content_type="application/json")

@login_required(login_url="/ingresar")
def tllamada(request,id_base,id_agente):


	agentebase = Agentebase.objects.filter(base_id=id_base,agente_id=id_agente)

	for agente in agentebase:

		fecha = agente.tiniciollamada
	

	ti= str(fecha)[0:19]
	tf= str(datetime.now())[0:19]

	fmt = '%Y-%m-%d %H:%M:%S'

	ti = datetime.strptime(ti,fmt)
	tf = datetime.strptime(tf,fmt)

	return HttpResponse(tf-ti, content_type="application/json")


	
@login_required(login_url="/ingresar")
def agregarfiltro(request):

	if request.method == 'POST':

		data = json.loads(request.body)

		grupo= json.loads(request.body)['grupo']
		ciudad= json.loads(request.body)['ciudad']
		segmento= json.loads(request.body)['segmento']
		campania = json.loads(request.body)['campania']
		resultado = ''

		for d in data:

			if d == 'resultado':

				resultado = data['resultado']

		ciudadt = ""
		grupot = ""
		segmentot = ""
		resultadot = ""

		r =[]
		c=[]
		g=[]
		s=[]

		
		for i in range(len(resultado)):

			resultadot = resultadot  + resultado[i]['name'] +'/'
			r.insert(i,resultado[i]['name'])

		for i in range(len(ciudad)):

			ciudadt = ciudadt  + ciudad[i]['status_f'] +'/'
			c.insert(i,ciudad[i]['status_f'])

		for i in range(len(grupo)):

			grupot = grupot  + grupo[i]['status_g'] +'/'
			g.insert(i,grupo[i]['status_g'])

		for i in range(len(segmento)):

			segmentot = segmentot  + segmento[i]['status_h'] +'/'
			s.insert(i,segmento[i]['status_h'])

		print r,c,g,s

		print 'xxx',Base.objects.filter(resultado__name__in=r,status_f__in=c,status_g__in=g,status_h__in=s,campania_id=campania).update(proflag=None,proestado=None,filtrohdec=None,status=0)



		i = Filtro.objects.filter(campania_id=campania).count()

		Filtro(resultado=resultadot,status_f=ciudadt,status_g=grupot,status_h=segmentot,campania_id=campania,status=1,orden=i+1).save()

		return HttpResponse('data', content_type="application/json")


@login_required(login_url="/ingresar")
def eliminarfiltro(request):

	if request.method == 'POST':

		#id {u'dato': {u'status': 1, u'index': 0, u'resultado': u'', u'status_h': u'BASE/', u'status_g': u'ORIENTE/', u'status_f': u'PENDIENTE/', u'id': 146, u'color': u'#FAF8F8', u'fonosporbarrer': 0, u'colort': u'#564D4D', u'statusname': u'Apagado', u'total': 0, u'fonosin

		

		id_filtro= json.loads(request.body)['dato']['id']

		campania = Filtro.objects.get(id=id_filtro).campania

		Filtro.objects.get(id=id_filtro).delete()

		fil = Filtro.objects.filter(campania_id=campania).order_by('id')

		i=0

		for f in fil:

			f.orden = i+1
			f.save()
			i=i+1


		return HttpResponse(id_filtro, content_type="application/json")


@login_required(login_url="/ingresar")
def preguntas(request,examen):

		if request.method == 'GET':

			data = PregExam.objects.filter(examen=examen).values('id','pregunta','examen__nombre','valor').order_by('id')

			for i in range(len(data)):

				data[i]['estadosi'] = True

				data[i]['estadono'] = True

			data_dict = ValuesQuerySetToDict(data)

			data = simplejson.dumps(data_dict)

			return HttpResponse(data, content_type="application/json")

		if request.method == 'POST':

			tipo = json.loads(request.body)['add']

			data = json.loads(request.body)['dato']

			pregunta = data['pregunta']

			respuesta = data['respuesta']

			if tipo == 'New':

				Preguntas(pregunta=pregunta,respuesta=respuesta).save()

				id_pregunta = Preguntas.objects.all().values('id').order_by('-id')[0]['id']

				pregunta = Preguntas.objects.get(id=id_pregunta)

				return HttpResponse(pregunta.pregunta, content_type="application/json")

			if tipo == 'Edit':

				id_pregunta = data['id']

				datap = Preguntas.objects.get(id=id_pregunta)
			
				datap.pregunta = pregunta

				datap.respuesta = respuesta

				datap.save()

				return HttpResponse(datap.pregunta, content_type="application/json")

			if tipo == 'Eliminar':

				id_pregunta = data['id']

				pregunta = Preguntas.objects.get(id=id_pregunta)
				
				pregunta.delete()

				return HttpResponse(pregunta.pregunta, content_type="application/json")



@login_required(login_url="/ingresar")
def mascaras(request):

		data = Mascara.objects.all().values('id','tipo').order_by('-id')

		data_dict = ValuesQuerySetToDict(data)

		data = simplejson.dumps(data_dict)

		return HttpResponse(data, content_type="application/json")

@login_required(login_url="/ingresar")
def getanexo(request,nivel):

		if int(nivel) == 3:

			anexo = []

			for i in range(100, 300):
			
				anexo.insert(0,i)

			

			users = AuthUser.objects.all()

			anexouso = []

			for u in users:

			

				if u.anexo > 0:

					anexouso.insert(0,int(u.anexo))

			libres = []
			
			for i in anexo:

				if i in anexouso:

					pass
				else:

					libres.insert(0,i)

			


			anexo = json.dumps(libres)

		else:

			anexo = []

			for i in range(300, 500):
			
				anexo.insert(0,i)

			

			users = AuthUser.objects.all()

			anexouso = []

			for u in users:

				if u.anexo > 0:

					anexouso.insert(0,int(u.anexo))

			libres = []
			
			for i in anexo:

				if i in anexouso:

					pass
				else:

					libres.insert(0,i)

		libres = sorted(libres, reverse = True)

		anexo = json.dumps(libres)

		return HttpResponse(anexo, content_type="application/json")

@login_required(login_url="/ingresar")
def resultadototal(request):



		data = Resultado.objects.all().values('id','name','tipo','codigo').order_by('-id')

		data_dict = ValuesQuerySetToDict(data)

		data = simplejson.dumps(data_dict)

		return HttpResponse(data, content_type="application/json")

@login_required(login_url="/ingresar")
def resultado(request,campania):

		xdata = Base.objects.filter(campania_id=campania).annotate(total=Count('resultado'))
		

		lista=[]

		for x in xdata:

			lista.append(x.resultado_id)

		

		data = Resultado.objects.filter(id__in =lista).values('id','name','tipo','codigo').order_by('-id')

		data_dict = ValuesQuerySetToDict(data)

		data = simplejson.dumps(data_dict)

		return HttpResponse(data, content_type="application/json")


@login_required(login_url="/ingresar")
def agente(request,id_agente):

	data = Agentes.objects.filter(id=id_agente).values('id','user__empresa_id','user__anexo','fono','atendidas','contactadas','estado__nombre','user__first_name','supervisor','calificacion','user__empresa__mascaras__tipo','user__empresa__url').order_by('-id')

	#for i in range(len(data)):

		#data[i]['media'] = data[i]['contactadas']*100/data[i]['atendidas']

	data_dict = ValuesQuerySetToDict(data)

	data = simplejson.dumps(data_dict)

	'''
	AjxProLla.objects.filter(age_codigo=id_agente).count()

	t = datetime.strftime(datetime.now(), '%Y-%m-%d')

	xx = AjxProLla.objects.filter(age_codigo=id_agente,llam_estado=4)

	c = 0

	for x in xx:

		if str(t) == str(x.f_origen)[0:10]:

			c=c+1

	#atendidas = c
	'''

	atendidas = 1
	'''
	

	acuerdos = Base.objects.filter(agente_id=id_agente,resultado_id__in=[15,5]).count()

	if atendidas == 0:
		media = 0
	else:
		media=float(acuerdos)*100/float(atendidas)
		media = round(media,2)
	'''
	acuerdos = 1
	media = 1
	
	data = {'data':data,'atendidas':atendidas,'acuerdos':acuerdos,'media':media}

	data = simplejson.dumps(data)

	return HttpResponse(data, content_type="application/json")


@login_required(login_url="/ingresar")
def agenteparametros(request,id_agente):

	AjxProLla.objects.filter(age_codigo=id_agente).count()

	t = datetime.strftime(datetime.now(), '%Y-%m-%d')

	xx = AjxProLla.objects.filter(age_codigo=id_agente,llam_estado=4)

	c = 0

	for x in xx:

		if str(t) == str(x.f_origen)[0:10]:

			c=c+1

	atendidas = c
	
	

	yy = Base.objects.filter(agente_id=id_agente,resultado_id__in=[15,5])

	a = 0

	for x in yy:

		if str(t) == str(x.tiniciogestion)[0:10]:

			a=a+1

	acuerdos = a

	if atendidas == 0:
		media = 0
	else:
		media=float(acuerdos)*100/float(atendidas)
		media = round(media,2)
	
	data = {'atendidas':atendidas,'acuerdos':acuerdos,'media':media}

	data = simplejson.dumps(data)

	return HttpResponse(data, content_type="application/json")


def lanzallamada(request,id_agente,id_base,id_cliente):

		agente = Agentes.objects.get(id=id_agente)
		mascara = agente.user.empresa.mascaras.tipo
		user = agente.user.username
		agente.estado_id = 3
		agente.est_ag_predictivo = 0
		agente.tiniciollamada = datetime.now()-timedelta(hours=5)
		agente.save()

		Base.objects.filter(agente_id=id_agente).update(status=0)

		redis_publisher = RedisPublisher(facility='foobar', users=[user])

		message = RedisMessage('llamada')

		redis_publisher.publish_message(message)

		redis_publisher = RedisPublisher(facility='foobar', users=[user])

		message = RedisMessage('ll')

		redis_publisher.publish_message(message)


		base = Base.objects.get(id=id_base)
		base.agente_id = id_agente
		base.status = 1
		base.tiniciogestion = datetime.now()-timedelta(hours=5)

		base.save()


		return HttpResponse(str(base.cliente)+str(base.telefono), content_type="application/json")



def finllamada(request,id_agente):

		agente = Agentes.objects.get(id=id_agente)


		user = agente.user.username
		agente.est_ag_predictivo = 0

		if int(agente.estado_id) == 3:
			agente.estado_id = 6
			agente.est_ag_predictivo = 0

		agente.tiniciogestion = datetime.now()-timedelta(hours=5)
		agente.save()


		redis_publisher = RedisPublisher(facility='foobar', users=[user])

		message = RedisMessage('llamadax')

		redis_publisher.publish_message(message)


		return HttpResponse('fin llamada', content_type="application/json")


@login_required(login_url="/ingresar")
def cliente(request,id_agente):

		user = Agentes.objects.get(id=id_agente).user.username

		redis_publisher = RedisPublisher(facility='foobar', users=[user])

		message = RedisMessage('Consulta')

		redis_publisher.publish_message(message)

		base = Base.objects.filter(agente_id=id_agente,status=1).order_by('-id').values('id','telefono','orden','cliente','id_cliente','status_a','status_b','status_c','status_d','status_e','status_f','status_g','status_h','status','campania__nombre','resultado__name','resultado','campania__mxllamada','campania__mxllamada','campania__hombreobjetivo','campania__cartera__nombre')

		fmt = '%Y-%m-%d %H:%M:%S %Z'

		for i in range(len(base)):

			if Base.objects.get(id=base[i]['id']).tiniciollamada == None:
				base[i]['tiniciollamada'] = ''
			else:
				base[i]['tiniciollamada'] = Base.objects.get(id=base[i]['id']).tiniciollamada.strftime(fmt)

		data_dict = ValuesQuerySetToDict(base)

		data = simplejson.dumps(data_dict)

		return HttpResponse(data, content_type="application/json")


@login_required(login_url="/ingresar")
def atendida(request,id_agente):
		

		today = datetime.now()

		fmt1 = '%Y-%m-%d'

		today =  today.strftime(fmt1)

		ajax = AjxProLla.objects.filter(age_codigo=id_agente).order_by('-id_ori_llamadas')

		

		t=0

		for i in ajax:

			if str(i.f_origen).split(" ")[0] == today:

				

				t = t + i.duration 


		return HttpResponse(t, content_type="application/json")


@login_required(login_url="/ingresar")
def desfase(request,id_agente):

		id = request.user.id

		user = AuthUser.objects.filter(id=id).values('id')

		fmt = '%Y-%m-%d %H:%M:%S %Z'

		for i in range(len(user)):

			user[i]['last_login'] = AuthUser.objects.get(id=user[i]['id']).last_login.strftime(fmt)

			datex = AuthUser.objects.get(id=user[i]['id']).last_login
		
			a = datetime(datex.year,datex.month,datex.day,datex.hour,datex.minute,datex.second)

			b = datetime.now()
			
			user[i]['conectado'] = str(b - a)[0:7]

		conectado = user[0]['conectado']

		
		cantidad = Agentebase.objects.filter(agente_id=id_agente).values('agente').annotate(total=Sum('duracion'))
		num=int(cantidad[0]['total'])  
		hor=(int(num/3600))  
		minu=int((num-(hor*3600))/60)  
		seg=num-((hor*3600)+(minu*60))  

		atendida = str(hor)+":"+str(minu)+":"+str(seg)
		
		if minu < 10:

			atendida = str(hor)+":0"+str(minu)+":"+str(seg)

		if seg < 10:

			atendida = str(hor)+":"+str(minu)+"0:"+str(seg)

		if seg < 10 or minu < 10 :

			atendida = str(hor)+":0"+str(minu)+":0"+str(seg)

		at = datetime.strptime(atendida, "%H:%M:%S")

		co = datetime.strptime(conectado, "%H:%M:%S")

		data = co-at

		return HttpResponse(data, content_type="application/json")

@login_required(login_url="/ingresar")
def pausa(request,id_agente):


		agente = Agentes.objects.get(id=id_agente)
		user = agente.user.id

		if agente.estado.id == 2:
			agente.estado_id = 5
			agente.checabreak = 0
			agente.checa = 0
			agente.checaser = 0
			Estadocambio(user_id=user,estado_id=5).save()

		if agente.estado.id == 8:
			agente.estado_id = 5
			agente.checabreak = 0
			agente.checa = 0
			agente.checaser = 0
			Estadocambio(user_id=user,estado_id=5).save()


		if agente.estado.id == 9:
			agente.estado_id = 5
			agente.checabreak = 0
			agente.checa = 0
			agente.checaser = 0
			Estadocambio(user_id=user,estado_id=5).save()


		if agente.estado.id == 5:
			agente.estado_id = 2
			agente.checabreak = 0
			agente.checa = 0
			agente.checaser = 0
			Estadocambio(user_id=user,estado_id=2).save()



		if agente.estado.id == 3:

			agente.checaser = 0
			agente.checa = 1
			agente.checabreak = 0
			

		agente.tiniciopausa = datetime.now()-timedelta(hours=5)
		
		agente.save()


		return HttpResponseRedirect("/teleoperador/"+id_agente)

@login_required(login_url="/ingresar")
def receso(request,id_agente):

		agente = Agentes.objects.get(id=id_agente)
		user = agente.user.id

		

		if agente.estado.id== 2:

			agente.estado_id = 8
			agente.checabreak = 0
			agente.checaser = 0
			agente.checa = 0
			Estadocambio(user_id=user,estado_id=8).save()

		if agente.estado.id== 5:

			agente.estado_id = 8
			agente.checabreak = 0
			agente.checaser = 0
			agente.checa = 0
			Estadocambio(user_id=user,estado_id=8).save()

		if agente.estado.id== 9:

			agente.estado_id = 8
			agente.checabreak = 0
			agente.checaser = 0
			agente.checa = 0
			Estadocambio(user_id=user,estado_id=8).save()

		if agente.estado.id== 8:

			agente.estado_id = 2
			agente.checabreak = 0
			agente.checaser = 0
			agente.checa = 0

		if agente.estado.id== 3:

			agente.checabreak = 1
			agente.checa = 0
			agente.checaser = 0


		agente.tiniciobreak = datetime.now()-timedelta(hours=5)

		agente.save()

		return HttpResponseRedirect("/teleoperador/"+id_agente)



@login_required(login_url="/ingresar")
def sshh(request,id_agente):

		agente = Agentes.objects.get(id=id_agente)
		user = agente.user.id

		

		if agente.estado.id== 2:

			agente.estado_id = 9
			agente.checabreak = 0
			agente.checaser = 0
			agente.checa = 0
			Estadocambio(user_id=user,estado_id=9).save()

		if agente.estado.id== 5:

			agente.estado_id = 9
			agente.checabreak = 0
			agente.checaser = 0
			agente.checa = 0
			Estadocambio(user_id=user,estado_id=9).save()

		if agente.estado.id== 8:

			agente.estado_id = 9
			agente.checabreak = 0
			agente.checaser = 0
			agente.checa = 0
			Estadocambio(user_id=user,estado_id=9).save()

		if agente.estado.id== 3:

			agente.checaser = 1
			agente.checa = 0
			agente.checabreak = 0

		if agente.estado.id== 9:

			agente.estado_id = 2
			agente.checaser = 2
			agente.checa = 0
			agente.checabreak = 0
			Estadocambio(user_id=user,estado_id=2).save()

		agente.tinicioservicio = datetime.now()-timedelta(hours=5)

		agente.save()

		return HttpResponseRedirect("/teleoperador/"+id_agente)



@login_required(login_url="/ingresar")
def reportecsv(request,cartera,campania):

	response = HttpResponse(content_type='text/csv')

	ncartera=Campania.objects.get(id=campania).cartera.nombre
	ncampania = Campania.objects.get(id=campania).nombre
	fecha= datetime.now()

	response['Content-Disposition'] = 'attachment; filename="RG_'+str(ncartera)+'_'+str(ncampania)+'_'+str(fecha)[0:19]+'.csv'

	writer = csv.writer(response)

	#resultado = Base.objects.filter(campania_id=campania).values('resultado').order_by('-resultado').annotate(total=Count('resultado'))[0]['resultado']

	base = Base.objects.filter(campania_id=campania).order_by('-id_cliente')

	writer.writerow(['Telefono','Orden','Cliente','ID Cliente','Cartera','Campania','Status A','Status B','Status C','Status D','Status E','Status F','Status G','Status H','Mejor Gestion','Fecha','Telefono','Agente','Intentos','Botonera','Observacion','Fecha de Pago','Importe de Pago','Duracion','Fecha de Gestion'])

	dniant = '2222'

	mejorgestion = ''

	for x in base:

		dniact = x.id_cliente

		status_b = x.status_b.replace('u"','').replace('"','')

		telefono = x.telefono

		intentos = AjxProLla.objects.filter(llam_numero=telefono,cam_codigo=campania).count()

		resultado = 'Sin Gestion'

		bx =Base.objects.filter(id_cliente=dniact)
		pant =0
		mejorgestion = 'Sin Gestion'
		p=0

		for r in bx:

			if r.resultado:

				resultado = r.resultado.name
		
				if resultado == 'Msj Tercero (No vive)':

					p =1

					if p>pant:

						mejorgestion = 'Msj Tercero (No vive)'

				if resultado == 'Msj Tercero (Si vive)':

					p = 2

					if p>pant:

						mejorgestion = 'Msj Tercero (Si vive)'

				if resultado == 'Contacto Indirecto':
					p=3

					if p>pant:

						mejorgestion = 'Contacto Indirecto'

				if resultado == 'Contacto Directo':
					p=4
					if p>pant:
						mejorgestion = 'Contacto Directo'

				if resultado == 'Promesa':
					p=5
					if p>pant:
						mejorgestion = 'Promesa'

				pant = p
			
		x.campania.nombre = x.campania.nombre.encode('ascii','ignore')

		x.campania.nombre = x.campania.nombre.encode('ascii','replace')

		x.monto = x.monto.encode('ascii','ignore')

		x.monto = x.monto.encode('ascii','replace')

		if x.agente:

			agente = x.agente.user.first_name

		else:

			agente = ''

		duracion = ''

		if x.tiniciogestion and x.tfingestion :

			inicio = x.tiniciogestion
			fin = x.tfingestion
			fmt = '%M:%S'

			duracion = str(fin-inicio)[2:8]

		#writer.writerow(['Id','Telefono','Orden','Cliente','ID Cliente','Cartera','Campania','Status A','Status B','Status C','Status D','Status E','Status F','Status G','Status H','Mejor Gestion','Fecha','Telefono','Agente','Intentos','Botonera','Observacion','Fecha de Pago','Importe de Pago','Duracion','Fecha de Gestion'])

		writer.writerow([x.telefono,x.orden,x.cliente,x.id_cliente,x.campania.cartera.nombre,x.campania.nombre,x.status_a,x.status_b,x.status_c,x.status_d,x.status_e,x.status_f,x.status_g,x.status_h,mejorgestion,x.fecha,x.telefono,agente,intentos,resultado,x.detalle,x.fecha,x.monto,duracion,x.tfingestion])

		dniant = x.id_cliente

	return response



@login_required(login_url="/ingresar")
def getcampanias(request,cartera):


	
	id = request.user.id
	nivel = AuthUser.objects.get(id=id).nivel.id

	if nivel == 4: #Manager

		pass
	if nivel == 2: #Supervisores
		
		pass
	if nivel == 1: #Admin

		pass

	if nivel == 5: #Monitor

		cartera = Carteraempresa.objects.get(id=cartera).cartera.id
	
	campanias = Campania.objects.filter(cartera_id=cartera).values('id','usuario__first_name','estado','nombre','troncal','canales','timbrados','mxllamada','llamadaxhora','hombreobjetivo','supervisor__user__first_name').order_by('-id')

	data_dict = ValuesQuerySetToDict(campanias)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@login_required(login_url="/ingresar")
def traercampania(request,campania):

		carteras = Campania.objects.filter(id=campania).values('id','usuario__first_name','estado','nombre','troncal','canales','timbrados','mxllamada','llamadaxhora','hombreobjetivo','supervisor__user__first_name').order_by('-id')
	
		data_dict = ValuesQuerySetToDict(carteras)

		data = simplejson.dumps(data_dict)

		return HttpResponse(data, content_type="application/json")


@login_required(login_url="/ingresar")
def play(request,id_agente):


		agente = Agentes.objects.get(id=id_agente)
		agente.estado_id = 2
		agente.save()




		return HttpResponseRedirect("/teleoperador/"+id_agente)

@login_required(login_url="/ingresar")
def resultadofiltro(request,id_filtro):

		filtro = Filtro.objects.get(id=id_filtro)

		resultado = filtro.resultado

		resultado =  resultado.split('/')

		status_f = filtro.status_f

		status_f =  status_f.split('/')
		
		status_h = filtro.status_h

		status_h =  status_h.split('/')

		status_g = filtro.status_g

		status_g =  status_g.split('/')
		
		resultadototal = Base.objects.filter(resultado__name__in=resultado,status_f__in=status_f,status_g__in=status_g,status_h__in=status_h).count()

		resultadobarrido = Base.objects.filter(resultado__name__in=resultado,status_f__in=status_f,status_g__in=status_g,status_h__in=status_h,status=1).count()

		data = {'resultadototal':resultadototal,'resultadobarrido':resultadobarrido}

		data = json.dumps(data)

		return HttpResponse(data, content_type="application/json")



@login_required(login_url="/ingresar")
def carteras(request):

	id = request.user.id
	nivel = AuthUser.objects.get(id=id).nivel.id
	empresa = AuthUser.objects.get(id=id).empresa.id

	if request.method == 'GET':

		if nivel == 1:

			data = Carteraempresa.objects.filter(empresa_id=empresa).values('id','cartera__nombre','empresa__nombre','cartera_id','user__first_name').order_by('-id')

		if nivel == 2:

			data =Supervisorcartera.objects.filter(supervisor__user__id=id).values('id','cartera__nombre','cartera_id')

		if nivel == 3:

			data = Carteraempresa.objects.filter(empresa_id=empresa).values('id','cartera__nombre','empresa__nombre','cartera_id','user__first_name').order_by('-id')

		if nivel == 4:

			data = Carteraempresa.objects.all().values('id','cartera__nombre','empresa__nombre','cartera_id','user__first_name').order_by('-id')

		if nivel == 5:

			data = Carteraempresa.objects.filter(empresa_id=empresa).values('id','cartera__nombre','empresa__nombre','cartera_id','user__first_name').order_by('-id')

		
		fmt = '%Y-%m-%d %H:%M:%S %Z'

		#for i in range(len(data)):

			#data[i]['fecha'] = Carteraempresa.objects.get(id=data[i]['id']).fecha.strftime(fmt)
		
		data_dict = ValuesQuerySetToDict(data)

		data = simplejson.dumps(data_dict)

		return HttpResponse(data, content_type="application/json")

	if request.method == 'POST':

		data= json.loads(request.body)['dato']
		tipo= json.loads(request.body)['add']

		if tipo == 'New':

			Cartera(nombre=data['cartera']).save()

			id_cartera = Cartera.objects.all().values('id').order_by('-id')[0]['id']

			Carteraempresa(cartera_id=id_cartera,empresa_id=empresa,user_id=id).save()

			data = Cartera.objects.get(id=id_cartera)

			return HttpResponse(data.nombre, content_type="application/json")

		if tipo == 'Edit':

			
			id_cartera = data['id']
			cartera = Carteraempresa.objects.get(id=id_cartera).cartera.id
			cartera = Cartera.objects.get(id=cartera)
			cartera.nombre = data['cartera__nombre']
			cartera.save()

			return HttpResponse(cartera.nombre, content_type="application/json")

		if tipo == 'Eliminar':

			

			id_cartera = data['id']
			cartera = Carteraempresa.objects.get(id=id_cartera)
			
			cartera.delete()

			return HttpResponse('cartera.nombre', content_type="application/json")





@login_required(login_url="/ingresar")
def listafiltros(request,id_campania):


	data = Filtro.objects.filter(campania_id=id_campania).values('id','status_f','status_h','status_g','resultado','status').order_by('-id')


	for i in range(len(data)):

		filtro = Filtro.objects.get(id=data[i]['id'])

		if data[i]['status']==1:


			data[i]['color'] = '#FAF8F8'
			
			data[i]['colort'] = '#000'

		
			data[i]['statusname'] = 'Apagado'

		else:

			data[i]['color'] = '#3AAED8'
			data[i]['colort'] = '#fff'

			data[i]['statusname'] = 'Activado'
		

		resultado = filtro.resultado

		resultado =  resultado.split('/')

		status_f = filtro.status_f

		status_f =  status_f.split('/')

		status_h = filtro.status_h

		status_h =  status_h.split('/')

		status_g = filtro.status_g

		status_g =  status_g.split('/')

		print resultado 
		print status_f
		print status_g
		print status_h

		
		resultadonullos = Base.objects.filter(resultado_id__isnull=True,campania_id=id_campania,status_f__in=status_f,status_g__in=status_g,status_h__in=status_h).count()

		f = open('/var/www/html/nullos.txt', 'a')
		f.write('kkk'+str(resultadonullos))
		f.close()
		
		resultadototal = Base.objects.filter(resultado__name__in=resultado,campania_id=id_campania,status_f__in=status_f,status_g__in=status_g,status_h__in=status_h).count()+resultadonullos

		resultadobarrido = Base.objects.filter(campania_id=id_campania,status_f__in=status_f,status_g__in=status_g,status_h__in=status_h,proflag=1,resultado__name__in=resultado).count()

		if int(resultadototal) == int(resultadobarrido):

			#filtro.status = 1
			#filtro.save()
			pass

		#fonosinexito = Base.objects.filter(campania_id=id_campania,resultado__name__in=resultado,status_f__in=status_f,status_g__in=status_g,status_h__in=status_h,status=2).count()

		data[i]['total'] = resultadototal 
		data[i]['fonosporbarrer'] = resultadobarrido
		#data[i]['fonosinexito'] = fonosinexito

	data_dict = ValuesQuerySetToDict(data)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@login_required(login_url="/ingresar")
def activafiltro(request,id_filtro,id_campania):


	data = Filtro.objects.filter(id=id_filtro).values('id','status_f','status_h','status_g','resultado').order_by('-id')

	for i in range(len(data)):


		filtro = Filtro.objects.get(id=data[i]['id'])

		os.environ['body']='PeruCall Se activo filtro'

		os.environ['title']='http://10.13.50.50/filtros/'+str(id_filtro)

		os.system('./b.sh')

	
		filtro.status = 0
		filtro.save() 

		resultado = filtro.resultado

		resultado =  resultado.split('/')

		status_f = filtro.status_f

		status_f =  status_f.split('/')

		status_h = filtro.status_h

		status_h =  status_h.split('/')

		status_g = filtro.status_g

		status_g =  status_g.split('/')


		base = Base.objects.filter(campania_id=id_campania,resultado__name__in=resultado,status_f__in=status_f,status_g__in=status_g,status_h__in=status_h)

		for base in base:

			base.status = 1
			base.save()


	data_dict = ValuesQuerySetToDict(data)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@login_required(login_url="/ingresar")
def desactivafiltro(request,id_filtro,id_campania):


	data = Filtro.objects.filter(id=id_filtro).values('id','status_f','status_h','status_g','resultado').order_by('-id')

	for i in range(len(data)):



		filtro = Filtro.objects.get(id=data[i]['id'])

		filtro.status = 1
		filtro.save() 

		resultado = filtro.resultado

		resultado =  resultado.split('/')

		status_f = filtro.ciudad

		status_f =  status_f.split('/')

		status_h = filtro.segmento

		status_h =  status_h.split('/')

		status_g = filtro.grupo

		status_g =  status_g.split('/')

		base = Base.objects.filter(campania_id=id_campania,resultado__name__in=resultado,status_f__in=status_f,status_g__in=status_g,status_h__in=status_h)

		for base in base:

			base.status = 0
			base.save()
			

	data_dict = ValuesQuerySetToDict(data)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@login_required(login_url="/ingresar")
def agentenosupervisor(request,id_user):


	id = request.user.id
	nivel = AuthUser.objects.get(id=id).nivel.id
	empresa = AuthUser.objects.get(id=id).empresa.id

	
	data = Agentesupervisor.objects.filter(agente__user__id=id_user)

	lista=[]

	for x in data:

		lista.append(x.supervisor.id)


	data = Supervisor.objects.filter(user__empresa__id=empresa).exclude(id__in=lista).values('id','user__first_name').order_by('-id')

	data_dict = ValuesQuerySetToDict(data)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@login_required(login_url="/ingresar")
def carterasupervisor(request,id_user):


	data = Supervisorcartera.objects.filter(supervisor__user__id=id_user).values('id','supervisor__user__first_name','cartera__nombre').order_by('-id')

	data_dict = ValuesQuerySetToDict(data)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@login_required(login_url="/ingresar")
def header(request,id_campania):


	data = Header.objects.filter(campania_id=id_campania).values('id','campania__nombre','statusa','statusb','statusc','statusd','statuse','statusf','statusg','statush').order_by('-id')

	for i in range(len(data)):

		data[i]['statusa'] = data[i]['statusa'].title()
		data[i]['statusb'] = data[i]['statusb'].title()
		data[i]['statusc'] = data[i]['statusc'].title()
		data[i]['statusd'] = data[i]['statusd'].title()
		data[i]['statuse'] = data[i]['statuse'].title()
		data[i]['statusf'] = data[i]['statusf'].title()
		data[i]['statusg'] = data[i]['statusg'].title()
		data[i]['statush'] = data[i]['statush'].title()

	data_dict = ValuesQuerySetToDict(data)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@login_required(login_url="/ingresar")
def agesup(request,id_user):

	data = Agentesupervisor.objects.filter(supervisor__user__id=id_user).values('id','supervisor__user__first_name','supervisor','agente__user__first_name','agente')
	

	for i in range(len(data)):

		data[i]['id'] = data[i]['agente']
	

	data_dict = ValuesQuerySetToDict(data)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@login_required(login_url="/ingresar")
def agentesupervisor(request,id_user):

	id = request.user.id
	nivel = AuthUser.objects.get(id=id).nivel.id
	empresa = AuthUser.objects.get(id=id).empresa.id

	data = Agentesupervisor.objects.filter(agente__user__id=id_user).values('id','supervisor__user__first_name','supervisor')

	data_dict = ValuesQuerySetToDict(data)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@login_required(login_url="/ingresar")
def agregarsupervisor(request):

	id = request.user.id
	nivel = AuthUser.objects.get(id=id).nivel.id
	empresa = AuthUser.objects.get(id=id).empresa.id

	agente = json.loads(request.body)['agente']
	supervisor = json.loads(request.body)['supervisor']

	user = agente['id']

	agente = Agentes.objects.get(user_id=user).id

	supervisor = supervisor['id']

	Agentesupervisor(agente_id=agente,supervisor_id=supervisor).save()

	return HttpResponse('data', content_type="application/json")

@login_required(login_url="/ingresar")
def quitarsupervisor(request):

	id = request.user.id
	nivel = AuthUser.objects.get(id=id).nivel.id
	empresa = AuthUser.objects.get(id=id).empresa.id

	agente = json.loads(request.body)['agente']
	supervisor = json.loads(request.body)['supervisor']



	user = agente['id']

	agente = Agentes.objects.get(user_id=user).id

	supervisor = supervisor['supervisor']


	Agentesupervisor.objects.get(agente_id=agente,supervisor_id=supervisor).delete()

	return HttpResponse('data', content_type="application/json")


@login_required(login_url="/ingresar")
def duracionagente(request,agente):

	
	duracion = AjxProLla.objects.filter(age_codigo=agente).values('age_codigo').annotate(total=Sum('duration'))
	bill = AjxProLla.objects.filter(age_codigo=agente).values('age_codigo').annotate(total=Sum('bill'))

	for b in bill:

		bill = b['total']

	for b in duracion:

		duracion = b['total']

	

	t = int(duracion)-int(bill)

	data = simplejson.dumps(t)


	return HttpResponse(data, content_type="application/json")



@login_required(login_url="/ingresar")
def carteranosupervisor(request,id_user):

	id = request.user.id
	nivel = AuthUser.objects.get(id=id).nivel.id
	empresa = AuthUser.objects.get(id=id).empresa.id

	
	data = Supervisorcartera.objects.filter(supervisor__user__id=id_user)

	lista=[]

	for x in data:

		lista.append(x.cartera.id)

	data = Carteraempresa.objects.filter(empresa_id=empresa).exclude(cartera_id__in=lista).values('id','cartera__nombre','empresa__nombre').order_by('-id')

	data_dict = ValuesQuerySetToDict(data)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@login_required(login_url="/ingresar")
def user(request):

	id = request.user.id

	user = AuthUser.objects.filter(id=id).values('id','username','email','empresa','nivel','first_name','nivel__nombre','empresa__mascaras__tipo','anexo')

	fmt = '%Y-%m-%d %H:%M:%S %Z'

	for i in range(len(user)):

		user[i]['last_login'] = AuthUser.objects.get(id=user[i]['id']).last_login.strftime(fmt)


	data_dict = ValuesQuerySetToDict(user)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")




@login_required(login_url="/ingresar")
def reasignarsupervisor(request):

	if request.method == 'POST':

		id = request.user.id

		data= json.loads(request.body)['dato']


	
		id_supervisor = data['supervisor']

		id_campania = data['id']

		canales = data['canales']

		factor = data['factor']

		discado = data['discado']

		password = data['password']

		campania = Campania.objects.get(id=id_campania)

		campania.supervisor_id = id_supervisor

		campania.factor = factor
		campania.discado = discado
		campania.password = password
		campania.canales = canales

		campania.save()


		data_dict = ValuesQuerySetToDict(data)

		data = simplejson.dumps(data_dict)


	return HttpResponse(data, content_type="application/json")



@login_required(login_url="/ingresar")
def botoneraagente(request,campania):

	agentes = Agentescampanias.objects.filter(campania_id=campania).values('id','agente__user__first_name','campania','agente')

	for i in range(len(agentes)):

		agentes[i]['promesa'] = Base.objects.filter(campania_id=campania,resultado_id=15,agente_id=agentes[i]['agente']).count()
		agentes[i]['directo'] = Base.objects.filter(campania_id=campania,resultado_id=16,agente_id=agentes[i]['agente']).count()
		agentes[i]['indirecto'] = Base.objects.filter(campania_id=campania,resultado_id=17,agente_id=agentes[i]['agente']).count()
		agentes[i]['nocontacto'] = Base.objects.filter(campania_id=campania,resultado_id=18,agente_id=agentes[i]['agente']).count()
		agentes[i]['seleccionar'] = 'no'
		agentes[i]['btnon'] = True
		agentes[i]['btnoff'] = False
	
	data_dict = ValuesQuerySetToDict(agentes)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")



@login_required(login_url="/ingresar")
def agentegrafico(request):

	if request.method == 'POST':

		age = json.loads(request.body)['agentes']
		campania = json.loads(request.body)['campania']


		lista1 = []


		for i in range(len(age)):

			
			s =  age[i]['seleccionar']

			

			if s == True:

				lista1.append(age[i]['agente'])

	

		agentes = Agentescampanias.objects.filter(campania_id=campania).values('id','agente__user__first_name','campania','agente')

		

		for i in range(len(agentes)):

			agentes[i]['promesa'] = Base.objects.filter(campania_id=campania,resultado_id=15,agente_id=agentes[i]['agente']).count()
			agentes[i]['directo'] = Base.objects.filter(campania_id=campania,resultado_id=16,agente_id=agentes[i]['agente']).count()
			agentes[i]['indirecto'] = Base.objects.filter(campania_id=campania,resultado_id=17,agente_id=agentes[i]['agente']).count()
			agentes[i]['nocontacto'] = Base.objects.filter(campania_id=campania,resultado_id=18,agente_id=agentes[i]['agente']).count()
			
		
		data_dict = ValuesQuerySetToDict(agentes)

		data = simplejson.dumps(data_dict)

		return HttpResponse(data, content_type="application/json")




@login_required(login_url="/ingresar")
def botoneragraph(request,campania):


       id = request.user.id
       mascara = AuthUser.objects.get(id=id).empresa.mascaras.id
       total = Base.objects.filter(campania_id=campania).count()
       promesa = Base.objects.filter(resultado_id=15,campania_id=campania).count()
       contactodirecto = Base.objects.filter(resultado_id=16,campania_id=campania).count()
       contactoindirecto = Base.objects.filter(resultado_id=17,campania_id=campania).count()
       nocontacto = Base.objects.filter(resultado_id=18,campania_id=campania).count()
       '''
       fallecido =  Base.objects.filter(resultado_id=1,campania_id=campania).count()
       consultatramite =  Base.objects.filter(resultado_id=2,campania_id=campania).count()
       contactosinpromesa =  Base.objects.filter(resultado_id=3,campania_id=campania).count()
       dificultadpago =  Base.objects.filter(resultado_id=4,campania_id=campania).count()
       acuerdoconfecha =  Base.objects.filter(resultado_id=5,campania_id=campania).count()
       reclamoinstitucion =  Base.objects.filter(resultado_id=6,campania_id=campania).count()
       refinanciaconvenio =  Base.objects.filter(resultado_id=7,campania_id=campania).count()
       renuenterehuye =  Base.objects.filter(resultado_id=8,campania_id=campania).count()
       pagoboucher =  Base.objects.filter(resultado_id=9,campania_id=campania).count()
       desconocidomudado =  Base.objects.filter(resultado_id=10,campania_id=campania).count()
       novivelabora =  Base.objects.filter(resultado_id=11,campania_id=campania).count()
       sivivelabora =  Base.objects.filter(resultado_id=12,campania_id=campania).count()
       '''

       contesta = AjxProLla.objects.filter(cam_codigo=campania,llam_estado=4).count()
       nocontesta = AjxProLla.objects.filter(cam_codigo=campania,llam_estado=3).count()
       buzon = AjxProLla.objects.filter(cam_codigo=campania,llam_estado=5).count()
       congestiondered = AjxProLla.objects.filter(cam_codigo=campania,llam_estado=2).count()
       #asterisk = AjxProLla.objects.filter(cam_codigo=campania,llam_estado__in=[2,3,5]).count()
       pendiente = Base.objects.filter(campania_id=campania).count()-Base.objects.filter(campania_id=campania,proflag=1).count()
       
       if int(total) == 0:

       		total = 0.0001


       if 2 == 2:

               data = {

               		 'total':total,
               		 
               		 #'fallecido':fallecido,
               		 #'consultatramite':consultatramite,
               		 #'contactosinpromesa':contactosinpromesa,
               		 #'dificultadpago':dificultmonitoreo/259/adpago,
               		 #'acuerdoconfecha':acuerdoconfecha,
               		 #'reclamoinstitucion':reclamoinstitucion,
               		 #'refinanciaconvenio':refinanciaconvenio,
               		 #'renuenterehuye':renuenterehuye,
               		 #'pagoboucher':pagoboucher,
               		 #'desconocidomudado':desconocidomudado,
               		 #'novivelabora':novivelabora,
               		 #'sivivelabora':sivivelabora,
               		 
               		 'Promesa':promesa,
                     'Contacto Directo':contactodirecto,
                     'Contacto Indirecto':contactoindirecto,
                     'No Contacto':nocontacto,
       				 'No Contesta':nocontesta,
       				 'Contesta':contesta,
                     'Buzon':buzon,
                     #'Congestion de Red':congestiondered,
                     #'Asterisk':asterisk,
                     'Pendiente':pendiente
                     #'pPromesa':promesa*100/total,
                     #'pDirecto':contactodirecto*100/total,
                     #'pIndirecto':contactoindirecto*100/total,
                     #'pNocontacto':nocontacto*100/total,
                     #'pNocontesta':nocontesta*100/total,
                     #'pBuzon':buzon*100/total,
                     #'pCongestion':promesa*100/total,
                     #'pAsterisk':asterisk*100/total,
                     #'pPendiente':pendiente*100/total

                   
                     }


               data_string = json.dumps(data)

               

       else:

               data_string = 1


       return HttpResponse(data_string, content_type="application/json")

@login_required(login_url="/ingresar")
def busqueda(request):

	if request.method == 'POST':

		data = json.loads(request.body)

		filtro = {}

		for i in data:

			if i == 'telefono':
			
				filtro['telefono']  = data['telefono']

			if i == 'campania':

				filtro['campania']  = data['campania']

			if i == 'cartera':

				filtro['cartera']  = data['cartera']

			if i== 'inicio':

				filtro['inicio']  = data['inicio']

			if i == 'fin':

				filtro['fin']  = data['fin']

			if i=='cliente':

				filtro['cliente']  = data['cliente']

	

	#base = Base.objects.filter(**filtro)


	
	return 'response'


def generacsv(request,cartera,campania,inicio,fin,telefono,cliente):

	

	filtro = {}

	if cartera!='undefined':

		filtro['campania__cartera']=cartera
	if campania!='undefined':

		filtro['campania']=campania
	if inicio!='undefined':

		inicio = datetime.strptime(inicio,'%Y%m%d')

		filtro['fecha__lte'] =inicio

	if fin!='undefined':

		fin = datetime.strptime(fin,'%Y%m%d')

		filtro['fecha__lte'] =fin

	if telefono!='undefined':

		filtro['telefono']=telefono

	if cliente!='undefined':

		filtro['id_cliente']=cliente

	response = HttpResponse(content_type='text/csv')

	ncartera=Campania.objects.get(id=campania).cartera.nombre
	ncampania = Campania.objects.get(id=campania).nombre
	fecha= datetime.now()

	response['Content-Disposition'] = 'attachment; filename="RD_'+str(ncartera)+'_'+str(ncampania)+'_'+str(fecha)[0:19]+'.csv'

	writer = csv.writer(response)

	

	base = Base.objects.filter(**filtro)
	
	writer.writerow(['Id','Telefono','Orden','Cliente','ID Cliente','Cartera','Campania','Agente','Duracion','Monto','Fecha Gestion','Status A','Status B','Status C','Status D','Status E','Status F','Status G','Status H','Botonera','Observacion','Fecha de Pago','Importe de Pago'])

	for x in base:

		x.campania.nombre = x.campania.nombre.encode('ascii','ignore')

		x.campania.nombre = x.campania.nombre.encode('ascii','replace')

		x.monto = x.monto.encode('ascii','ignore')

		x.monto = x.monto.encode('ascii','replace')

		if x.agente:

			agente = x.agente.user.first_name

		else:

			agente = ''

		if x.resultado:

			resultado = x.resultado.name

		else:

			resultado = ''

		duracion = ''

		if x.tiniciogestion and x.tfingestion :

			inicio = x.tiniciogestion
			fin = x.tfingestion
			fmt = '%M:%S'

			duracion = str(fin-inicio)[2:8]

		writer.writerow([x.id,x.telefono,x.orden,x.cliente,x.id_cliente,x.campania.cartera.nombre,x.campania.nombre,agente,duracion,x.monto,x.fecha,x.status_a,x.status_b,x.status_c,x.status_d,x.status_e,x.status_f,x.status_g,x.status_h,resultado,x.detalle,x.fecha,x.monto])


	return response


@login_required(login_url="/ingresar")
def botonera(request):

	if request.method == 'POST':

		id = request.user.id

		id_resultado= json.loads(request.body)['resultado']['id']
		agente= json.loads(request.body)['agente']
		id_base= json.loads(request.body)['cliente']['id']

		

		resultado = Resultado.objects.get(id=id_resultado).name

		base = Base.objects.get(id=id_base)
		base.resultado_id = id_resultado
		base.save()

	
	return HttpResponse(resultado, content_type="application/json")



@login_required(login_url="/ingresar")
def listanegra(request):

	if request.method == 'POST':

		campania =  request.POST['campania']

		filex = request.FILES['process_file']

		Excel(archivo=filex).save()

		id_excel = Excel.objects.all().values('id').order_by('-id')[0]['id']

		archivo = Excel.objects.get(id=id_excel).archivo

		ruta = '/var/www/html/'+str(archivo)

		

		book = xlrd.open_workbook(ruta)

		sh = book.sheet_by_index(0)

		u=[]

		for rx in range(sh.nrows):

			for col in range(sh.ncols):

				

				if rx > 0:

					x = str(sh.row(rx)[col]).replace('text:u','').replace('number:','').replace("'","").replace('.0','').replace('"','')
					
					u.append(x)

					
					
					Listanegra(campania_id=campania,dni=int(x)).save()

		lista = Listanegra.objects.filter(campania_id=campania)

		for l in lista:

			base = Base.objects.filter(id_cliente=l.dni)
			
			for b in base:

				b.blacklist = 1
				b.save()


		return HttpResponseRedirect("/filtros/"+campania)

	



@login_required(login_url="/ingresar")
def colas(request,campania):

	f = datetime.now().date()

	data = AjxProLla.objects.filter(id_ori_seg_cola=campania,f_origen__gte=f).values('age_ip','llam_numero','llam_estado').order_by('-id_ori_llamadas')[:12]

	data_dict = ValuesQuerySetToDict(data)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")



@login_required(login_url="/ingresar")
def calificar(request):

	if request.method == 'POST':
		
		data =json.loads(request.body)

		

		campania = data['campania']
		agente = data['user']['agente']
		llamada = data['user']['idllamada']
		pregunta = data['pregunta']['id']
		respuesta = data['respuesta']

		if Calificacion.objects.filter(campania_id=campania,agente_id=agente,llamada=llamada,preg_exam_id=pregunta):

			'''
			c = Calificacion.objects.get(llamada_id=llamada)
			c.respuesta = respuesta
			c.save()
			'''
			pass
			
		else:

			pass

		Calificacion(preg_exam_id=pregunta,agente_id=agente,campania_id=campania,respuesta=respuesta,llamada=llamada).save()

		return HttpResponse('resultado', content_type="application/json")

@login_required(login_url="/ingresar")
def calificaraudio(request):

	if request.method == 'POST':
		
		data =json.loads(request.body)



	
		campania = data['campania']
		agente = data['agente']['age_codigo']
		llamada = data['user']['id_ori_llamadas']
		pregunta = data['pregunta']['id']
		respuesta = data['respuesta']

		print campania,agente,llamada,pregunta,respuesta


		Calificacion(preg_exam_id=pregunta,agente_id=agente,campania_id=campania,respuesta=respuesta,llamada=llamada).save()

		return HttpResponse('resultado', content_type="application/json")




@login_required(login_url="/ingresar")
def troncales(request):

	id = request.user.id

	troncal = Troncales.objects.all().values('id','nombre')

	data_dict = ValuesQuerySetToDict(troncal)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@login_required(login_url="/ingresar")
def detallesupervisor(request,user):

	supervisor = Supervisor.objects.get(user_id=user).id

	campanias = Campania.objects.filter(supervisor_id=supervisor).values('id','cartera__nombre','nombre','supervisor__user__first_name')

	data_dict = ValuesQuerySetToDict(campanias)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@login_required(login_url="/ingresar")
def detalleagente(request,user):

	agente = Agentes.objects.get(user_id=user).id

	campanias = Agentescampanias.objects.filter(agente_id=agente).values('id','campania__nombre','campania__cartera__nombre','campania__supervisor__user__first_name','agente__user__first_name')

	data_dict = ValuesQuerySetToDict(campanias)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@login_required(login_url="/ingresar")
def filtroscampania(request,campania):

	filtros = Filtro.objects.filter(campania_id=campania).values('campania','id','resultado','campania__nombre','status_f','status_h','status_g','status').order_by('-id')

	for i in range(len(filtros)):

		if filtros[i]['status']==1:

			filtros[i]['estadoname'] = 'Apagado'

		if filtros[i]['status']==0:

			filtros[i]['estadoname'] = 'Activado'

		id_campania = filtros[i]['campania']

		resultado = filtros[i]['resultado']

		resultado =  resultado.split('/')

		status_f = filtros[i]['status_f']

		status_f =  status_f.split('/')

		status_h = filtros[i]['status_h']

		status_h =  status_h.split('/')

		status_g = filtros[i]['status_g']

		status_g =  status_g.split('/')

		resultadonullos = Base.objects.filter(resultado_id__isnull=True,campania_id=id_campania,status_f__in=status_f,status_g__in=status_g,status_h__in=status_h).count()

		resultadototal = Base.objects.filter(resultado__name__in=resultado,campania_id=id_campania,status_f__in=status_f,status_g__in=status_g,status_h__in=status_h).count()+resultadonullos

		resultadobarrido = Base.objects.filter(campania_id=id_campania,status_f__in=status_f,status_g__in=status_g,status_h__in=status_h,proflag=1,resultado__name__in=resultado).count()

		filtros[i]['total'] = resultadototal 

		filtros[i]['fonosporbarrer'] = resultadobarrido


	data_dict = ValuesQuerySetToDict(filtros)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@login_required(login_url="/ingresar")
def nregistrosbase(request):

	id_campania = Campania.objects.all().values('id').order_by('-id')[0]['id']
	base = Base.objects.filter(campania_id=id_campania).count()
	data = simplejson.dumps(base)

	return HttpResponse(data, content_type="application/json")




@login_required(login_url="/ingresar")
def conteofilas(request):

	if request.method == 'POST':

		filex = request.FILES['process_file']

		

		Excel(archivo=filex).save()

		id_excel = Excel.objects.all().values('id').order_by('-id')[0]['id']

		archivo = Excel.objects.get(id=id_excel).archivo

		ruta = '/var/www/html/'+str(archivo)

		book = xlrd.open_workbook(ruta)

		sh = book.sheet_by_index(0)
		
		date =datetime.now()

		data = simplejson.dumps(sh.nrows)

		return HttpResponse(data, content_type="application/json")


@login_required(login_url="/ingresar")
def uploadCampania(request):

	if request.method == 'POST':

		id = request.user.id
		nivel = AuthUser.objects.get(id=id).nivel.id
		empresa = AuthUser.objects.get(id=id).empresa
		data = request.POST
		canales = data['canales']
		cartera = data['cartera']
		inicio = data['inicio']
		fin = data['fin']
		nombre = data['nombre']
		timbrados = data['timbrados']
		llamadaxhora = data['timbrados']
		hombreobjetivo = data['hombreobjetivo']
		mxllamada = data['mxllamada']
		supervisor = data['supervisor']
		tgestion = data['tgestion']
		now = datetime.now()
		archivo =  request.FILES['process_file']
		password = data['password']
		discado = data['discado']
		factor = data['factor']

		Campania(password=password,discado=discado,factor=factor,tgestion=tgestion,cartera_id=cartera,supervisor_id=supervisor,usuario_id=id,fecha_cargada= now,archivo = archivo,canales=canales,htinicio=inicio,htfin=fin,nombre=nombre,timbrados=timbrados,llamadaxhora=llamadaxhora,hombreobjetivo=hombreobjetivo,mxllamada=mxllamada).save()

		id_campania = Campania.objects.all().values('id').order_by('-id')[0]['id']

		archivo  = Campania.objects.get(id=id_campania).archivo

		xls_name = '/var/www/html/'+str(archivo)

		a ={}

		book = xlrd.open_workbook(xls_name)

		sh = book.sheet_by_index(0)
		
		date =datetime.now()

		

		for rx in range(sh.nrows):

			if rx == 0:

				for col in range(sh.ncols):

					a[col] = str(sh.row(rx)[col])

					a[col] = a[col].split(':')

					a[col]= a[col][1][0:150]

					a[col] = a[col].replace("u'","")

					a[col] = a[col].replace("'","")

				telefono = a[0]
				orden = a[1]
				cliente = a[2]
				id_cliente = a[3]
				status_a = a[4]
				status_b = a[5]
				status_c = a[6]
				status_d =a[7]
				status_e= a[8]
				status_f=a[9]
				status_g= a[10]
				status_h = a[11]

				Header(campania_id=id_campania,statusa=status_a,statusb=status_b,statusc=status_c,statusd=status_d,statuse=status_e,statusf=status_f,statusg=status_g,statush=status_h).save()

			else:

				for col in range(sh.ncols):

					a[col] = str(sh.row(rx)[col])

					a[col] = a[col].split(':')

					a[col]= a[col][1][0:150]

					a[col] = a[col].replace("u","").replace('"','').replace("'","")



				telefono = int(a[0].replace('.0',''))
				orden = int(a[1].replace('.0',''))
				cliente = a[2]
				id_cliente = a[3]
				status_a = a[4]
				status_b = a[5]
				status_c = a[6]
				status_d =a[7]
				status_e= a[8]
				status_f=a[9]
				status_g= a[10]
				status_h = a[11]

				'''

				telefono = a[0].replace('.0','')
				orden = a[1]
				cliente = a[2]
				id_cliente = a[3]
				status_a = a[4].replace('.0','')
				status_b = a[5].replace('.0','')
				status_c = a[6].replace('.0','')
				status_d =a[7].replace('.0','')
				status_e= a[8].replace(".0","")
				status_f=a[9].replace('.0','')
				status_g= a[10].replace('.0','')
				status_h = a[11].replace('.0','')
				'''

				Base(campania_id=id_campania,telefono=telefono,orden=orden,cliente=cliente,id_cliente=id_cliente,status_a=status_a,status_b=status_b,status_c=status_c,status_d=status_d,status_e=status_e,status_f=status_f,status_g=status_g,status_h=status_h,blacklist=0).save()

				time.sleep(.002)
		
		data = simplejson.dumps(id_campania)

		return HttpResponse(data, content_type="application/json")


@login_required(login_url="/ingresar")
def campanias(request):

	if request.method == 'GET':

		id = request.user.id
		nivel = AuthUser.objects.get(id=id).nivel.id
		empresa = AuthUser.objects.get(id=id).empresa

		if nivel == 4: #Manager

			data = Campania.objects.all().values('cartera__nombre','password','id','usuario__first_name','estado','nombre','troncal','canales','timbrados','mxllamada','llamadaxhora','hombreobjetivo','supervisor__user__first_name','supervisor__user__empresa__nombre','supervisor').order_by('-id')
		
		if nivel == 2: #Supervisores
			
			supervisor = Supervisor.objects.get(user=id).id

			data = Campania.objects.filter(supervisor=supervisor).values('cartera__nombre','password','id','usuario__first_name','estado','nombre','troncal','canales','timbrados','mxllamada','llamadaxhora','hombreobjetivo','supervisor__user__first_name','factor','discado','supervisor').order_by('-id')

		if nivel == 1: #Admin

			data = Campania.objects.filter(usuario__empresa=empresa).values('cartera__nombre','password','id','usuario__first_name','estado','nombre','troncal','canales','timbrados','mxllamada','llamadaxhora','hombreobjetivo','supervisor__user__first_name','factor','discado','supervisor').order_by('-id')

		if nivel == 5: #Monitor

			data = Campania.objects.filter(usuario__empresa=empresa).values('cartera__nombre','password','id','usuario__first_name','estado','nombre','troncal','canales','timbrados','mxllamada','llamadaxhora','hombreobjetivo','supervisor__user__first_name','supervisor').order_by('-id')

		fmt = '%H:%M:%S %Z'
		fmt1 = '%Y-%m-%d %H:%M:%S %Z'

		for i in range(len(data)):

			data[i]['htinicio'] = Campania.objects.get(id=data[i]['id']).htinicio.strftime(fmt)
			data[i]['hfin'] = Campania.objects.get(id=data[i]['id']).htfin.strftime(fmt)
			data[i]['fecha_cargada'] = Campania.objects.get(id=data[i]['id']).fecha_cargada.strftime(fmt1)
			data[i]['totalagentes'] = Agentescampanias.objects.filter(campania_id=data[i]['id']).count()
			data[i]['conectados'] = Agentescampanias.objects.filter(campania_id=data[i]['id']).exclude(agente__estado=1).count()
			data[i]['cargados'] = Base.objects.filter(campania_id=data[i]['id']).count()
			data[i]['barridos'] = Base.objects.filter(campania_id=data[i]['id'],proflag=1).count()
			data[i]['errados'] = AjxProLla.objects.filter(cam_codigo=data[i]['id'],llam_estado=2).count()
			data[i]['filtro'] = '1'
			data[i]['a'] = True
			data[i]['b'] = False

			total = Filtro.objects.filter(campania_id=data[i]['id']).count()
	
			apagado = Filtro.objects.filter(campania_id=data[i]['id'],status=1).count()
			activado = Filtro.objects.filter(campania_id=data[i]['id'],status=0).count()
			
			#0 Iniciado
			#1 Apagado


			if activado > 0:
				data[i]['estado'] = ''
				data[i]['color'] = '#5C93B5'
				data[i]['font'] = '#fff'

			if apagado == total:
				data[i]['estado'] = ''
				data[i]['color'] = '#fff'
				data[i]['font'] = '#000'

			

			if total == 0:
				data[i]['estado'] = ''
				data[i]['color'] = '#fff'
				data[i]['font'] = '#000'

			

			#Apagado = F58C48

	
		data_dict = ValuesQuerySetToDict(data)

		data = simplejson.dumps(data_dict)

		return HttpResponse(data, content_type="application/json")

	if request.method == 'POST':

		data= json.loads(request.body)['dato']

		Campania.objects.get(id=data['id']).delete()

		return HttpResponse(data, content_type="application/json")




@login_required(login_url="/ingresar")
def nivel(request):

	id = request.user.id

	nivel = AuthUser.objects.get(id=id).nivel.id

	if nivel == 4: #Manager

		nivel = Nivel.objects.all().exclude(id__in=[2,3]).values('id','nombre')


	if nivel == 2: #Supervisores

		nivel = Nivel.objects.all().values('id','nombre')[2:3]


	if nivel == 1: #Admin

		nivel =  Nivel.objects.all().exclude(id=4).values('id','nombre')[1:5]


	if nivel == 5: #Monitor

		nivel =  Nivel.objects.all().exclude(id=4).values('id','nombre')[1:5]



	data_dict = ValuesQuerySetToDict(nivel)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


def status_f(request,id_campania):

	id = request.user.id

	empresa = AuthUser.objects.get(id=id).empresa.id

	status_f = Base.objects.filter(campania_id=id_campania).values('status_f').annotate(total=Count('status_f'))

	data_dict = ValuesQuerySetToDict(status_f)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@login_required(login_url="/ingresar")
def status_g(request,id_campania):

	id = request.user.id

	empresa = AuthUser.objects.get(id=id).empresa.id

	status_g = Base.objects.filter(campania_id=id_campania).values('status_g').annotate(total=Count('status_g'))

	data_dict = ValuesQuerySetToDict(status_g)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@login_required(login_url="/ingresar")
def status_h(request,id_campania):

	id = request.user.id

	empresa = AuthUser.objects.get(id=id).empresa.id

	status_h = Base.objects.filter(campania_id=id_campania).values('status_h').annotate(total=Count('status_h'))

	data_dict = ValuesQuerySetToDict(status_h)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@login_required(login_url="/ingresar")
def agentesdisponibles(request,id_campania):


	id = Campania.objects.get(id=id_campania).supervisor.user.id

	agentescampania = Agentescampanias.objects.filter(campania=id_campania)

	data = Agentesupervisor.objects.filter(supervisor__user__id=id)

	lista1 = []

	for x in data:

		lista1.append(x.agente.id)

	lista2 = []

	for a in agentescampania:

		lista2.append(a.agente.id) 	

	agentes = Agentes.objects.filter(id__in=lista1).exclude(id__in=lista2).values('id')

	for i in range(len(agentes)):

		agentes[i]['name'] = Agentes.objects.get(id=agentes[i]['id']).user.first_name
		agentes[i]['estado'] = Agentes.objects.get(id=agentes[i]['id']).estado.nombre
		agentes[i]['agente'] = agentes[i]['id']

	data_dict = ValuesQuerySetToDict(agentes)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@login_required(login_url="/ingresar")
def agentescampania(request,id_campania):

	id = request.user.id

	agentes = Agentescampanias.objects.filter(campania=id_campania).values('id','agente','campania__nombre','campania__cartera__nombre','campania__supervisor__user__first_name')

	for i in range(len(agentes)):

		agentes[i]['name'] = Agentescampanias.objects.get(id=agentes[i]['id']).agente.user.first_name

		agentes[i]['estado'] = Agentescampanias.objects.get(id=agentes[i]['id']).agente.estado.nombre


	data_dict = ValuesQuerySetToDict(agentes)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")



@login_required(login_url="/ingresar")
def agregaragente(request):

	if request.method == 'POST':

		data= json.loads(request.body)['dato']

		campania = json.loads(request.body)['campania'] 

		for data in data:

			id_agente = data['agente']

			Agentescampanias(agente_id=id_agente,campania_id=campania).save()

		return HttpResponse('data', content_type="application/json")


@login_required(login_url="/ingresar")
def quitaragente(request):

	if request.method == 'POST':

		data= json.loads(request.body)['dato']

		campania = json.loads(request.body)['campania']

		for data in data:

			id_agente = data['agente']

			agente = Agentes.objects.get(id=id_agente)

			Agentescampanias.objects.filter(agente=agente.id,campania=campania).delete()

		return HttpResponse(agente.user.first_name, content_type="application/json")


@login_required(login_url="/ingresar")
def supervisores(request):

	id = request.user.id

	nivel = AuthUser.objects.get(id=id).nivel.id

	empresa = AuthUser.objects.get(id=id).empresa.id

	if nivel == 2:

		supervisores = Supervisor.objects.filter(user=id).values('id','user__first_name','user')

	if nivel == 1:

		supervisores = Supervisor.objects.filter(user__empresa__id=empresa).values('id','user__first_name','user')

	if nivel == 4:

		supervisores = Supervisor.objects.all().values('id','user__first_name','user')

	if nivel == 5:

		supervisores = Supervisor.objects.filter(user__empresa__id=empresa).values('id','user__first_name','user')


	data = json.dumps(ValuesQuerySetToDict(supervisores))

	return HttpResponse(data, content_type="application/json")



@login_required(login_url="/ingresar")
def usuarios(request):

	id = request.user.id

	nivel = AuthUser.objects.get(id=id).nivel.id

	empresa = AuthUser.objects.get(id=id).empresa

	if nivel == 4: #Manager

		usuarios = AuthUser.objects.all().values('nivel','anexo','id','telefono','username','email','empresa__nombre','nivel__nombre','first_name').order_by('-id')
	
	if nivel == 3: #Agentes

		usuarios = AuthUser.objects.filter(id=id).values('nivel','anexo','id','telefono','username','email','empresa__nombre','nivel__nombre','first_name').order_by('-id')

	if nivel == 2: #Supervisores

		supervisor = Supervisor.objects.get(user=id).id

		usuarios = AuthUser.objects.filter(empresa_id=empresa).values('nivel','anexo','id','telefono','username','email','empresa__nombre','nivel__nombre','first_name').order_by('-id')

	if nivel == 1: #Admin

		usuarios = AuthUser.objects.filter(empresa_id=empresa).exclude(nivel=4).values('nivel','anexo','id','telefono','username','email','empresa__nombre','nivel__nombre','first_name').order_by('-id')

	if nivel == 5: #Admin

		usuarios = AuthUser.objects.filter(empresa_id=empresa).exclude(nivel=4).values('nivel','anexo','id','telefono','username','email','empresa__nombre','nivel__nombre','first_name').order_by('-id')


	data = json.dumps(ValuesQuerySetToDict(usuarios))

	if request.method == 'POST':

		tipo = json.loads(request.body)['add']

		data = json.loads(request.body)['dato']

		
		telefono = None

		supi = False
		carti = False

		if tipo == "New":

			for d in data:

				if d == 'telefono':

					telefono = data['telefono']

				if d == 'supervisor':

					supi = True

				if d == 'cartera':

					carti = True



			
			username = data['username']
					
			if nivel == 4:
			
				empresa = data['empresa']
			else:
				empresa = empresa.id

			
		
			nivel = data['nivel']
			password = data['password']
			
			nombre=data['nombre']


			users = User.objects.all()

			e = 1

			for users in users:

				if username == users.username:

					info = username +' este usuario ya existe, escoja otro pofavor'
					e = 0

			
			if e == 1:

				user = User.objects.create_user(username=username,password=password)

				user.save()

				id_user = AuthUser.objects.all().values('id').order_by('-id')[0]['id']

				usuario = AuthUser.objects.get(id=id_user)
				usuario.empresa_id = empresa
				usuario.nivel_id = nivel
				usuario.first_name = nombre
				usuario.anexo = data['anexo']
				usuario.telefono = telefono
				usuario.save()

				info = 'Usuario ' + usuario.first_name + ' ingresado al sistema, gracias'

				if nivel == 2: #Asignacion de carteras al supervisor

					supi = Supervisor(user_id=id_user).save()

					id_sup = Supervisor.objects.all().values('id').order_by('-id')[0]['id']

					if carti:

						for i in data['cartera']:

							


							id_cartera = Carteraempresa.objects.get(cartera__nombre=i['cartera__nombre'],empresa_id=empresa).cartera.id

							Supervisorcartera(cartera_id=id_cartera,supervisor_id=id_sup).save()

		
				if nivel == 3: # Usuario Agente

					
					Agentes(user_id=id_user).save()
					agente =Agentes.objects.get(user=id_user)
					agente.atendidas = 0
					agente.contactadas =0

				
					agente.anexo = data['anexo']
					agente.estado_id = 1
					#agente.tiempo = datetime.strptime("00:00:00", "%H:%M:%S")
					agente.save()

					id_age = Agentes.objects.all().values('id').order_by('-id')[0]['id']

					if supi:

						for i in data['supervisor']:

							

							supervisor = Supervisor.objects.get(user__first_name=i['user__first_name']).id

							Agentesupervisor(agente_id=id_age,supervisor_id=supervisor).save()


			return HttpResponse(info, content_type="application/json")


		if tipo=="Edit":

			id= data['id']

			


			

			user = AuthUser.objects.get(id=id)

			nivelid = user.nivel.id
			user.username =data['username']
			user.first_name =data['first_name']
			user.telefono = data['telefono']
			user.anexo = data['anexo']
			user.save()

			if nivelid == 3:

				

				agente = Agentes.objects.get(user_id=id)
				agente.anexo = data['anexo']
				agente.save()

				


		if tipo=="Eliminar":

			id= data['id']

		
			if data['nivel__nombre']=='Supervisor':

				if Supervisor.objects.filter(user_id=id):

					Supervisor.objects.get(user_id=id).delete()

			if data['nivel__nombre']=='Agente':

				if Agentes.objects.filter(user_id=id):

					Agentes.objects.get(user_id=id).delete()

			User.objects.get(id=id).delete()



		return HttpResponse(data['username'], content_type="application/json")


	return HttpResponse(data, content_type="application/json")

@login_required(login_url="/ingresar")
def empresas(request):

	id = request.user.id

	nivel = AuthUser.objects.get(id=id).nivel.id

	if nivel == 4:

		empresas = Empresa.objects.all().values('id','nombre','licencias','mascaras__tipo','telefono','contacto','mail','url').order_by('-id')

	else:

		empresa = AuthUser.objects.get(id=id).empresa.id

		empresas = Empresa.objects.filter(id=empresa).values('id','nombre','licencias','mascaras__tipo','telefono','contacto','mail','url').order_by('-id')

	data = json.dumps(ValuesQuerySetToDict(empresas))

	if request.method == 'POST':

		tipo = json.loads(request.body)['add']

		data = json.loads(request.body)['dato']

		if tipo == "New":

			nombre = data['nombre']
			contacto = data['contacto']
			mail = data['mail']
			licencias = data['licencias']
			if data['mascara']==2:
				url =data['url']
			else:
				url=""
			
			telefono = data['telefono']
			mascara = data['mascara']

	

			Empresa(mascaras_id=mascara,nombre=nombre,contacto=contacto,mail=mail,licencias=licencias,telefono=telefono,url=url).save()

			return HttpResponse(nombre, content_type="application/json")


		if tipo=="Edit":

			id= data['id']

	

			empresa = Empresa.objects.get(id=id)
			empresa.nombre =data['nombre']
			empresa.contacto =data['contacto']
			empresa.mail =data['mail']
			empresa.licencias =data['licencias']
			empresa.mascaras_id =data['mascaras__tipo']
			if data['mascaras__tipo']==2:
				empresa.url =data['url']

			

			empresa.telefono =data['telefono']
			empresa.save()


		if tipo=="Eliminar":

			id= data['id']

			

			Empresa.objects.get(id=id).delete()

	


		return HttpResponse(data['nombre'], content_type="application/json")


	return HttpResponse(data, content_type="application/json")



@login_required(login_url="/ingresar")
def salir(request):

	
	id =request.user.id
	nivel = AuthUser.objects.get(id=id).nivel.id
	
	if nivel == 3:
		agente = Agentes.objects.get(user=id)
		agente.estado_id=1
		agente.est_ag_predictivo = 0
		agente.save()
		Estadocambio(user_id=id,estado_id=1).save()

	logout(request)
	
	return HttpResponseRedirect("/ingresar")


def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]







