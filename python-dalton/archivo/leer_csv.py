import csv
from numpy import False_
import pandas as pd
with open("archivo\\datos.csv") as archivo:
    reader=csv.reader(archivo)
    for row in reader:
        print(row)
        
#con pandas
df=pd.read_csv("archivo\\datos.csv")
df2=pd.read_csv("archivo\\datos.csv")
#obteniendo los datos de la columna nombre
nombre=df["nombre"]
#ordenando el df por la edad
df_ordenas=df.sort_values("edad")
#ordenando los datos descendente
df_ordendes=df.sort_values("edad",ascending=False_)

#cocatenando los 2 df
df_concat=pd.concat([df,df2])
#primeras fila
primerafil=df.head(3)
#a las ultimas filas
ultimafil=df.tail(3)
#cantidad de row y col
filas_total,columnas_tptal,=df.shape 
#data estadistica del df
df_info= df.describe()
#elemento especifico del df con  loc
elemesp=df.loc[2,"edad"]
#elemento especifico del df con  iloc
elemesp=df.iloc[2,2]
#todas las columnas de una columna
apellido=df.iloc[:,1]
#fila 3 con loc
fila3=df.loc[1,:]
mayor=df.loc[df["edad"]>18,:]

print(mayor)












