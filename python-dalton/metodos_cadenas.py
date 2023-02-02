cadena1="hola soy dalto"
cadena2="bienbenido maquinola"

#convierte a mayusculas
mayusc= cadena1.upper()
#convierte a minuscula
minusc= cadena1.lower()
#primer letra en mayuscula
primera_letra= cadena1.capitalize()
#buscamos una cadena en otra cadena (devuelve en la posicion si no encuentra nada devuelve -1)
find= cadena1.find("hola")
#busqueda index lo mismo que find pero si no encuentra coincidencia lanza una execepcion
index= cadena1.index("hola")
#si es numerico devuelve true
numerico= cadena1.isnumeric()
#si es alpha numerico devuelve true, los espacion cuentan como no
alpha= cadena1.isalpha()
#cuenta las coincidencias
contar= cadena1.count("a")
#cuantos caracteres tiene una cadena
len= len(cadena1)
# verifica si una cadena empieza con otra cadena dada, si es asi devuelve true
empieza_con= cadena1.startswith("hola")
# verifica si una cadena termina con otra cadena dada, si es asi devuelve true
termina_con= cadena2.endswith("hola")
# reemplaza un pedazo de cadena x otra
reem= cadena1.replace("la","lu")
#separa cadenas con la cadena que le pasemos devuelve una lista
separate= cadena1.split()

print(separate)