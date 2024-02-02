#!/home/pi/Deepak/env/bin/python

from RPLCD import *
import time
from RPLCD.i2c import CharLCD
import multiprocessing
import os
from pwn import *
import numpy as np

os.system("sudo ip link set can0 up type can bitrate 500000")

def LCD(speed, SoC, Temp, R2D, can_data_queue):
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

    while True:
        if not can_data_queue.empty():
            data = can_data_queue.get()
            # Add your logic to update LCD based on data
            # Example: speed.value = data['speed']

def CANData(can_data_queue):
    p = process("cd ~ && ./candump.sh")
    while True:
        # Modify this part to capture and format the data from your CAN source
        # Example: can_data = get_can_data()
        can_data = p.recvline().strip()  # Replace this line with your actual data source
        can_data_queue.put(can_data)

def parse_can_data(data):
    newData = np.delete(data, [0, 2], 1)
    
    # ... (your existing parser code)

    with open("2c_disch_parsed.txt", "a") as file:
        # Modify the code to write to the file instead of print
        # For example, replace: print(a) with file.write(a)

if __name__ == "__main__":
    speed = multiprocessing.Value('d', 0.0)  # Placeholder for speed, replace with actual type
    SoC = multiprocessing.Value('d', 0.0)    # Placeholder for SoC, replace with actual type
    Temp = multiprocessing.Value('d', 0.0)   # Placeholder for Temp, replace with actual type
    R2D = multiprocessing.Value('i', 0)     # Placeholder for R2D, replace with actual type

    can_data_queue = multiprocessing.Queue()

    p_lcd = multiprocessing.Process(target=LCD, args=(speed, SoC, Temp, R2D, can_data_queue))
    p_can_data = multiprocessing.Process(target=CANData, args=(can_data_queue,))

    p_lcd.start()
    p_can_data.start()

    try:
        while True:
            if not can_data_queue.empty():
                data = can_data_queue.get()
                parse_can_data(data)
    except KeyboardInterrupt:
        p_lcd.terminate()
        p_can_data.terminate()
        p_lcd.join()
        p_can_data.join()
