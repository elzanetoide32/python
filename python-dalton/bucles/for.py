#funca para listas y tuplas y conjuntos

animales=["gato","perro","loro","cocodrilo"]
numeros=[10,20,30,39]
cadena="hola dalto"
#lista animales
for animal in animales:
    print(f"el animal es: {animal}")
    
#lista numero y x2 c/u
for numero in numeros:
    resultado=numero*2
    print(resultado)

#las 2 listas al mismo tiempop
for numero,animal in zip(animales,numeros):
    print(f"recorriendo la lista 1: {animal}")
    print(f"recorriendo la lista 2: {numero}")
    
    
for num in range(1,10)    :
    print(num)

#forma correcta de recorre una lista con su indice
for num in enumerate(numeros):
    print(num)
else:
    print("el bucle termino")


# para diccionarios

diccionario={
    "nombre":"lucas",
    "apellido": "dalto",
    "subs":10000 
}

for datos in diccionario.items():
    key=datos[0]
    value=datos[1]
    print(f"la key es: {key} y el valor: {value}")
    
#iterar una cadena de texto
for letra in cadena:
    print(letra)
    
#for en una sola linea de codigo *2 los numeros
numeros_dup=[x*2 for x in numeros]
print(numeros_dup)

#////////while

count=0
#mientras que la condicion se cumpla, el bucle se va a seguir ejecutando
while count<10:
    count+=1
    print(count)
   














