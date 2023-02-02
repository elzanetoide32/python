numeros=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]

#creando una func lamba
multiplicar_por_dos= lambda x : x*2
print(multiplicar_por_dos(5))
#func para ver si es par o impar
def es_par(num):
    if (num%2==0):
        return True
#usando filter con una func comun
numeros_par=filter(es_par,numeros)
print(list(numeros_par))

#lo mismo pero con lambda
numeros_par2=filter(lambda numero:numero%2 == 0,numeros)
print(list(numeros_par2))