#creando una lista con list()
lista  = list(["hola", "dalto", 34,56,23, True])
#devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)
#agregando un elemento a la lista
lista.append("JAJAJAJA")
#agregando un elemento a la lista en un indice especifico
lista.insert(2, "TOMA MAMA")
#agregando varios elementos a la lista
lista.extend([False, 2030])
#eliminando un elemento de la lista (por su indice)
lista.pop(3) #-1 para eliminar el ultimo, -2 para eliminar el anteultimo, y asi sucesivamente
#removiendo un elemento de la lista por su valor
lista.remove("TOMA МАМА")
#eliminando todos los elementos de la lista
#lista.clear()
#ordena la lista de forma ascedente(si usamos el parametro reverse=true lo ordena en reversa)
lista.sort()
#invirtiendo los elementos de una lista
lista.reverse()
#verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(56)


print(lista)
