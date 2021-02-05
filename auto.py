#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 11:51:36 2020

@author: trocotronic
foked by @ancafe
"""
import os

from EdistribucionAPI import Edistribucion
from configparser import ConfigParser
from datetime import datetime
import functions
import mariadb
import sys
import json

config_object = ConfigParser()
file = os.path.dirname(__file__) + "\\config.ini"
config_object.read(file)
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
    edis = Edistribucion(login[0], login[1])
    edis.login()
    r = edis.get_cups()

    for cup in r['data']['lstCups']:
        s = edis.get_cups_detail(cup['Id'])
        nombre = edis.get_login_info()
        lstATR = s['lstATR'][0]['Id']
        print("CUP ", cup['Id'], ': ', cup['Direccion'])
        cups = cup['Id']
        try:
            cur.execute(
                "INSERT IGNORE cups (`cups`, `titular`, `direccion`, `id`, `asr`) VALUES (%s,%s,%s,%s,%s)",
                (cup['Name'], nombre['Name'], cup['Direccion'], cup['Id'], lstATR))
        except mariadb.Error as e:
            print(f"Error: {e}")
        conn.commit()
        functions.readConsumo(edis, cur, conn, lstATR, cup['Name'])

    if os.path.exists("edistribucion.access"):
        os.remove("edistribucion.access")
    if os.path.exists("edistribucion.session"):
            os.remove("edistribucion.session")


conn.close()
