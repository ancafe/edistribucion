#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 11:51:36 2020

@author: trocotronic
foked by @ancafe
"""

from EdistribucionAPI import Edistribucion
from configparser import ConfigParser
from datetime import datetime
import mariadb
import sys
import json




def readConsumo( cups, real ):
    # OBTENEMOS CONSUMO
    print("MEDIMO CONSUMO")
    print(cups)
    consumo = edis.get_measure(cups)
    if 'mapHourlyPoints' in consumo['data']:
        for el, value in consumo['data']['mapHourlyPoints'].items():
            for dia in value:
                date_object = datetime.strptime(el, '%d-%m-%Y').strftime('%Y-%m-%d')
                try:
                    cur.execute(
                        "REPLACE INTO consumos (`cups`, `date`, `hour`, `invoiced`, `obtainingMethod`, `real`, `value`) VALUES (%s,%s,%s,%s,%s,%s,%d)",
                        (real, date_object, dia['hour'], dia['invoiced'], dia['obtainingMethod'], dia['real'],
                         dia['value']))
                except mariadb.Error as e:
                    print(f"Error: {e}")
    conn.commit()
    return


config_object = ConfigParser()
config_object.read("config.ini")

login = config_object["LOGIN"]
db = config_object["DATABASE"]

try:
   conn = mariadb.connect(
      user=db['user'],
      password=db['pwd'],
      host=db['host'],
      port=int(db['port']),
      database=db['database'])

except mariadb.Error as e:
   print(f"Error conectando a la base de datos: {e}")
   sys.exit(1)

cur = conn.cursor()

query = f"SELECT * FROM login"
cur.execute(query)
rows = cur.fetchall()

for login in rows:
    print(login[0])

sys.exit(1)

edis = Edistribucion(login['user'],login['pwd'])
edis.login()

r = edis.get_cups()

for cup in r['data']['lstCups']:
    s = edis.get_cups_detail(cup['Id'])
    nombre = edis.get_login_info()
    lstATR = s['lstATR'][0]['Id']
    print("CUP ",cup['Id'], ': ',cup['Direccion'])
    cups = cup['Id']
    try:
        cur.execute(
            "REPLACE INTO cups (`cups`, `titular`, `direccion`, `id`, `asr`) VALUES (%s,%s,%s,%s,%s)",
            (cup['Name'], nombre['Name'], cup['Direccion'], cup['Id'], lstATR))
    except mariadb.Error as e:
        print(f"Error: {e}")
    conn.commit()
    readConsumo(lstATR, cup['Name'])



#auth = edis.get_auth()
#print (auth)

"""
r = edis.get_cups()
cups = r['data']['lstCups'][0]['Id']
print('CUPS: ',r)
print('Cups: ',edis.get_all_cups())
meter = edis.get_meter(cups)
print('Meter: ',meter)"""


conn.close()




#meter = edis.get_meter(cups)
#res = edis.get_logininfo()
#print(res);

#res = edis.get_info(cups)
#print(res)