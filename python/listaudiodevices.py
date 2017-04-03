# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 17:33:34 2017

@author: PMay
"""

import sys
import traceback
import os
import pyaudio

def getaudiodevices():
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        print(i," >> ",p.get_device_info_by_index(i).get('name'))


def getaudiodevicesos():
    devices = os.popen("arecord -l")
    device_string = devices.read()
    device_string = device_string.split("\n")
    for line in device_string:
        if(line.find("card") != -1):
            print("hw:" + line[line.find("card")+5] + "," + line[line.find("device")+7])
            
def list_devices():
    # List all audio input devices
    print("List all audio input devices\n")
    p = pyaudio.PyAudio()
    i = 0
    n = p.get_device_count()
    print(n," devices")
    while i < n:
        dev = p.get_device_info_by_index(i)
        #if dev['maxInputChannels'] > 0:
        print(str(i) + ". " + dev['name'] + " // " + str(dev['maxInputChannels']) + " // " + str(dev['index']))
        i += 1


def main():
    try:
        getaudiodevices()
        list_devices()

    except IOError as ioe:

        sys.exit(1)

    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        print(''.join('!! ' + line for line in lines))  # Log it or whatever here
        sys.exit(1)

if __name__ == '__main__':
    main()


