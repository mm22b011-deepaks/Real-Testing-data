#!/home/pi/Deepak/env/bin/python

from RPLCD import *
import time
from RPLCD.i2c import CharLCD
from datetime import datetime
from pwn import process

# Global variable to store CAN messages
can_send = ""

def CANData():
    global can_send
    global can_data
    lcd = CharLCD('PCF8574', 0x27)
    lcd.cursor_pos = (0, 0)
    lcd.write_string('Speed     :')
    lcd.cursor_pos = (1,0)
    lcd.write_string('Soc       :')
    lcd.cursor_pos = (2,0)
    lcd.write_string('Temp      :')

    lcd.cursor_pos = (0,11)
    lcd.write_string("m/s")
    lcd.cursor_pos = (1,11)
    lcd.write_string("%")
    lcd.cursor_pos = (2,11)
    lcd.write_string("C")
    lcd.cursor_pos = (3,0)
    lcd.write_string('R2D State :')

    timestamp = datetime.now()
    filename = timestamp.strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
    print(filename)
    p10 = process("./candump.sh")
    while True:
        can_data = p10.recvline()
        can_send = can_data.decode('utf-8')
        print(can_send)
        with open(filename, "a+") as f:
             f.write(can_send)
    



#def saveData():
#    global can_data
#    timestamp = datetime.now()
#    filename = timestamp.strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
#    print(filename)
#    while True:
#        with open(filename, "a+") as f:
#             f.write(can_send)

if __name__ == "__main__":
#    CANData()
#    saveData()
    CANData()
