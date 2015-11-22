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

import xlrd
import json 
import csv
import simplejson
import xlwt
import requests
import os

from datetime import datetime
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

					id_user= AuthUser.objects.get(username=user).id

					print nivel

					if nivel == 1:

						return HttpResponseRedirect("/empresa")

					if nivel == 2:

						return HttpResponseRedirect("/empresa")

					if nivel == 3:

						return HttpResponseRedirect("/teleoperador/"+str(id_user))

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



	troncales = Troncales.objects.all()

	if nivel == 1:

		supervisor = Supervisor.objects.all()


	if nivel == 2:

		supervisor = Supervisor.objects.filter(user=id)


	if nivel == 4:

		supervisor = Supervisor.objects.all()



	
	
	
	return render(request, 'campania.html',{'supervisor':supervisor,'troncales':troncales})



@login_required(login_url="/ingresar")
def filtros(request,id):
	campania = Campania.objects.get(id=id)
	return render(request, 'filtros.html',{'campania':campania})

@login_required(login_url="/ingresar")
def cartera(request):
	
	return render(request, 'cartera.html',{})

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

	user = Agentescampanias.objects.filter(campania=id_campania).values('id','agente__user__first_name','agente__fono','agente__anexo','agente__atendidas','agente__contactadas','agente__estado')

	fmt = '%Y-%m-%d %H:%M:%S %Z'

	for i in range(len(user)):

		print user[i]['id']

		user[i]['agente__tiempo'] = Agentescampanias.objects.get(id=user[i]['id']).agente.tiempo.strftime(fmt)
		
		if user[i]['agente__atendidas'] > 0:

			user[i]['performance'] =  (user[i]['agente__contactadas']/user[i]['agente__atendidas'])*100

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
def agregarfiltro(request):

	if request.method == 'POST':

		grupo= json.loads(request.body)['grupo']
		ciudad= json.loads(request.body)['ciudad']
		segmento= json.loads(request.body)['segmento']
		campania = json.loads(request.body)['campania']

		ciudadt = ""
		grupot = ""
		segmentot = ""

		for i in range(len(ciudad)):

			print ciudad[i]['nombre']

			ciudadt = ciudadt  + ciudad[i]['nombre'] +'/'

		for i in range(len(grupo)):

			print grupo[i]['nombre']

			grupot = grupot  + grupo[i]['nombre'] +'/'

		for i in range(len(segmento)):

			print segmento[i]['nombre']

			segmentot = segmentot  + segmento[i]['nombre'] +'/'
  

		Filtro(ciudad=ciudadt,grupo=grupot,segmento=segmentot,campania_id=campania).save()

		data = Base.objects.filter(ciudad=ciudad,segmento=segmento,grupo=grupo).values('id','ciudad','segmento','grupo').count()


		return HttpResponse(data, content_type="application/json")

@login_required(login_url="/ingresar")
def eliminarfiltro(request):

	if request.method == 'POST':

		id_filtro= json.loads(request.body)['dato']['id']

		Filtro.objects.get(id=id_filtro).delete()

		print dato

		return HttpResponse(id_filtro, content_type="application/json")

@login_required(login_url="/ingresar")
def carteras(request):

	id = request.user.id
	nivel = AuthUser.objects.get(id=id).nivel.id
	empresa = AuthUser.objects.get(id=id).empresa.id

	if request.method == 'GET':

		if nivel == 1:

			data = Carteraempresa.objects.filter(empresa_id=empresa).values('id','cartera__nombre','empresa__nombre').order_by('-id')

		if nivel == 2:

			data = Carteraempresa.objects.filter(empresa_id=empresa).values('id','cartera__nombre','empresa__nombre').order_by('-id')

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


	data = Filtro.objects.filter(campania_id=id_campania).values('id','ciudad','segmento','grupo').order_by('-id')

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

	data_dict = ValuesQuerySetToDict(user)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@login_required(login_url="/ingresar")
def ciudad(request):

	user = Ciudad.objects.all().values('id','nombre')

	data_dict = ValuesQuerySetToDict(user)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@login_required(login_url="/ingresar")
def grupo(request):

	user = Grupo.objects.all().values('id','nombre')

	data_dict = ValuesQuerySetToDict(user)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@login_required(login_url="/ingresar")
def segmento(request):

	user = Segmento.objects.all().values('id','nombre')

	data_dict = ValuesQuerySetToDict(user)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")



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

		data = request.POST

		canales = data['canales']
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

		Campania(supervisor_id=supervisor,usuario_id=id,fecha_cargada= now,archivo = archivo,canales=canales,htinicio=inicio,htfin=fin,nombre=nombre,timbrados=timbrados,llamadaxhora=llamadaxhora,hombreobjetivo=hombreobjetivo,mxllamada=mxllamada).save()

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
			producto = a[4]
			tarjeta = a[5]
			deuda = a[6]
			descuento =a[7]
			diasmora= a[8].replace(".0","")
			ciudad=a[9]
			segmento= a[10]
			grupo = a[11]

			Base(telefono=telefono,orden=orden,cliente=cliente,id_cliente=id_cliente,producto=producto,tarjeta=tarjeta,deuda=deuda,descuento=descuento,diasmora=diasmora,ciudad=ciudad,segmento=segmento,grupo=grupo).save()

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

@login_required(login_url="/ingresar")
def base(request,id_campania):

	id = request.user.id

	base = Base.objects.filter(campania=id_campania,status=1).values('id','telefono','orden','producto','id_cliente','tarjeta','deuda','descuento','diasmora')

	data_dict = ValuesQuerySetToDict(base)

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

		usuarios = Agentes.objects.filter(supervisor=supervisor).values('user')

		for i in range(len(usuarios)):


			usuarios[i]['id'] = AuthUser.objects.get(id=usuarios[i]['user']).id
			usuarios[i]['username'] = AuthUser.objects.get(id=usuarios[i]['user']).username
			usuarios[i]['first_name'] = AuthUser.objects.get(id=usuarios[i]['user']).first_name
			usuarios[i]['email'] = AuthUser.objects.get(id=usuarios[i]['user']).email
			usuarios[i]['empresa__nombre'] = AuthUser.objects.get(id=usuarios[i]['user']).empresa.nombre
			usuarios[i]['nivel__nombre'] = AuthUser.objects.get(id=usuarios[i]['user']).nivel.nombre

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

						Supervisorcartera(cartera_id=i['id'],supervisor_id=id_sup).save()

		
				if nivel == 3: # Usuario Agente

					
					Agentes(user_id=id_user).save()

					agente =Agentes.objects.get(user=id_user)
					
					agente.atendidas = 0
					agente.contactadas =0
					agente.estado_id = 1
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



