#while

quien= "luca"

i=0
while i<5:
    i+=1
    nombre= input("introduce tu nombre ")
    if quien !=nombre:
        print("no eres la persona")
    else:
        print("bienvenido luca, que quieres saber?")
        
        break
    

else:
    print("se exedio en el numero de intentos")




