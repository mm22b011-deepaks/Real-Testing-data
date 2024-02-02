from datetime import datetime

from sparton_comm import pitch, yaw, roll, accelerometer, gyro
from sparton_comm import connect_serial
import time
import pandas as pd
connect_serial()
time.sleep(0.1)

df=pd.DataFrame(columns=['Time', 'Roll', 'Pitch', 'Yaw',
                         'ax', 'ay', 'az', 'gx', 'gy', 'gz'])

i=True

while True:

    current_time = datetime.now().time()
    formatted_time = current_time.strftime("%H:%M:%S")

    dat=pd.DataFrame({'Time': [formatted_time], 'Roll': [roll()], 'Pitch': [pitch()], 'Yaw':[yaw()],
                      'ax': [accelerometer()[0]], 'ay': [accelerometer()[1]], 'az': [accelerometer()[2]],
                      'gx': [gyro()[0]], 'gy': [gyro()[1]], 'gz': [gyro()[2]]})

    df= pd.concat([df,dat], ignore_index=True)
    time.sleep(0.01)
    df.to_csv('sparton_log.csv', index=False)



