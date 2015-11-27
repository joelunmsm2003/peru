from django.shortcuts import *
from django.template import RequestContext
from django.contrib.auth import *
from django.contrib.auth.models import Group, User
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.core.urlresolvers import reverse
from django.db.models import Max,Count
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from PeruCall.models import *

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

import xlrd
import json 
import csv
import simplejson
import xlwt
import requests
import os

from datetime import datetime,date
from django.contrib.auth import authenticate

def ingresar(request):

	if request.user.is_authenticated():

		return HttpResponseRedirect("/empresa")

	else:

		if request.method == 'POST':

			print request.POST

			user = request.POST['user']
			
			psw = request.POST['password']

			user = authenticate(username=user, password=psw)

		
			if user is not None:

				if user.is_active:

					login(request, user)

					nivel = AuthUser.objects.get(username=user).nivel.id

					

					print nivel

					if nivel == 1:

						return HttpResponseRedirect("/empresa")

					if nivel == 2:

						return HttpResponseRedirect("/empresa")

					if nivel == 3:

						id_agente= Agentes.objects.get(user_id=user).id

						return HttpResponseRedirect("/teleoperador/"+str(id_agente))

					if nivel == 4:

						return HttpResponseRedirect("/empresa")



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

@login_required(login_url="/ingresar")
def teleoperador(request,id):
	return render(request, 'teleoperador.html',{})

@login_required(login_url="/ingresar")
def empresa(request):
	return render(request, 'empresa.html',{})

@login_required(login_url="/ingresar")
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

	
	return render(request, 'campania.html',{'supervisor':supervisor,'troncales':troncales,'cartera':cartera})



@login_required(login_url="/ingresar")
def filtros(request,id):
	campania = Campania.objects.get(id=id)
	return render(request, 'filtros.html',{'campania':campania})

@login_required(login_url="/ingresar")
def cartera(request):
	
	return render(request, 'cartera.html',{})

@login_required(login_url="/ingresar")
def supervisorcartera(request,id_supervisor):
	
	return render(request, 'carterasupervisor.html',{})

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

	user = Agentescampanias.objects.filter(campania=id_campania).values('id','agente','agente__user__first_name','agente__fono','agente__anexo','agente__atendidas','agente__contactadas','agente__estado')

	fmt = '%Y-%m-%d %H:%M:%S %Z'
	fmt1 = '%Y-%m-%d %H:%M:%S'
	fmt2='%H:%M:%S'

	for i in range(len(user)):

		agentebase = Agentebase.objects.filter(agente_id=user[i]['agente'],status_id=6)

		for agente in agentebase:

			tiniciogestion = agente.tiniciogestion

			ti= str(tiniciogestion)[0:19]
			tf= str(datetime.now())[0:19]

			ti = datetime.strptime(ti,fmt1)
			tf = datetime.strptime(tf,fmt1)

			user[i]['tgestion'] = str(tf-ti)

			sec = str(tf-ti).split(':')
			print 'sec',sec[2]

			user[i]['secgestion'] = sec[2]

			if sec[2] > 0 and sec[2]< 30:
				user[i]['color'] = '#81C784'
			if sec[2] > 30 and sec[2]< 55:
				user[i]['color'] = '#2196F3'
			if sec[2] > 55 :
				user[i]['color'] = '#EF5350'




		user[i]['agente__tiempo'] = Agentescampanias.objects.get(id=user[i]['id']).agente.tiempo.strftime(fmt)
		
		if user[i]['agente__atendidas'] > 0:

			user[i]['performance'] =  (user[i]['agente__contactadas']*100/user[i]['agente__atendidas'])

			print 'performance',user[i]['performance']

		else:

			user[i]['performance'] = 0

	data_dict = ValuesQuerySetToDict(user)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")



@login_required(login_url="/ingresar")
def agregarcartera(request):

	if request.method == 'POST':


		data= json.loads(request.body)['dato']
		user=json.loads(request.body)['user']

		print data
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

		id_cliente = cliente['id']
		base = Agentebase.objects.get(base_id=id_cliente,agente_id=id_agente)
		base.tiniciogestion = fecha
		base.save()

		return HttpResponse('data', content_type="application/json")

@login_required(login_url="/ingresar")
def gestionupdate(request):


	if request.method == 'POST':

		gestion = json.loads(request.body)['gestion']
		agente = json.loads(request.body)['agente']
		cliente = json.loads(request.body)['cliente']['id']

		print cliente

		comentario = gestion['comentario']

		print 'gestion',gestion

		print len(gestion)

		if len(gestion)>1:

			if gestion['fecha']:
				fecha = gestion['fecha']
			if gestion['monto']:
				monto = gestion['monto']

			base = Agentebase.objects.get(base_id=cliente,agente_id=agente)
			base.facuerdo = fecha
			base.macuerdo = monto
			base.save()



		base = Agentebase.objects.get(base_id=cliente,agente_id=agente)
		base.comentario = comentario
		base.save()

		

		return HttpResponse('data', content_type="application/json")




@login_required(login_url="/ingresar")
def tgestion(request,id_base,id_agente):


	agentebase = Agentebase.objects.get(base_id=id_base,agente_id=id_agente)

	fecha = agentebase.tiniciogestion

	ti= str(fecha)[0:19]
	tf= str(datetime.now())[0:19]

	fmt = '%Y-%m-%d %H:%M:%S'

	ti = datetime.strptime(ti,fmt)
	tf = datetime.strptime(tf,fmt)

	return HttpResponse(tf-ti, content_type="application/json")

	
@login_required(login_url="/ingresar")
def agregarfiltro(request):

	if request.method == 'POST':

		grupo= json.loads(request.body)['grupo']
		ciudad= json.loads(request.body)['ciudad']
		segmento= json.loads(request.body)['segmento']
		campania = json.loads(request.body)['campania']
		resultado = json.loads(request.body)['resultado']

		ciudadt = ""
		grupot = ""
		segmentot = ""
		resultadot = ""

		for i in range(len(resultado)):

			print resultado[i]['name']

			resultadot = resultadot  + resultado[i]['name'] +'/'

		for i in range(len(ciudad)):

			print ciudad[i]['status_f']

			ciudadt = ciudadt  + ciudad[i]['status_f'] +'/'

		for i in range(len(grupo)):

			print grupo[i]['status_g']

			grupot = grupot  + grupo[i]['status_g'] +'/'

		for i in range(len(segmento)):

			print segmento[i]['status_h']

			segmentot = segmentot  + segmento[i]['status_h'] +'/'
  

		Filtro(resultado = resultadot,ciudad=ciudadt,grupo=grupot,segmento=segmentot,campania_id=campania).save()

	
		return HttpResponse('data', content_type="application/json")

@login_required(login_url="/ingresar")
def eliminarfiltro(request):

	if request.method == 'POST':

		id_filtro= json.loads(request.body)['dato']['id']

		Filtro.objects.get(id=id_filtro).delete()

		print dato

		return HttpResponse(id_filtro, content_type="application/json")



@login_required(login_url="/ingresar")
def resultado(request):

		data = Resultado.objects.all().values('id','name','tipo','codigo').order_by('-id')

		data_dict = ValuesQuerySetToDict(data)

		data = simplejson.dumps(data_dict)

		return HttpResponse(data, content_type="application/json")


@login_required(login_url="/ingresar")
def agente(request,id_agente):

	data = Agentes.objects.filter(id=id_agente).values('id','anexo','fono','atendidas','contactadas','estado__nombre','user__first_name','supervisor','calificacion').order_by('-id')

	#for i in range(len(data)):

		#data[i]['media'] = data[i]['contactadas']*100/data[i]['atendidas']

	data_dict = ValuesQuerySetToDict(data)

	data = simplejson.dumps(data_dict)

	atendidas = Base.objects.filter(agente_id=id_agente,status=1).count()

	acuerdos = Base.objects.filter(agente_id=id_agente,resultado_id__in=[4,1,2]).count()

	data = {'data':data,'atendidas':atendidas,'acuerdos':acuerdos,'media':3}

	data = simplejson.dumps(data)

	return HttpResponse(data, content_type="application/json")



@login_required(login_url="/ingresar")
def cliente(request,id_agente):

	
		base = Base.objects.filter(agente_id=id_agente,status=1).values('id','telefono','orden','cliente','id_cliente','status_a','status_b','status_c','status_d','status_e','status_f','status_g','status_h','status','campania__nombre','resultado__name')

		data_dict = ValuesQuerySetToDict(base)

		data = simplejson.dumps(data_dict)

		return HttpResponse(data, content_type="application/json")


@login_required(login_url="/ingresar")
def atendida(request,id_agente):
		
		cantidad = Base.objects.filter(agente_id=id_agente).values('agente').annotate(total=Sum('duracion'))
		num=int(cantidad[0]['total'])  
		hor=(int(num/3600))  
		minu=int((num-(hor*3600))/60)  
		seg=num-((hor*3600)+(minu*60))  
		
		print minu

		atendida = str(hor)+":"+str(minu)+":"+str(seg)

		if minu < 10:

			atendida = str(hor)+":0"+str(minu)+":"+str(seg)

		if seg < 10:

			atendida = str(hor)+":"+str(minu)+"0:"+str(seg)

		if seg < 10 or minu < 10 :

			atendida = str(hor)+":0"+str(minu)+":0"+str(seg)


		


		return HttpResponse(atendida, content_type="application/json")


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

		
		cantidad = Base.objects.filter(agente_id=id_agente).values('agente').annotate(total=Sum('duracion'))
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
def resultadofiltro(request,id_filtro):

		filtro = Filtro.objects.get(id=id_filtro)

		resultado = filtro.resultado

		resultado =  resultado.split('/')

		status_f = filtro.ciudad

		status_f =  status_f.split('/')
		
		status_h = filtro.segmento

		status_h =  status_h.split('/')

		status_g = filtro.grupo

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

			data = Carteraempresa.objects.filter(empresa_id=empresa).values('id','cartera__nombre','empresa__nombre').order_by('-id')

		if nivel == 2:

			data =Supervisorcartera.objects.filter(supervisor__user__id=id).values('id','cartera__nombre')


		if nivel == 3:

			data = Carteraempresa.objects.filter(empresa_id=empresa).values('id','cartera__nombre','empresa__nombre').order_by('-id')

		if nivel == 4:

			data = Carteraempresa.objects.all().values('id','cartera__nombre','empresa__nombre').order_by('-id')



		data_dict = ValuesQuerySetToDict(data)

		data = simplejson.dumps(data_dict)

		return HttpResponse(data, content_type="application/json")

	if request.method == 'POST':

		data= json.loads(request.body)['dato']
		tipo= json.loads(request.body)['add']

		if tipo == 'New':

			Cartera(nombre=data['cartera']).save()

			id_cartera = Cartera.objects.all().values('id').order_by('-id')[0]['id']


			Carteraempresa(cartera_id=id_cartera,empresa_id=empresa).save()

			data = Cartera.objects.get(id=id_cartera)

			return HttpResponse(data.nombre, content_type="application/json")

		if tipo == 'Edit':

			print data

			id_cartera = data['id']
			cartera = Carteraempresa.objects.get(id=id_cartera).cartera.id
			cartera = Cartera.objects.get(id=cartera)
			cartera.nombre = data['cartera__nombre']
			cartera.save()

			return HttpResponse(cartera.nombre, content_type="application/json")

		if tipo == 'Eliminar':

			print data

			id_cartera = data['id']
			cartera = Carteraempresa.objects.get(id=id_cartera)
			
			cartera.delete()

			return HttpResponse('cartera.nombre', content_type="application/json")





@login_required(login_url="/ingresar")
def listafiltros(request,id_campania):


	data = Filtro.objects.filter(campania_id=id_campania).values('id','ciudad','segmento','grupo','resultado').order_by('-id')

	for i in range(len(data)):

		print data[i]['id']

		filtro = Filtro.objects.get(id=data[i]['id'])

		resultado = filtro.resultado

		resultado =  resultado.split('/')

		status_f = filtro.ciudad

		status_f =  status_f.split('/')

		status_h = filtro.segmento

		status_h =  status_h.split('/')

		status_g = filtro.grupo

		status_g =  status_g.split('/')

		resultadototal = Base.objects.filter(campania_id=id_campania,resultado__name__in=resultado,status_f__in=status_f,status_g__in=status_g,status_h__in=status_h).count()

		resultadobarrido = Base.objects.filter(campania_id=id_campania,resultado__name__in=resultado,status_f__in=status_f,status_g__in=status_g,status_h__in=status_h,status=1).count()

		fonosinexito = Base.objects.filter(campania_id=id_campania,resultado__name__in=resultado,status_f__in=status_f,status_g__in=status_g,status_h__in=status_h,status=2).count()

		data[i]['total'] = resultadototal 
		data[i]['fonosporbarrer'] = resultadototal - resultadobarrido
		data[i]['fonosinexito'] = fonosinexito


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
def carteranosupervisor(request,id_user):

	id = request.user.id
	nivel = AuthUser.objects.get(id=id).nivel.id
	empresa = AuthUser.objects.get(id=id).empresa.id

	
	data = Supervisorcartera.objects.filter(supervisor__user__id=id_user)

	lista=[]

	for x in data:

		lista.append(x.cartera.id)

	print lista

	

	data = Carteraempresa.objects.filter(empresa_id=empresa).exclude(cartera_id__in=lista).values('id','cartera__nombre','empresa__nombre').order_by('-id')

	data_dict = ValuesQuerySetToDict(data)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@login_required(login_url="/ingresar")
def user(request):

	id = request.user.id

	user = AuthUser.objects.filter(id=id).values('id','username','email','empresa','nivel','first_name','nivel__nombre')

	fmt = '%Y-%m-%d %H:%M:%S %Z'

	for i in range(len(user)):

		user[i]['last_login'] = AuthUser.objects.get(id=user[i]['id']).last_login.strftime(fmt)

		datex = AuthUser.objects.get(id=user[i]['id']).last_login
	
		a = datetime(datex.year,datex.month,datex.day,datex.hour,datex.minute,datex.second)

		b = datetime.now()
		
		user[i]['conectado'] = str(b - a)[0:7]


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

		campania = Campania.objects.get(id=id_campania)

		print campania.nombre

		campania.supervisor_id = id_supervisor
		campania.save()


		data_dict = ValuesQuerySetToDict(data)

		data = simplejson.dumps(data_dict)


	return HttpResponse(data, content_type="application/json")


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
def troncales(request):

	id = request.user.id

	troncal = Troncales.objects.all().values('id','nombre')

	data_dict = ValuesQuerySetToDict(troncal)

	data = simplejson.dumps(data_dict)

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
		cartera = Cartera.objects.get(nombre=cartera).id
		inicio = data['inicio']
		fin = data['fin']
		nombre = data['nombre']
		timbrados = data['timbrados']
		llamadaxhora = data['timbrados']
		hombreobjetivo = data['hombreobjetivo']
		mxllamada = data['mxllamada']
		supervisor = data['supervisor']
		now = datetime.now()
		archivo =  request.FILES['process_file']

		Campania(cartera_id=cartera,supervisor_id=supervisor,usuario_id=id,fecha_cargada= now,archivo = archivo,canales=canales,htinicio=inicio,htfin=fin,nombre=nombre,timbrados=timbrados,llamadaxhora=llamadaxhora,hombreobjetivo=hombreobjetivo,mxllamada=mxllamada).save()

		id_campania = Campania.objects.all().values('id').order_by('-id')[0]['id']

		archivo  = Campania.objects.get(id=id_campania).archivo


		xls_name = '/var/www/html/'+str(archivo)

		print xls_name

		
		
		a ={}

		book = xlrd.open_workbook(xls_name)

		sh = book.sheet_by_index(0)
		
		date =datetime.now()

		for rx in range(sh.nrows):

			for col in range(sh.ncols):

				a[col] = str(sh.row(rx)[col])

				a[col] = a[col].split(':')

				a[col]= a[col][1][0:150]

				a[col] = a[col].replace("u'","")

				a[col] = a[col].replace("'","")

			telefono = a[0].replace(".0","")
			orden = a[1].replace(".0","")
			cliente = a[2]
			id_cliente = a[3]
			status_a = a[4]
			status_b = a[5]
			status_c = a[6]
			status_d =a[7]
			status_e= a[8].replace(".0","")
			status_f=a[9]
			status_g= a[10]
			status_h = a[11]

			Base(resultado_id=7,campania_id=id_campania,telefono=telefono,orden=orden,cliente=cliente,id_cliente=id_cliente,status_a=status_a,status_b=status_b,status_c=status_c,status_d=status_d,status_e=status_e,status_f=status_f,status_g=status_g,status_h=status_h).save()

	return HttpResponseRedirect("/adminCampania/"+str(id_campania))


@login_required(login_url="/ingresar")
def campanias(request):

	id = request.user.id
	nivel = AuthUser.objects.get(id=id).nivel.id
	empresa = AuthUser.objects.get(id=id).empresa

	if nivel == 4: #Manager

		data = Campania.objects.all().values('id','usuario__first_name','estado','nombre','troncal','canales','timbrados','mxllamada','llamadaxhora','hombreobjetivo','supervisor__user__first_name').order_by('-id')
	
	if nivel == 2: #Supervisores
		
		supervisor = Supervisor.objects.get(user=id).id

		data = Campania.objects.filter(supervisor=supervisor).values('id','usuario__first_name','estado','nombre','troncal','canales','timbrados','mxllamada','llamadaxhora','hombreobjetivo','supervisor__user__first_name').order_by('-id')

	if nivel == 1: #Admin

		data = Campania.objects.filter(usuario__empresa=empresa).values('id','usuario__first_name','estado','nombre','troncal','canales','timbrados','mxllamada','llamadaxhora','hombreobjetivo','supervisor__user__first_name').order_by('-id')


	fmt = '%H:%M:%S %Z'
	fmt1 = '%Y-%m-%d %H:%M:%S %Z'

	for i in range(len(data)):

		data[i]['htinicio'] = Campania.objects.get(id=data[i]['id']).htinicio.strftime(fmt)
		data[i]['hfin'] = Campania.objects.get(id=data[i]['id']).htfin.strftime(fmt)
		data[i]['fecha_cargada'] = Campania.objects.get(id=data[i]['id']).fecha_cargada.strftime(fmt1)

	data_dict = ValuesQuerySetToDict(data)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@login_required(login_url="/ingresar")
def nivel(request):

	id = request.user.id

	nivel = AuthUser.objects.get(id=id).nivel.id

	if nivel == 4: #Manager

		nivel = Nivel.objects.all().values('id','nombre')


	if nivel == 2: #Supervisores

		nivel = Nivel.objects.all().values('id','nombre')[2:3]


	if nivel == 1: #Admin

		nivel =  Nivel.objects.all().values('id','nombre')[1:3]



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

	id = request.user.id

	nivel = AuthUser.objects.get(id=id).nivel.id

	empresa = AuthUser.objects.get(id=id).empresa.id

	agentescampania = Agentescampanias.objects.filter(campania=id_campania)

	lista = []

	for a in agentescampania:

		lista.append(a.agente.id) 

	print lista

	agentes = Agentes.objects.filter(user__empresa__id=empresa).exclude(id__in=lista).values('id')


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

	nivel = AuthUser.objects.get(id=id).nivel.id

	agentes = Agentescampanias.objects.filter(campania=id_campania).values('id','agente','campania__nombre')

	for i in range(len(agentes)):


		print agentes[i]['id']



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

		print data

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

		supervisores = Supervisor.objects.filter(user=id).values('id','user__first_name')

	if nivel == 1:

		supervisores = Supervisor.objects.filter(user__empresa__id=empresa).values('id','user__first_name')

	if nivel == 4:

		supervisores = Supervisor.objects.all().values('id','user__first_name')


	data = json.dumps(ValuesQuerySetToDict(supervisores))

	return HttpResponse(data, content_type="application/json")



@login_required(login_url="/ingresar")
def usuarios(request):

	id = request.user.id

	nivel = AuthUser.objects.get(id=id).nivel.id

	empresa = AuthUser.objects.get(id=id).empresa

	if nivel == 4: #Manager

		usuarios = AuthUser.objects.all().values('id','telefono','username','email','empresa__nombre','nivel__nombre','first_name').order_by('-id')
	
	if nivel == 3: #Agentes

		usuarios = AuthUser.objects.filter(id=id).values('id','telefono','username','email','empresa__nombre','nivel__nombre','first_name').order_by('-id')

	if nivel == 2: #Supervisores

		supervisor = Supervisor.objects.get(user=id).id

		usuarios = AuthUser.objects.filter(empresa_id=empresa).values('id','telefono','username','email','empresa__nombre','nivel__nombre','first_name').order_by('-id')

	if nivel == 1: #Admin

		usuarios = AuthUser.objects.filter(empresa=empresa).exclude(nivel=4).values('id','telefono','username','email','empresa__nombre','nivel__nombre','first_name').order_by('-id')


	data = json.dumps(ValuesQuerySetToDict(usuarios))

	if request.method == 'POST':

		tipo = json.loads(request.body)['add']

		data = json.loads(request.body)['dato']

		print data

		if tipo == "New":

			username = data['username']
			telefono = data['telefono']

			if nivel == 4:
			
				empresa = data['empresa']
			else:
				empresa = empresa.id

			print empresa
		
			nivel = data['nivel']
			password = data['password']
			
			nombre=data['nombre']


			users = User.objects.all()

			e = 1

			for users in users:

				if username == users.username:

					info = username +' este correo ya existe, escoja otro pofavor'
					e = 0

			print 'e',e

			if e == 1:

				

				user = User.objects.create_user(username=username,password=password)

				user.save()

				id_user = AuthUser.objects.all().values('id').order_by('-id')[0]['id']

				usuario = AuthUser.objects.get(id=id_user)
			
				usuario.empresa_id = empresa
				usuario.nivel_id = nivel
				usuario.first_name = nombre
				usuario.telefono = telefono
				usuario.save()

				info = 'Usuario ' + usuario.first_name + ' ingresado al sistema, gracias'

				if nivel == 2: #Asignacion de carteras al supervisor

					supi = Supervisor(user_id=id_user).save()

					id_sup = Supervisor.objects.all().values('id').order_by('-id')[0]['id']

					for i in data['cartera']:

						id_cartera = Cartera.objects.get(nombre=i['cartera__nombre']).id

						Supervisorcartera(cartera_id=id_cartera,supervisor_id=id_sup).save()

		
				if nivel == 3: # Usuario Agente

					
					Agentes(user_id=id_user).save()

					agente =Agentes.objects.get(user=id_user)
					
					agente.atendidas = 0
					agente.contactadas =0
					agente.estado_id = 1
					agente.tiempo = datetime.strptime("00:00:00", "%H:%M:%S")
					agente.save()

			return HttpResponse(info, content_type="application/json")


		if tipo=="Edit":

			id= data['id']

			print data

			user = AuthUser.objects.get(id=id)
			user.username =data['username']
			user.first_name =data['first_name']
			user.telefono = data['telefono']
			

			user.save()


		if tipo=="Eliminar":

			id= data['id']

		
			if data['nivel__nombre']=='Supervisor':

				Supervisor.objects.get(user_id=id).delete()

			if data['nivel__nombre']=='Agente':

				Agentes.objects.get(user_id=id).delete()

			User.objects.get(id=id).delete()



		return HttpResponse(data['username'], content_type="application/json")


	return HttpResponse(data, content_type="application/json")

@login_required(login_url="/ingresar")
def empresas(request):

	id = request.user.id

	nivel = AuthUser.objects.get(id=id).nivel.id

	if nivel == 4:

		empresas = Empresa.objects.all().values('id','nombre','licencias','mascaras','telefono','contacto','mail').order_by('-id')

	else:

		empresa = AuthUser.objects.get(id=id).empresa.id

		empresas = Empresa.objects.filter(id=empresa).values('id','nombre','licencias','mascaras','telefono','contacto','mail').order_by('-id')

	data = json.dumps(ValuesQuerySetToDict(empresas))

	if request.method == 'POST':

		tipo = json.loads(request.body)['add']

		data = json.loads(request.body)['dato']

		print 'data',json.loads(request.body)

		if tipo == "New":

			nombre = data['nombre']
			contacto = data['contacto']
			mail = data['mail']
			licencias = data['licencias']
			mascaras = data['mascaras']
			telefono = data['telefono']

			Empresa(nombre=nombre,contacto=contacto,mail=mail,licencias=licencias,mascaras=mascaras,telefono=telefono).save()

			return HttpResponse(nombre, content_type="application/json")


		if tipo=="Edit":

			id= data['id']

			print data

			empresa = Empresa.objects.get(id=id)
			empresa.nombre =data['nombre']
			empresa.contacto =data['contacto']
			empresa.mail =data['mail']
			empresa.licencias =data['licencias']
			empresa.mascaras =data['mascaras']
			empresa.telefono =data['telefono']
			empresa.save()


		if tipo=="Eliminar":

			id= data['id']

			print Empresa.objects.get(id=id).delete()


		return HttpResponse(data['nombre'], content_type="application/json")


	return HttpResponse(data, content_type="application/json")



@login_required(login_url="/ingresar")
def salir(request):

	logout(request)
	
	return HttpResponseRedirect("/ingresar")


def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]




def teleoperador(request,id):

	return render(request, 'screenagent.html',{})



