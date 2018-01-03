from PeruCall.models import *

print AjxProLla.objects.all()[:1]


anio = data['fecha'].slice(0,4)
mes = data['fecha'].slice(5,7)
dia = data['fecha'].slice(8,10)
campania = data['cam_codigo']
origen = data['cam_codigo']
destino = data['llam_numero']
fecha = data['fecha'].slice(0,10)
hora = data['fecha'].slice(11,13)
min = data['fecha'].slice(14,16)
seg= data['fecha'].slice(17,19)