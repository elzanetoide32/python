diccionario={
    "nombre":"lucas",
    "apellido":'dalto',
    "subs":10000
}
#nos devuelve un objeto dict_item
claves = diccionario.keys()

#obteniendo un elemento con get() (si no encuentra nada el programa conti nua)
valor_de_dddd=diccionario.get("dddd")
print("el programa continua")

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("nombre","subs")

print(claves)
