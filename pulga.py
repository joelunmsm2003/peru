import MySQLdb
import sys

cli =  sys.argv[1]

db = MySQLdb.connect(host="127.0.0.1",user="root",passwd="d4t4B4$3*",db="perucall") 

cur = db.cursor()

query ="UPDATE base SET bloqueocliente="+ str(0) +" WHERE id_cliente ="+ str(cli)

cur.execute(query)

db.commit()

