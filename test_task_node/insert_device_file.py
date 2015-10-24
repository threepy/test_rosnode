#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import urllib


def readlineAndInsert():
    # open file, it's should be utf-8
    # iconv -f gbk -t utf8 device10.txt > dev.txt
    f = open('/home/robot/dev.txt', mode='r')
    # read lines
    for line in f.readlines():
        # split with ","
        list2 = line.split(',')
        # delete blank
        list3 = map(lambda x:x.strip(),list2)
        # if item has '' it will replace NULL
        for item in list3:
            if item == '':
                item = 'Null'
        # execute insert
        insertTable(list3)
        print 'insert one line'
    print'insert ok'

def insertTable(list3):
    url = '/home/robot/sqlite/robotdb.db'
    db_uri = urllib.quote(url)
    conn = sqlite3.connect(db_uri)
    sql = "insert into table1 values (" \
          + list3[0] + "," + list3[1] + "," + list3[2]+ "," + list3[3]+ "," + "'" + list3[4]+ "'" + "," + "'" + list3[5] + "'" + "," + list3[6]\
          + "," + list3[7]+ "," + list3[8]+ "," + list3[9]+ "," + list3[10]+ "," + list3[11]+ "," + list3[12]+ "," + "'" + list3[13]\
          + "'" + "," + list3[14] + "," + list3[15]+ "," + "'" +list3[16]+ "'" + "," + list3[17] +")"
    conn.execute(sql)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    readlineAndInsert()