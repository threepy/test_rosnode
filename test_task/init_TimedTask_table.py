#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import urllib
import time

def insert_TimedTask(colume_num):
    url = '/home/robot/sqlite/robotdb.db'
    db_uri = urllib.quote(url)
    conn = sqlite3.connect(db_uri)
    print 'delete TimedTask data..'
    conn.execute("DELETE FROM TimedTask")
    conn.commit()
    # insert into table TimedTask
    for id in range(1,colume_num+1):

        # get time now
        hour = time.strftime('%H',  time.localtime(time.time()))
        min = time.strftime('%M', time.localtime(time.time()))
        second = time.strftime('%S', time.localtime(time.time()))

        t = int(hour)*3600 + int(min)*60 + int(second) 
        schedule_time = t + id*3 + 30
        # loopType: 0:立即 1:每天, 2:每周, 3:每月, 4:单次
        # SCHEDULE_PARAM: 每周的周一至周日(1,2,3,4,5,6,7),(1,2,3,...31)每月的1,2,3号
        loopType = 1

        taskname = 'taskname' + str(id)
        sql = "INSERT INTO TimedTask (taskPlanID, taskName, taskType, loopType, runMode, SCHEDULE_PARAM, SCHEDULE_TIME, finishAction, RecordVideo) \
              VALUES (" + str(id) + ",'" + taskname + "', 1," + str(loopType) + ", 1,'1,2,3,26,30'," + str(schedule_time) + ", 0, 1)"
        # sql = "INSERT INTO TimedTask (taskPlanID, taskName, taskType, loopType, runMode, SCHEDULE_PARAM, SCHEDULE_TIME, finishAction, RecordVideo) \
        #       VALUES (" + str(id) + ", 'taskname', 1," + str(loopType) + ", 1,'1,2,3,26,30'," + str(schedule_time) + ", 0, 1)"

        conn.execute(sql)
    conn.commit()
    print 'insert  %s lines data ok.'%colume_num
    conn.close()

if __name__ == '__main__':
    insert_TimedTask(10)
