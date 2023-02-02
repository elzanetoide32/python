import re  

texto='''hola maestro, esta es la cadena 1,10 como estas mi capitan
Esta es la segunda linea de texto 22
y Esta es la final definitiva mi capitan'''
#busqueda simple
resultado=re.findall("esta",texto)

#digitos numericos 0-9
resultado=re.findall(r"\d",texto)
#todo menos numeros
resultado=re.findall(r"\D",texto)
#caracteres alfanumericos
resultado=re.findall(r"\w",texto)
#todo menos alfanumericos
resultado=re.findall(r"\W",texto)
#espacios en blanco
resultado=re.findall(r"\s",texto)
#todo menos espacios en blaco
resultado=re.findall(r"\S",texto)
#menos saltos en linea
resultado=re.findall(r".",texto)
#saltos de linea
resultado=re.findall(r"\n",texto)
#cancelar caracteres especiales
resultado=re.findall(r"\.",texto)
#comienzo de una linea en conjunto, con el flags activa la multilinea
resultado=re.findall(r"^hola",texto,flags=re.M)
#final de la linea
resultado=re.findall(r"capitan$",texto)
#busca n cantidad de veces el valor
resultado=re.findall(r"\d{3}",texto)
#{n,m}-> al menos n, como maximo m
resultado=re.findall(r"\d{1,4}",texto)
#busca una cosa o otra
resultado=re.findall(r"\d{1,4}|hola",texto)

print(resultado)


