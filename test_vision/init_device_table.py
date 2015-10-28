#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import urllib

url = '/home/robot/sqlite/robotdb.db'

def insert_device(colume_num):
    db_uri = urllib.quote(url)
    conn = sqlite3.connect(db_uri)
    print 'delete device data..'
    conn.execute("DELETE FROM device")
    conn.commit()
    # insert into table TimedTask
    for id in xrange(1,colume_num+1):
        devicename = 'devicename' + str(id)
        sql = "insert into device values(" + str(id) + "," + str(id) + ",'" + devicename + "', 45, 1, 2, 0, 128, 657, 356, " \
              "232, 26, 789, 435)"
        conn.execute(sql)
    conn.commit()
    print 'insert  %s lines data ok.'%colume_num
    conn.close()

if __name__ == '__main__':
    insert_device(100)
