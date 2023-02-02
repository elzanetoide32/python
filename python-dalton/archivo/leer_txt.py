archivo=open("archivo\\testo de dalto.txt", encoding="UTF-8")
#leer archivo completo
#print(archivo.read())

#leer linea x linea
line1=archivo.readlines()
#leer una sola linea
line=archivo.readline(10000)
#cerrar el archivo
archivo.close()
print(line)

#abriendo el archivo con with open no es necesario cerrarlo
with open("archivo\\testo de dalto.txt", encoding="UTF-8") as archivo:
    print(archivo.read())
    
with open("archivo\\testo de dalto.txt",'w', encoding="UTF-8") as archivo:
    #sobrescribiendo el archivo
    #archivo.write("jajsjsj te cage")
    archivo.writelines(["hola maestro como andas\n ", "misericordia"])
    


















