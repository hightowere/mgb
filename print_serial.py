# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 06:21:57 2020

@author: Emily
"""

import serial

class ReadLine:
    def __init__(self, s):
        self.buf = bytearray()
        self.s = s
    
    def readline(self):
        i = self.buf.find(b"\n")
        if i >= 0:
            r = self.buf[:i+1]
            self.buf = self.buf[i+1:]
            return r
        while True:
            i = max(1, min(2048, self.s.in_waiting))
            data = self.s.read(i)
            i = data.find(b"\n")
            if i >= 0:
                r = self.buf + data[:i+1]
                self.buf[0:] = data[i+1:]
                return r
            else:
                self.buf.extend(data)

ser=serial.Serial(port='/dev/ttyUSB1', timeout=None, baudrate=19200)
r1=ReadLine(ser)

print('checkpoint')

while True:
    print(r1.readline())
