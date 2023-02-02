from pygame import mixer
mixer.init()
cancion= str(input("selecciona la cancion: "))
mixer.music.load(cancion)
#mixer.music.set_volumen(0.7)
mixer.music.play()

while True:
    print("pulsa p para parar")
    print("pulsa r para reanudar")
    print("pulsa e para otra cancion")
    print("q para salir")
    opcion= input(">>>")
    if opcion=="P":
        mixer.music.pause()
    elif opcion=="r":
        mixer.music.unpause()
    elif opcion=="q":
        mixer.misic.stop()
        break
    elif opcion== "e":
        mixer.music.stop()
        cancion=str(input("selecione a cancion: "))
        mixer.music.load(cancion)
       # mixer.music.set_volumen(0.7)
        mixer.music.play()


