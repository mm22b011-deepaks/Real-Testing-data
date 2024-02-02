#!/home/pi/Deepak/env/bin/python

from RPLCD import *
import time
from RPLCD.i2c import CharLCD
import multiprocessing
from datetime import datetime
import os
from pwn import *

#os.system("sudo ip link set can0 up type can bitrate 500000")

#def LCD(speed, SoC, Temp, R2D):

#    lcd = CharLCD('PCF8574', 0x27)

#    lcd.cursor_pos = (0, 0)
#    lcd.write_string('Speed     :')
#    lcd.cursor_pos = (1,0)
#    lcd.write_string('Soc       :')
#    lcd.cursor_pos = (2,0)
#    lcd.write_string('Temp      :')

#    lcd.cursor_pos = (0,11)
#    lcd.write_string("m/s")
#    lcd.cursor_pos = (1,11)
#    lcd.write_string("%")
#    lcd.cursor_pos = (2,11)
#    lcd.write_string("C")
#    lcd.cursor_pos = (3,0)
#    lcd.write_string('R2D State :')

def CANData():
    #subprocess.run(["candump", "any"])
    p10 = process("./candump.sh")
    p = p10.recvline()
    return p

def saveData(p):
    timestamp = datetime.now()
    filename = timestamp.strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
    f = open(filename, "w+")
    while 2>1:
        f.write(p)
    f.close()


if __name__ == "__main__": 
    p = ""
    p1 = multiprocessing.Process(target=CANData)
    #p2 = multiprocessing.Process(target=LCD, args=(speed, SoC, Temp,R2D))
    p2 = multiprocessing.Process(target=saveData, args=(p))


