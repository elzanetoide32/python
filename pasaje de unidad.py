print(
" 1 de mm a km"
" 2 de mm a hm"
" 3 de mm a dam"
" 4 de mm a m"
" 5 de mm a dm"
" 6 de mm a cm"

" 7 de km a hm"
" 8 de km a dam"
" 9 de km a m"
" 10 de km a dm"
" 11 de km a cm"
" 12 de km a mm"

" 13 de cm a mm"
" 14 de cm a dm"
" 15 de cm a m"
" 16 de cm a dam"
" 17 de cm a hm "
" 18 de cm a km"


" 19 de dm a mm"
" 20 de dm a cm"
" 21 de dm a m"
" 22 de dm a dam"
" 23 de dm a hm"
" 24 de dm a km"

" 25 de m a mm"
" 26 de m a cm"
" 27 de m a dam"
" 28 de m a hm"
" 29 de m a km"

" 30 de dam a mm"
" 31 de dam a cm"
" 32 de dam a dm"
" 33 de dam a m"
" 34 de dam a hm"
" 35 de dam a km"

" 36 de hm a mm"
" 37 de hm a cm"
" 38 de hm a dm"
" 39 de hm a m"
" 40 de hm a dam"
" 41 de hm a km"

)
opcion= int(input("seleccione una opcion: "))

if opcion ==1:
    numero1= float(input("cual es el numero en mm:"))
    resultado1= numero1/1000000 
    print("en km es: ")
    print(resultado1 )

if opcion==2:
    numero2= float(input("cual es el numero en mm:"))
    resultado2= numero2/100000
    print("en hm es:")
    print(resultado2)

if opcion==3:
    numero3= float(input("cual es el numero en mm:"))
    resultado3= numero3/10000
    print("en dam es:")
    print(resultado3)

if opcion==4:
    numero4= float(input("cual es el numero en mm:"))
    resultado4= numero4/1000
    print("en m es:")
    print(resultado4)

if opcion==5:
    numero5= float(input("cual es el numero en mm:"))
    resultado5= numero5/100
    print("en dm es:")
    print(resultado5)

if opcion== 6:
    numero6= float(input("cual es el numero en mm:"))
    resultado6= numero6/10
    print("en cm es:")
    print(resultado6)

if opcion==7:
    numero7= float(input("cual es el numero en km:"))
    resultado7= numero7*10
    print("en hm es:")
    print(resultado7)

if opcion==8:
    numero8= float(input("cual es el numero en km:"))
    resultado8= numero8*100
    print("en dam es:")
    print(resultado8)

if opcion==9:
    numero9= float(input("cual es el numero en km:"))
    resultado9=numero9*1000
    print("en m es:")
    print(resultado9)

if opcion==10:
    numero10= float(input("cual es el numero en km:"))
    resultado10=numero10*10000
    print("en dm es:")
    print(resultado10)

if opcion==11:
    numero11= float(input("cual es el numero en km:"))
    resultado11=numero11*100000
    print("en cm es:")
    print(resultado11)

if opcion==12:
    numero12= float(input("cual es el numero en km:"))
    resultado12=numero12*1000000
    print("en mm es:")
    print(resultado12)

if opcion==13:
    numero13= float(input("cual es el numero en cm:"))
    resultado13= numero13*10
    print("en mm es:")
    print(resultado13)

if opcion==14:
    numero14= float(input("cual es el numero en cm:"))
    resultado14= numero14/10
    print("en dm es:")
    print(resultado14)

if opcion==15:
    numero15= float(input("cual es el numero en cm:"))
    resultado15= numero15/100
    print("en m es:")
    print(resultado15)

if opcion==16:
    numero16= float(input("cual es el numero en cm: "))
    resultado16= numero16/1000
    print("en dam es:")
    print(resultado16)

if opcion==17:
    numero17= float(input("cual es el numero en cm:"))
    resultado17= numero17/10000
    print("en hm es:")
    print(resultado17)

if opcion==18:
    numero18= float(input("cual es el numero en cm:"))
    resultado18= numero18/100000
    print("en km es:")
    print(resultado18)

if opcion==19:
    numero19= float(input("cual es el numero en dm:"))
    resultado19= numero19*100
    print("en mm es:")
    print(resultado19)

if opcion==20:
    numero20= float(input("cual es el numero en mm:"))
    resultado20= numero20*10
    print("en cm es:")
    print(resultado20)

if opcion==21:
    numero21= float(input("cual es el numero en dm:"))
    resultado21= numero21/10
    print("en m es:")
    print(resultado21)

if opcion==22:
    numero22= float(input("cual es el numero en dm:"))
    resultado22= numero22/100
    print("en dam es:")
    print(resultado22)

if opcion==23:
    numero23= float(input("cual es el numero en dm:"))
    resultado23= numero23/1000
    print("en hm es:")
    print(resultado23)

if opcion==24:
    numero24= float(input("cual es el numero en dm:"))
    resultado24= numero24/10000
    print("en km es:")
    print(resultado24)

if opcion==25:
    numero25=float(input("cual es el numero en m:"))
    resultado25= numero25*1000
    print("en mm es: ")
    print(resultado25)

if opcion==26:
    numero26=float(input("cual es el numero en m:"))
    resultado26= numero26*100
    print("en cm es: ")
    print(resultado26)

if opcion==27:
    numero27=float(input("cual es el numero en m:"))
    resultado27=numero27*10
    print("en dm es: ")
    print(resultado27)

if opcion==28:
    numero28=float(input("cual es el numero en m:"))
    resultado28= numero28/10
    print("en dam es: ")
    print(resultado28)

if opcion==29:
    numero29= float(input("cual es el numero en m:"))
    resultado29= numero29/100
    print("en km es: ")
    print(resultado29)

if opcion==30:
    numero30=float(input("cual es el numero en dam:"))
    resultado30= numero30*10000
    print("en mm es: ")
    print(resultado30)

if opcion==31:
    numero31=float(input("cual es el numero en dam:"))
    resultado31= numero31*1000
    print("en cm es: ")
    print(resultado31)

if opcion==32:
    numero32=float(input("cual es el numero en dam:"))
    resultado32= numero32*100
    print("en dm es: ")
    print(resultado32)

if opcion== 33:
    numero33=float(input("cual es el numero en dam:"))
    resultado33= numero33*10
    print("en m es: ")
    print(resultado33)

if opcion==34:
    numero34= float(input("cual es el numero en dam:"))
    resultado34= numero34/10
    print("en hm es: ")
    print(resultado34)

if opcion==35:
    numero35=float(input("cual es el numero en dam:"))
    resultado35=numero35/100
    print("en km es: ")
    print(resultado35)

if opcion==36:
    numero36=float(input("cual es el numero en hm:"))
    resultado36=numero36*100000
    print("en mm es: ")
    print(resultado36)

if opcion==37:
    numero37=float(input("cual es el numero en hm:"))
    resultado37= numero37*10000
    print("en cm es: ")
    print(resultado37)

if opcion==38:
    numero38=float(input("cual es el numero en hm:"))
    resultado38=numero38*1000
    print("en dm es: ")
    print(resultado38)

if opcion==39:
    numero39=float(input("cual es el numero en hm:"))
    resultado39= numero39*100
    print("en m es: ")
    print(resultado39)

if opcion==40:
    numero40=float(input("cual es el numero en hm:"))
    resultado40=numero40*10
    print("en dam es: ")
    print(resultado40)

if opcion==41:
    numero41=float(input("cual es el numero en hm:"))
    resultado41=numero41/10
    print("en km es: ")
    print(resultado41)


