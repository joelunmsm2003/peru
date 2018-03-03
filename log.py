import os
import time
import requests

os.system('cat mysite.log |grep "ERROR" >log.txt')

file = open('log.txt', 'r')

x= 'No hay Error'

while True :

	for line in file:


		x=line


	print 'Enviando ticket....'
	url ="http://xiencias.com:8000/add_tarea/"
	params = {'username':'joel','password':'123','asunto':'Error PeruCall' ,'tipo':1,'descripcion':str(line)}
	r=requests.post(url,params=params)

	print r.text

	f = open('error.html','w')
	f.write(r.text)
	f.close()



	time.sleep(500)



