from pyfirmata import Arduino
import time 
led=13
arduino=Arduino("COM3")
for x in range(10):
    arduino.digital[led].write(1)
    time.sleep(.500)
    arduino.digital[led].write(0)
    time.sleep(.500)
    
tarjeta.exit()