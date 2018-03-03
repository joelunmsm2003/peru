from PeruCall.models import *
import os

print AjxProLla.objects.all()[:1]

cam = Campania.objects.filter(fecha_cargada__gte='2018-01-01',cartera__nombre='ENEL')

for c in cam

	data  = AjxProLla.objects.filter(cam_codigo=c.id).values('id_ori_llamadas','cam_codigo','llam_numero')

	fmt = '%Y-%m-%d %H:%M:%S %Z'

	for i in range(len(data)):

		data[i]['fecha'] = AjxProLla.objects.get(id_ori_llamadas=data[i]['id_ori_llamadas']).f_origen.strftime(fmt)
		anio = data[i]['fecha'].slice(0,4)
		mes = data[i]['fecha'].slice(5,7)
		dia = data[i]['fecha'].slice(8,10)
		campania = data[i]['cam_codigo']
		origen = data[i]['cam_codigo']
		destino = data[i]['llam_numero']
		fecha = data[i]['fecha'].slice(0,10)
		hora = data[i]['fecha'].slice(11,13)
		minu = data[i]['fecha'].slice(14,16)
		seg= data[i]['fecha'].slice(17,19)

		os.system("cp /var/www//monitor/pcall/"+anio+"/"+mes+"/"+dia+"/"+campania+"/"+origen+"-"+destino+"-"+fecha+"_"+hora+"-"+min+"-"+seg+".gsm /var/www/html/enel/")


# window.location.href = "http://192.168.50.206:81/monitor/pcall/"+anio+"/"+mes+"/"+dia+"/"+campania+"/"+origen+"-"+destino+"-"+fecha+"_"+hora+"-"+min+"-"+seg+".gsm"
        
