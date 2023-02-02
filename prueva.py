import os
print("\n\t\t\tAhorcado \n\n\tIngrese una palabra")
pal = input("\n\t>>> ")
print("\n\tComenzar juego")
os.system("pause")
os.system("cls")
lista =[]
piv = ""
for i in range (0 , len(pal)):
    if pal[i] != "$":
        piv += pal[i].replace(pal[i], "$")
        lista.append(piv[i])
intentos = 6
while intentos >= 1:
    letr = input("\n\tIngresa una letra \n\t>>> ")
    if letr in pal:
        for i in range(0, len(pal)):
            if letr == pal[i]:
                lista[i] = pal[i]
                for i in range (0 , len( lista)):
                    if i == 0:
                        print("\n\t",lista[i], end = "")
                    else:
                        print(lista[i], end = "")
        print("\n\t")
        os.system ("pause")
    else:
        intentos -=1
        print("\n\tNo existe la letr %s"%letr)
        print("\n\tTe quedan %d intentos"%intentos)
    if all(i != "$" for i in lista):
        os.system("cls")
        print("\n\tHas ganado")
        break
if intentos == 0:
    print("\n\tHas perdido\n\tLa palabra era: %s"%pal)






