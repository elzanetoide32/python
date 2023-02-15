#con el firmata en el arduino
import pyfirmata 
puerto="\\.\COM3"
pin=(13)

print("conectando al arduino")
tarjeta=pyfirmata.Arduino(puerto)
print("conectado")
while True:
    print("encendiendo led")
    tarjeta.digital[pin].write(1)
    tarjeta.pass_time(1)
    print("apagando led")
    tarjeta.digital[pin].write(0)
    tarjeta.pass_time(1)
    
tarjeta.exit()




