import pymysql

db= pymysql.connect("localhost","root","","python")

cursor= db.cursor()


cursor.execute("SELECT * FROM usuarios")

resultado= cursor.fetchall()

for fila in resultado:
    print(fila)

    nombre= fila[0]
    edad= fila[1]
    print("nombre",nombre,"edad",edad)


db.close()

