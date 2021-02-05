import mariadb

from EdistribucionAPI import Edistribucion
from datetime import datetime

def readConsumo( edis, cur, conn, cups, real ):
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
                        "INSERT IGNORE INTO consumos (`cups`, `date`, `hour`, `invoiced`, `obtainingMethod`, `real`, `value`) VALUES (%s,%s,%s,%s,%s,%s,%d)",
                        (real, date_object, dia['hour'], dia['invoiced'], dia['obtainingMethod'], dia['real'],
                         dia['value']))
                except mariadb.Error as e:
                    print(f"Error: {e}")
    conn.commit()
    return
