#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import urllib
import uuid

url = '/home/robot/sqlite/robotdb.db'

def insert_device(colume_num):
    db_uri = urllib.quote(url)
    conn = sqlite3.connect(db_uri)
    print 'delete device and idOfTaskAndDev table data..'
    conn.execute("DELETE FROM device")
    conn.execute("DELETE FROM idOfTaskAndDev")
    conn.commit()

    # insert into table TimedTask
    for id in xrange(1,colume_num+1):
        devicename = 'devicename' + str(id)
        s_uuid = str(uuid.uuid4())
        l_uuid = s_uuid.split('-')
        deviceid = ''.join(l_uuid)
        sql1 = "insert into device values(" + str(id) + ",'" + deviceid + "','" + devicename + "'," + str(id*10) + ", 1, 2, 0, 128, 657, 356, " \
              "232, 26, 789, 435)"
        sql2 = "insert into idOfTaskAndDev values(" + str(id) + "," + str(id) + ",'" + deviceid + "')"
        conn.execute(sql1)
        conn.execute(sql2)
    conn.commit()
    print 'insert  %s lines data ok.'%colume_num
    conn.close()

if __name__ == '__main__':
    insert_device(10)
