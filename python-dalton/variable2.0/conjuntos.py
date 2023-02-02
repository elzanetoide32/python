#creando un conunto con set()
conjunto=set(["dato1","dato2"])
#metiendo un conjunto de otro conjunto
conjunto1=frozenset(["dato1","dato2"])
conjunto2={conjunto1,"dato3"}
print(conjunto)

#teoria de conjuntos
conjunto1={1,3,5,6}
conjunto2={1,3,9,5}
#verificando si es un subconjunto
resultado=conjunto2.issubset(conjunto1)
resultado1=conjunto2<=conjunto1
#verificando si es un conjunto
resultado2=conjunto2.issuperset(conjunto1)
resultado3=conjunto2>conjunto1
#verificando si hay algun elemento igual
resultado=conjunto2.isdisjoint(conjunto1)

print(conjunto)