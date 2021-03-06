#Adafruit implementation of the DS18B20 underwater temperature
import os
import glob
import time
import subprocess

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

class Temperature():
    def __init__(self):
        pass
    def read_temp_raw(self):
        catdata = subprocess.Popen(['cat', device_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = catdata.communicate()
        out_decode = out.decode('utf-8')
        lines = out_decode.split('\n')
        return lines


    def read_temp(self):
        lines = self.read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.5)
            lines = self.read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos + 2:]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
            # uncomment to print temp in console
            #print temp_f
            return temp_f