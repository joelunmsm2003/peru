import MySQLdb
import requests
import datetime
import json

db = MySQLdb.connect(host="127.0.0.1",user="root",passwd="d4t4B4$3p3c4ll2016*",db="perucall") 

cur = db.cursor()

query ="UPDATE sms_traffic SET status="+ str(3) +", error = '0', reference = '"+ respuesta +"' , reference_time = '"+ today + "' WHERE id ="+ str(id)
            
cur.execute(query)

db.commit()

            


          