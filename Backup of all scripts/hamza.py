#!/home/pi/Deepak/env/bin/python

from RPLCD import *
import time
from datetime import datetime
from RPLCD.i2c import CharLCD
lcd = CharLCD('PCF8574', 0x27)

lcd.cursor_pos = (0, 0)
lcd.write_string('Speed :')
lcd.cursor_pos = (1,0)
lcd.write_string('Soc   :')
lcd.cursor_pos = (2,0)
lcd.write_string('Temp  :')

lcd.cursor_pos = (0,11)
lcd.write_string("m/s")
lcd.cursor_pos = (1,11)
lcd.write_string("%")
lcd.cursor_pos = (2,11)
lcd.write_string("C")

now = datetime.now()
timestring = '%0#2d,%0#2d' % (now.hour,now.minute)

lcd.cursor_pos = (3,0)
lcd.write_string(timestring)
