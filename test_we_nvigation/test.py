#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ctypes import *

lib = cdll.LoadLibrary('/usr/local/lib/libmagsdk.so')

lib.MAG_NewChannel(1)

if lib.MAG_IsChannelAvailable(1):
    print 'channel available'
else:
    print 'channel not available'

lib.MAG_Initialize(1, None)

if lib.MAG_IsInitialized(1):
    print 'is init'
else:
    print 'not init'

if lib.MAG_LinkCamera(1, 207923392, 500):
    print 'link'
else:
    print 'not link'

class ss(Structure):
    _fields_ = [
        ('dwFPAWidth', c_ulong),
        ('dwFPAHeight', c_ulong),
        ('dwBMPWidth', c_ulong),
        ('dwBMPHeight', c_ulong),
        ('dwColorBarWidth', c_ulong),
        ('dwColorBarHeight', c_ulong),
    ]

OutputPara = ss()
OutputPara.dwFPAWidth = 100
OutputPara.dwFPAHeight = 200
OutputPara.dwBMPWidth = 100
OutputPara.dwBMPHeight = 200
OutputPara.dwColorBarWidth = 100
OutputPara.dwColorBarHeight = 200

def callback():
    print 'start process img'

def callback2():
    print 'start pluse'
stream = c_ulong(4)
if not lib.MAG_IsProcessingImage:

    lib.MAG_StartProcessImage(1, OutputPara, callback(), stream, None)
else:
    lib.MAG_StartProcessPulseImage(1, OutputPara, callback2(), stream, None)


class structPoint(Structure):
    _fields_ = [
        ('pData', c_ubyte),
    ]
pdata = structPoint()

class bitMap(Structure):
    _fields_ = [
        ('bitmap', c_ulong),
    ]
BITMAPINFO = bitMap()
BITMAPINFO = 10*20

# class pInfo(Structure):
#     _fields_ = [
#         ('dwBMPWidth', c_ulong)*('dwBMPHeight', c_ulong),
#     ]
if lib.MAG_GetOutputBMPdata(1, pdata, BITMAPINFO, BITMAPINFO):
    print 'output bmp true'
else:
    print 'output false'

# lib.MAG_ResetCamera(3)
dwIndex = c_ulong(1)
filename = c_wchar_p('/home/robot/ab.bmp')
# print type(dwIndex), type(filename)
lib.MAG_TransferPulseImage()
lib.MAG_SaveBMP(1,dwIndex,filename)