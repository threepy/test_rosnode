#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import urllib

def insert_process_table(colume_num):
    url = '/home/robot/sqlite/robotdb.db'
    db_uri = urllib.quote(url)
    conn = sqlite3.connect(db_uri)
    print 'delete process table data..'
    conn.execute("DELETE FROM process")
    conn.commit()
    # insert into table TimedTask
    for id in range(1,colume_num+1):
        # method: 0~10
        method = 0
        bTaskOver = 1 # 1: over
        sql = "INSERT INTO process (deviceID, taskID, taskPlanID, pointID, method, execTime, envTemperature, Humidity, WindSpeed, WindDirect, pm25, infraDistance, infraEmissivity, voltage, bTaskOver) \
              values ('4b43b0aee35624cd95b910189b3dc231','d630a1f488af4aa2a4d5f366a0494fd6',1,5," + str(method) + ",1234, 45.32, 23.21, 32.09, 1, 13.12, 34.44, 43.21, 56.3," + str(bTaskOver) + ")"

        conn.execute(sql)
    conn.commit()
    print 'insert  %s lines data ok.'%colume_num
    conn.close()

if __name__ == '__main__':
    insert_process_table(1)