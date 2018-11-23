from emblaze import mysql

import json
import datetime
import time  


def getInfo(inp,search):
    res = {}

    query = "SELECT * FROM {0} WHERE name LIKE '{1}%'".format(inp.lower(),search)
    
    conn = mysql.connect()
    cursor =mysql.get_db().cursor()
    queryResults = cursor.execute(query)
    data = cursor.fetchall()
    takeMedicineRes = {}

    for i,result in enumerate(data):
        res[i] = [str(result[0])]


    return res
