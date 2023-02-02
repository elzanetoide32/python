#creando diccionario con dict()
diccionario=dict(nomber="lucas",apellido="dalto")
#las listas no puieden ser claves y usamos frozenset para meter conjuntos
diccionario={frozenset(["dalto","raqncio"]):"jasjj"}
#creando diccionario con fromkeys() valor x defecto none
diccionario=dict.fromkeys(["nombre","apellido"])
#creando diccionario con fromkeys() cambiando el valor x defecto a "no se"
diccionario=dict.fromkeys(["nombre","apellido"],"no se")


print(diccionario)