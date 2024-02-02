import serial.tools.list_ports
ser = None
ser_flag=False

import time as tim
import datetime


flag=0

def time():
    t =  datetime.datetime.now()
    t = str(t)
    t = t[17:]
    t = float(t)
    return t


def roll():
    flag = 0
    ser.flush()
    while flag == 0:
        ser.write("roll di.\r\n".encode('utf-8'))
        t = time()
        while abs(t-time() < 0.01) and flag == 0:
            read = ser.readline().decode('utf-8')
            #print(read)
            for line in read.split('\r') :
                if line.startswith ("roll ="):
                    roll = line.split("=")
                    roll = float(roll[1])
                    #print "roll : "+str(roll)
                    flag = 1
    return roll

def pitch():
    flag = 0
    ser.flush()
    while flag == 0:
        ser.write("pitch di.\r\n".encode('utf-8'))
        t = time()
        while abs(t-time() < 0.01) and flag == 0:
            read = ser.readline().decode('utf-8')
            #print(read)
            for line in read.split('\r') :
                if line.startswith ("pitch ="):
                    roll = line.split("=")
                    roll = float(roll[1])
                    #print "roll : "+str(roll)
                    flag = 1
    return roll

def yaw():
    flag = 0
    ser.flush()
    while flag == 0:
        ser.write("yaw di.\r\n".encode('utf-8'))
        t = time()
        while abs(t-time() < 0.01) and flag == 0:
            read = ser.readline().decode('utf-8')
            #print(read)
            for line in read.split('\r') :
                if line.startswith ("yaw ="):
                    roll = line.split("=")
                    roll = float(roll[1])
                    #print "roll : "+str(roll)
                    flag = 1
    return roll


def accelerometer():
    flagx = 0
    flagy = 0
    flagz = 0
    ser.flush()
    while flagx == 0 or flagy == 0 or flagz == 0:
        ser.write("accelp di.\r\n".encode('utf-8'))
        t = time()
        while abs(t - time() < 0.01) and (flagx == 0 or flagy == 0 or flagz == 0):
            read = ser.readline().decode('utf-8')
            for line in read.split('\r'):
                if line.startswith("accelp = 00--"):
                    ax = line.split("--")
                    ax = float(ax[1])
                    # print "ax : "+str(ax)
                    flagx = 1
                if line.startswith("01--"):
                    ay = line.split("--")
                    ay = float(ay[1])
                    # print "ay : "+str(ay)
                    flagy = 1
                if line.startswith("02--"):
                    az = line.split("--")
                    az = float(az[1])
                    # print "az : "+str(az)
                    flagz = 1
        a = [ax, ay, az]
        return a

def gyro():
    flagx = 0
    flagy = 0
    flagz = 0
    ser.flush()
    while flagx == 0 or flagy == 0 or flagz == 0:
        ser.write("gyrop di.\r\n".encode('utf-8'))
        t = time()
        while abs(t-time() < 0.01) and (flagx == 0 or flagy == 0 or flagz == 0) :
            read = ser.readline().decode('utf-8')
            for line in read.split('\r') :
                if line.startswith ("gyrop = 00--"):
                    gx = line.split("--")
                    gx = float(gx[1])
                    #print "gx : "+str(gx)
                    flagx = 1
                if line.startswith ("01--"):
                    gy = line.split("--")
                    gy = float(gy[1])
                    #print "gy : "+str(gy)
                    flagy = 1
                if line.startswith ("02--"):
                    gz = line.split("--")
                    gz = float(gz[1])
                    #print "gz : "+str(gz)
                    flagz = 1
    g = [gx,gy,gz]
    return g

#SERIAL CONNECTION SIMPLY DO NOT TOUCH
def connect_serial():
    global ser, ser_flag
    serial_txt = 'Refreshing'
    ports = list(serial.tools.list_ports.comports())
    arduino_port = None


    for port in ports:
        if "USB Serial Port" in port.description:
            arduino_port = port.device

            break

    if arduino_port:
        serial_txt = f"RafTrack vPro found on {arduino_port}"
        baud_rate = 115200
        try:
            ser = serial.Serial(arduino_port, baud_rate)
            print(f"Connected to RafTrack vPro on {ser.name}")
            ser_flag = True
            roll()


        except serial.SerialException as e:
            serial_txt = f"Error: {e}"
            ser_flag = False

    else:
        print("RafTrack vPro not found. Please make sure your device is connected.")
        ser_flag = False



connect_serial()







