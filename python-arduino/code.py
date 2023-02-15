import serial,time
ser=serial.Serial('COM3',9600,timeout=1)

while True:
    ser.write(b'p')
    time.sleep(1)
    ser.write(b'n')
    time.sleep(1)