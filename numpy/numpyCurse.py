# diferencia entre listas (con distintos tipos de datos, conjunto de valores)  y arrays (con el mismo tipo de datos, valores independientes)  ///i de int, d de decomales
# import array as ar
# matriz = ar.array('i', [1, 2, 3, 4, 5, 6, 7, 8]) creando matris con array
# for ar in matriz:
#     print(ar)

import numpy as np      
# matriz=np.array([1,2,3,4,5,6,7])
# print(matriz) creando matris lineal

# lista=[1,3,5,7,9]
# matriz=np.array([2,4,6,8])
# lista.append(11)
# print(lista)  añadiendo datos a lista
# matriz=matriz + np.array([8])
# print(matriz)

# a= np.array([1,2,3])
# b= np.array([4,5,6])
# print(a+b) sumar matrices

# m2d= np.array([[1,2,3],[4,5,6]]) (matriz de 2 dimenciones)
# print(m2d)

# lista=[[1,2,3],[4,5,6],[7,8,9]]
# matriz=np.array(lista)
# print(matriz)

# m= np.arange(15).reshape(3,5) #crear matris rapidamente
# print(m.shape) # filas y columnas
# print(m.ndim) #dimensiones de la matris
# print(m.size)#elementos de la matris
# print(m)

# m= np.arange(24).reshape(2,3,4) #crear matris de 3d
# print(m)

# m= np.arange(24).reshape(4,6)
# print(m [3,4]) #ubicacion de elemento
# print(m)

# m1=np.array([90,50,60,40,80,30,20,])
# print(np.sort(m1))

# m2=np.array([2,3])
# print(np.power(m2,3))
# print(np.array(m2**2))#lo mismo que arriba
# print(np.array(m1 >=40))#lo que no cumple la condicion es false sino true
# print(np.array(m1 max()))
# print(np.array(m1 min()))

# m1=np.array([2,3,4,5,6])
# m2=np.array([11,22,7,8,9,10])
# print(np.concatenate((m1,m2)))

#m= np.random.randint(10, size=(3,3))
#m=np.random.rand(2,2)
# m=np.random.choice([3,5,69,8,7,5,3], size=(2,3))#culaquiera de los nue¿mros de la matris
# print(m)

# m= np.array([[1,1],[1,1]])
# m2=np.array([[8,8],[8,8]])
# print(m)
# print(m2)
# #print(np.sum(m, axis=0)) #sumar verticalmente
# print(np.concatenate([m,m2], axis=1))

# m= np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(m)
# print(np.amax(m))
# print(np.amin(m,1))
# print(np.ptp(m, axis=1))
# print(np.median(m, axis=0))
# print(np.mean(m))
# print(np.average(m))
# print(np.std(m))

# m=np.array([[1,-1,2],[3,2,0]])
# print(m)
# m1=np.array([[1, 2, 3]])
# print(np.transpose(m1))

# a=np.array([[2,1,-2],[3,0,1],[1,1,-1]])
# b=np.array([[-3],[5],[-2]])
# x=np.linalg.solve(a,b)
# print(x)
# print(np.allclose(np.dot(a,x),b))

m1=np.array([[2,7,3],[2,8,2],[1,3,1]])
m2= np.array([[1,1,0]])
m2.shape=(3,1)
print(m2)
print(np.linalg.solve(m1,m2))












