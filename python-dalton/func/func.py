#creando una funcion
def saludar():
    print("hola lucas, como estas?")
#ejecutando la func simple
saludar()
#creaar una func con parametros 
def saludar1(nombre,sexo):
    sexo=sexo.lower()
    if (sexo=="mujer"):
        adjetivo="reina"
    elif(sexo=="hombre"):
        adjetivo="titan"
    else:
        adjetivo="amor"
    print(f"hola {nombre}, mi {adjetivo} como estas?")
    
saludar1("lucas","hombre")

#func que retorne valores
def calculo(num):
    char="abcdefghijklmnñopqrstuvwxyz"
    num_int=str(num)
    num=int(num_int[0])
    c1=num-2
    c2=num
    c3=num-5
    contraceña=f"{char[c1]}{char[c2]}{char[c3]}{num*2}"
    return (contraceña,num)

passw=calculo(1)
frase=f"tu nuevaclave es: {passw}"
print(frase)



#utilizando el operador args como argumento
def suma(*numeros):
    return sum(numeros)
resultado=suma(5,55,8,88,9,66,3,10)
print(resultado)
#forma optima de sumar valores
def suma1(numeros):
    return sum([*numeros])
resultado4=suma1([5,55,8,88,9,66,3,10])
print(resultado4)

#creando una func de 3 parametros
def frase(nombre,apellido,adjetivo):
    return f"hola {nombre} {apellido}, sos muy {adjetivo}"

print(frase("lucas","pepe","capo"))

#utilizando keyword arguments
def frase(nombre,apellido,adjetivo="capo"):
    return f"hola {nombre} {apellido}, sos muy {adjetivo}"

print(frase("lucas","pepe",adjetivo="inteligente"))





