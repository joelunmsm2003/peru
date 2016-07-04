import MySQLdb
import sys

campania =  sys.argv[1]
resultado = sys.argv[2]
status_f = sys.argv[3]
status_h = sys.argv[4]
status_g = sys.argv[5]


print 'Sysargv',resultado,status_f,status_g,status_h

status_f = status_f.split("/")
status_g = status_g.split("/")
status_h = status_h.split("/")
resultado = resultado.split("/")

f = len(status_f)
g = len(status_g)
h = len(status_h)
r = len(resultado)

sf = ''
sg = ''
sh = ''
sr = ''

for i in range(0,f):

	sf = status_f[i]+"','"+sf 

for i in range(0,g):

	sg = status_g[i]+"','"+sg 

for i in range(0,h):

	sh = status_h[i]+"','"+sh 

for i in range(0,h):

	sr = resultado[i]+"','"+sr

status_f =  "("+sf[2:len(sf)-2]+")"
status_g =  "("+sg[2:len(sg)-2]+")"
status_h =  "("+sh[2:len(sh)-2]+")"
resultado =  "("+sr[2:len(sr)-2]+")"


print 'Resul',resultado,status_f,status_g,status_h

db = MySQLdb.connect(host="127.0.0.1",user="root",passwd="d4t4B4$3*",db="perucall") 

cur = db.cursor()

#SELECT campania, id, telefono, agEnte,id_cliente,ProFlag,ProEstado,FiltroHdeC,status,resultadotxt FROM base WHERE (status='' or status=0) AND campania ='264' AND ProFlag is NULL AND ProEstado is NULL AND FiltroHdeC is NULL AND status_f in ('CONTACTO') AND status_h in ('BASE1') AND status_g in ('BASE') AND ( resultadotxt='' OR resultadotxt in ('Contacto Directo'))

#cur = db.cursor()


print "SELECT resultadotxt FROM base where (status='' or status=0) and campania ="+campania +" and ProFlag is NULL and ProEstado is NULL and FiltroHdeC is NULL AND status_f in " + status_f

cur.execute("SELECT id_cliente,resultadotxt,status_f FROM base where (status='' or status=0) and campania ="+campania +" and ProFlag is NULL and ProEstado is NULL and FiltroHdeC is NULL AND status_f in " + status_f)  

y = cur.fetchall()

lote = [item for item in y]

'''

for e in lote:

	print e

'''