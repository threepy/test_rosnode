#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import urllib
import time

url = '/home/robot/sqlite/robotdb.db'

def insert_process_table(colume_num):
    db_uri = urllib.quote(url)
    conn = sqlite3.connect(db_uri)
    print 'delete process table data..'
    conn.execute("DELETE FROM process")
    conn.commit()
    # insert into table TimedTask
    for id in range(1,colume_num+1):
        sql = "INSERT INTO process (deviceID, taskID, taskPlanID, pointID, method, execTime) \
              values (1,1314691378,4,5,6,1234)"

        conn.execute(sql)
    conn.commit()
    print 'insert  %s lines data ok.'%colume_num
    conn.close()

if __name__ == '__main__':
    insert_process_table(10)
