Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import serial
... import time
... import serial.tools.list_ports
... speeds = ['1200','2400', '4800', '9600', '19200', '38400', '57600', '115200']
... ports = [p.device for p in serial.tools.list_ports.comports()]
... port_name = ports[0]
... port_speed = int(speeds[-1])
... port_timeout = 10
... ard = serial.Serial(port_name, port_speed, timeout = port_timeout)
... time.sleep(1)
... ard.flushInput()
... try:
...     msg_bin = ard.read(ard.inWaiting())
...     msg_bin += ard.read(ard.inWaiting())
...     msg_bin += ard.read(ard.inWaiting())
...     msg_bin += ard.read(ard.inWaiting())
...     msg_str_ = msg_bin.decode()
... print(len(msg_bin))
... except Exception as e:
...     print('Error!')
... ard.close()
... time.sleep(1)
