#!/home/pi/Deepak/env/bin/python

from datetime import datetime
from pwn import process

# Global variable to store CAN messages
#can_data = ""

def CANData():
    global can_data
    p10 = process("./candump.sh")
    can_data = p10.recvline()

def saveData():
    global can_data
    timestamp = datetime.now()
    filename = timestamp.strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
    print(filename)
    while True:
        with open(filename, "a+") as f:
            f.write(can_data.decode('utf-8'))

        can_data = ""

if __name__ == "__main__":
    CANData()
    saveData()

