import turtle

wn= turtle.Screen()
wn.title("pong")
wn.bgcolor("black")
wn.setup(width= 800, height= 600)
wn.tracer(0)



jugadorA= turtle.Turtle()
jugadorA.speed(0)
jugadorA.shape("square")
jugadorA.color("white")
jugadorA.penup()
jugadorA.goto(-350,0)
jugadorA.shapesize(stretch_wid= 5, stretch_len= 1)

jugadorB= turtle.Turtle()
jugadorB.speed(1000)
jugadorB.shape("square")
jugadorB.color("white")
jugadorB.penup()
jugadorB.goto(350,0)
jugadorB.shapesize(stretch_wid= 5, stretch_len= 1)

pelota= turtle.Turtle()
pelota.speed(0)
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0,0)
pelota.dx= 3
pelota.dy= 3



divicion= turtle.Turtle()
divicion.color("white")
divicion.goto(0,400)
divicion.goto(0,-400)

def jugadorA_up():
    y= jugadorA.ycor()
    y += 20
    jugadorA.sety(y)

def jugadorA_down():
    y= jugadorA.ycor()
    y -= 20
    jugadorA.sety(y)




def jugadorB_up():
    y= jugadorB.ycor()
    y += 20
    jugadorB.sety(y)

def jugadorB_down():
    y= jugadorB.ycor()
    y -= 20
    jugadorB.sety(y)

wn.listen()
wn.onkeypress(jugadorA_up, "w")
wn.onkeypress(jugadorA_down, "s")
wn.onkeypress(jugadorB_up, "Up")
wn.onkeypress(jugadorB_down, "Down")







while True:
    wn.update()

    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)





    if pelota.ycor()>290:
        pelota.dy +=-1

    if pelota.ycor()<-290:
        pelota.dy +=-1


    if pelota.xcor()>390:
        pelota.goto(0,0)
        pelota.dx +=-1

    if pelota.xcor()<-390:
        pelota.goto(0,0)
        pelota.dx +=-1

    if((pelota.xcor()>340 and pelota.xcor()<350)
          and (pelota.ycor()< jugadorB.ycor() + 50
          and pelota.ycor()> jugadorB.ycor() -50)):
          pelota.dx +=-1
