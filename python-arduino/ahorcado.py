import random

# Lista de palabras
lista_palabras = ["Python", "Java", "C++", "JavaScript", "HTML", "CSS"]

# Seleccionar una palabra al azar
palabra_elegida = random.choice(lista_palabras)

# Lista de letras acertadas
letras_acertadas = []

# Lista de letras falladas
letras_falladas = []

# Iniciar la partida
while len(letras_falladas) < 6 and len(letras_acertadas) != len(palabra_elegida):

    # Mostrar la palabra con los espacios en blanco
    for letra in palabra_elegida:
        if letra in letras_acertadas:
            print(letra, end=" ")
        else:
            print("_", end=" ")

    # Pedir al usuario que adivine una letra
    letra = input("Adivina una letra: ").upper()

    # Si la letra está en la palabra
    if letra in palabra_elegida:
        letras_acertadas.append(letra)
    else:
        letras_falladas.append(letra)

# Mostrar la palabra
print("La palabra es:", palabra_elegida)