import turtle
import time
import random
posponer= 0.1



#configuracion de la ventana
wn= turtle.Screen()
wn.title("Juego de snake")
wn.bgcolor("black")
wn.setup(width= 600, height= 600)
wn.tracer(0)

#cabeza serpiente
cabeza= turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direccion= "stop"

#comida
comida= turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

#cuerpo serpiente
segmento= [

]

#funciones

def arriba():
    cabeza.direccion="up"

def abajo():
    cabeza.direccion="down"

def izquierda():
    cabeza.direccion="left"

def derecha():
    cabeza.direccion="right"

def mov():
    if cabeza.direccion=="up":
        y=cabeza.ycor()
        cabeza.sety(y +20)
        
    if cabeza.direccion== "down":
       y=cabeza.ycor()
       cabeza.sety(y - 20)

    if cabeza.direccion=="left":
        x=cabeza.xcor()
        cabeza.setx(x -20)

    if cabeza.direccion=="right":
        x=cabeza.xcor()
        cabeza.setx(x +20)
    
#teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

while True:
    wn.update()
    #coliciones bordes
    if cabeza.xcor()>280 or cabeza.xcor()<-280 or cabeza.ycor()>280 or cabeza.ycor()<-280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direccion="stop"


    #coliciones comida
    if cabeza.distance(comida)<20:
        x=random.randint(-280,280)
        y= random.randint(-280,280)
        comida.goto(x,y)

        nuevo_segmento= turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("grey")
        nuevo_segmento.penup()
        segmento.append(nuevo_segmento)

        #cuerpo de la serp
    totalSeg= len(segmento)
    for index in range (totalSeg -1, 0, -1):
        x= segmento[index -1].xcor()
        y = segmento[index -1]. ycor()
        segmento[index].goto(x,y)
    if totalSeg>0:
        x= cabeza.xcor()
        y= cabeza.ycor()
        segmento[0].goto(x,y)


    mov ()
    time.sleep(posponer)





