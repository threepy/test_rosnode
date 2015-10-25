#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import urllib


def readlineAndInsert():
    # open file, it's should be utf-8
    # iconv -f gbk -t utf8 device10.txt > dev.txt
    f = open("/home/robot/map.txt", mode="r")

    while True:
        lines = f.readlines(10000)
        if not lines:
            break
        for line in lines:
            list2 = line.split()
            insertTable(list2)
            print "insert to map",list2[0],list2[1]

    f.close()
    print "insert ok"

def insertTable(list3):
    url = "/home/robot/sqlite/robotdb.db"
    db_uri = urllib.quote(url)
    conn = sqlite3.connect(db_uri)
    sql = "insert into map values (" + list3[0] + "," + list3[1] + ")"
    try:
        conn.execute(sql)
    finally:
        conn.commit()
        print "COMMIT!"

if __name__ == "__main__":
    readlineAndInsert()
