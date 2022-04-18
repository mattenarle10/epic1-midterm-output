#Matthew Enarle BSCS 1-B
from turtle import *
title("Mandala Pattern - Enarle")

bgcolor("black")
speed(3000)

def drawImaginaryLines():
    for times in range(18):
        color("dark blue")
        speed(11)
        circle(200)
        left(170)
        left(20)
        forward(15)

def drawRasengan():
    colors = ['white', 'lightblue', 'blue', 'lightgray']
    for line in range(180):
        penup()
        goto(0,0)
        pendown()
        left(1)
        for curve in range(4):
            if curve == 0:
                color( colors[0])
            elif curve == 1:
                color( colors[1])
            elif curve == 2:
                color( colors[2])
            elif curve == 3:
                color( colors[3])
            forward(50)
            left(50)


def drawShuriken():
    color("white")
    penup()
    goto(50,10)
    pendown()
    for i in range(300):
        left(60)
        forward(i)
        backward(i%800)
        left(145)
        forward(100)

def drawCircle():
    color('white')
    fillcolor('black')
    penup()
    goto(-5,-2)
    pendown()
    begin_fill()
    circle(5)
    end_fill()

drawImaginaryLines()
drawRasengan()
drawShuriken()
drawCircle()
hideturtle()
done()

#shuriken source: https://www.youtube.com/watch?v=vAZ5CycYDtE
#edited the shuriken to another level which makes it larger but not so sharper blades to make it seem like a cyclone
#edited the radius of the loop and its position to match perfectly with rasengan

#rasengan source: https://replicom/@Roger_Lai/mega-rasengan
#changed the colors of the rasengan to make it looke like a cyclone, and also edited the range so that the itiretation will be less and simple