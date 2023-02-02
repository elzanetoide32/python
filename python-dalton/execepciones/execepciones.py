#func que sume
def sumar():
    while True:
        #pidiendo numeros
        a=input ("numero 1: ")
        b=input("numero2: ")
        #intentamos convertirlos a entero y sumarlos
        try:
            resultado=int(a) + int(b)
            #si lanza una execpcion pedirle que reingrese los datos
        except ValueError as e:
            print("un numero")
            print(f"le execpcion es: {e}")
            #si salio bien terminamos el bucle
        else:
            break
        finally:
            print("execepcion de funalizacion")
    return resultado


print (sumar())

#creando mi propia execepcion
class MiExecepcion(Exception):
    def __init__(self,err):
        print(f"impresionante, cometistes el siguiente error {err}")
        
#lanzando mi propia execepcion
raise MiExecepcion("sjsjjssj, persona poco culta")




