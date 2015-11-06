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

			return render(request, 'logear.html',{})


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
	supervisor = Supervisor.objects.all()
	return render(request, 'campania.html',{'supervisor':supervisor})

@login_required(login_url="/ingresar")
def micampania(request):
	return render(request, 'micampania.html',{})

@login_required(login_url="/ingresar")
def adminCampania(request,id_campania):
	campania = Campania.objects.get(id=id_campania)
	return render(request, 'admincampania.html',{'campania':campania})

@login_required(login_url="/ingresar")
def monitoreo(request,id):
	campania = Campania.objects.get(id=id)
	return render(request, 'monitoreo.html',{'campania':campania})


@login_required(login_url="/ingresar")
def agentes(request,id_campania):
	id = request.user.id

	user = Agentescampanias.objects.filter(campania=id_campania).values('id','agente__user__first_name','agente__fono','agente__anexo','agente__atendidas','agente__contactadas','agente__estado')

	fmt = '%Y-%m-%d %H:%M:%S %Z'

	for i in range(len(user)):

		print user[i]['id']

		user[i]['agente__tiempo'] = Agentescampanias.objects.get(id=user[i]['id']).agente.tiempo.strftime(fmt)
		user[i]['performance'] =  (user[i]['agente__contactadas']/user[i]['agente__atendidas'])*100

	data_dict = ValuesQuerySetToDict(user)

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
def uploadCampania(request):

	if request.method == 'POST':

		id = request.user.id

		data = request.POST

		print 'dataaaaaaaaaaaaaaaaaa',data

		troncal = data['troncal']
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

		Campania(supervisor_id=supervisor,usuario_id=id,fecha_cargada= now,archivo = archivo,troncal=troncal,canales=canales,htinicio=inicio,htfin=fin,nombre=nombre,timbrados=timbrados,llamadaxhora=llamadaxhora,hombreobjetivo=hombreobjetivo,mxllamada=mxllamada).save()

		id_campania = Campania.objects.all().values('id').order_by('-id')[0]['id']

	return HttpResponseRedirect("/adminCampania/"+str(id_campania))


@login_required(login_url="/ingresar")
def campanias(request):

	id = request.user.id
	nivel = AuthUser.objects.get(id=id).nivel.id
	empresa = AuthUser.objects.get(id=id).empresa
	if nivel == 4: #Manager
		data = Campania.objects.all().values('id','usuario__first_name','estado','nombre','troncal','canales','timbrados','mxllamada','llamadaxhora','hombreobjetivo','supervisor__user__first_name')
	if nivel == 2: #Supervisores
		supervisor = Supervisor.objects.get(user=id).id

		data = Campania.objects.filter(supervisor=supervisor).values('id','usuario__first_name','estado','nombre','troncal','canales','timbrados','mxllamada','llamadaxhora','hombreobjetivo','supervisor__user__first_name')

	if nivel == 1: #Admin

		data = Campania.objects.filter(usuario__empresa=empresa).values('id','usuario__first_name','estado','nombre','troncal','canales','timbrados','mxllamada','llamadaxhora','hombreobjetivo','supervisor__user__first_name')


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
def agentesdisponibles(request,id_campania):

	id = request.user.id

	nivel = AuthUser.objects.get(id=id).nivel.id

	supervisor = Campania.objects.get(id=id_campania).supervisor

	agentescampania = Agentescampanias.objects.filter(campania=id_campania)

	lista = []

	for a in agentescampania:

		print a.agente

		lista.append(a.agente.id) 

	print lista

	agentes = Agentes.objects.filter(supervisor=supervisor).exclude(id__in=lista).values('id')

	for i in range(len(agentes)):

		agentes[i]['name'] = Agentes.objects.get(id=agentes[i]['id']).user.username
		agentes[i]['estado'] = Agentes.objects.get(id=agentes[i]['id']).estado.nombre
	

	data_dict = ValuesQuerySetToDict(agentes)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")

@login_required(login_url="/ingresar")
def agentescampania(request,id_campania):

	id = request.user.id

	nivel = AuthUser.objects.get(id=id).nivel.id

	supervisor = Campania.objects.get(id=id_campania).supervisor

	agentes = Agentescampanias.objects.filter(agente__supervisor=supervisor,campania=id_campania).values('id')

	for i in range(len(agentes)):

		agentes[i]['name'] = Agentescampanias.objects.get(id=agentes[i]['id']).agente.user.username
		agentes[i]['estado'] = Agentescampanias.objects.get(id=agentes[i]['id']).agente.estado.nombre

	data_dict = ValuesQuerySetToDict(agentes)

	data = simplejson.dumps(data_dict)

	return HttpResponse(data, content_type="application/json")


@login_required(login_url="/ingresar")
def agregaragente(request):

	if request.method == 'POST':

		data= json.loads(request.body)['dato']

		campania = json.loads(request.body)['campania']

		id_agente = data['id']

		Agentescampanias(agente_id=id_agente,campania_id=campania).save()

		agente = Agentes.objects.get(id=id_agente)

		return HttpResponse(agente.user.username, content_type="application/json")

@login_required(login_url="/ingresar")
def quitaragente(request):

	if request.method == 'POST':

		data= json.loads(request.body)['dato']

		campania = json.loads(request.body)['campania']

		id_agente = data['id']

		agente = Agentescampanias.objects.filter(agente=id_agente,campania=campania).delete()

		agente = Agentes.objects.get(id=id_agente)

		return HttpResponse(agente.user.username, content_type="application/json")

@login_required(login_url="/ingresar")
def supervisores(request):

	id = request.user.id

	nivel = AuthUser.objects.get(id=id).nivel.id

	empresa = AuthUser.objects.get(id=id).empresa

	if nivel == 2:

		supervisores = Supervisor.objects.filter(user=id).values('id','user__first_name')

	if nivel == 1:

		supervisores = Supervisor.objects.filter(agente__user__empresa__id=empresa).values('id','user__first_name')

	if nivel == 4:

		supervisores = Supervisor.objects.all().values('id','user__first_name')


	data = json.dumps(ValuesQuerySetToDict(supervisores))

	return HttpResponse(data, content_type="application/json")


@login_required(login_url="/ingresar")
def usuarios(request):


	id = request.user.id

	print id

	nivel = AuthUser.objects.get(id=id).nivel.id

	empresa = AuthUser.objects.get(id=id).empresa



	if nivel == 4: #Manager

		usuarios = AuthUser.objects.all().values('id','username','email','empresa__nombre','nivel__nombre','first_name').order_by('-id')
	
	if nivel == 3: #Agentes

		usuarios = AuthUser.objects.filter(id=id).values('id','username','email','empresa__nombre','nivel__nombre','first_name').order_by('-id')


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

		usuarios = AuthUser.objects.filter(empresa=empresa).exclude(nivel=4).values('id','username','email','empresa__nombre','nivel__nombre','first_name').order_by('-id')

	for i in range(len(usuarios)):

		if usuarios[i]['nivel__nombre'] == 'Agente':

			print usuarios[i]['id']

			usuarios[i]['supervisor'] = Agentes.objects.get(user=usuarios[i]['id']).supervisor.user.first_name
	

	data = json.dumps(ValuesQuerySetToDict(usuarios))

	if request.method == 'POST':

		tipo = json.loads(request.body)['add']

		data = json.loads(request.body)['dato']

		print 'data',json.loads(request.body)

		if tipo == "New":

			username = data['username']
			empresa = data['empresa']
			email = data['email']
			nivel = data['nivel']
			password = data['password']
			
			nombre=data['nombre']

			user = User.objects.create_user(username=username,email=email,password=password)

			user.save()

			id_user = AuthUser.objects.all().values('id').order_by('-id')[0]['id']

			usuario = AuthUser.objects.get(id=id_user)
		
			usuario.empresa_id = empresa
			usuario.nivel_id = nivel
			usuario.first_name = nombre
			usuario.save()

	
			if nivel == 3:

				supervisor = data['supervisor']
				Agentes(user_id=id_user).save()

				agente =Agentes.objects.get(user=id_user)
				agente.supervisor_id = supervisor
				agente.save()

			return HttpResponse(username, content_type="application/json")


		if tipo=="Edit":

			id= data['id']

			print data

			user = User.objects.get(id=id)
			user.username =data['username']
			user.empresa =data['empresa']
			user.email = data['email']
			user.nivel = data['nivel']

			user.save()


		if tipo=="Eliminar":

			id= data['id']

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



