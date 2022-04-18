#Matthew Enarle BSCS 1-B
from turtle import *

bgcolor("black")
speed(3000)

def drawRasengan():
    colors = ['yellow', 'orange', 'blue', 'silver']
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
    color("red")
    penup()
    goto(100,92)
    pendown()
    for i in range(100):
        left(120)
        forward(i)
        backward(i%800)
        left(145)
        forward(200)


def drawCenter():
    penup()
    goto(-5,-5)
    pendown()
    for times in range(36):
        color("white")
        speed(11)
        circle(20)
        left(170)
        left(20)
        forward(15)

drawShuriken()
drawCenter()
drawRasengan()


hideturtle()
done()


#shuriken source: https://www.youtube.com/watch?v=vAZ5CycYDtE
#modified his design wherein the shuriken acts as the spikes of a beyblade, more specifically, edited the loop iteration and radius and the number of spikes

#rasengan source: https://replit.com/@Roger_Lai/mega-rasengan
#changed the colors of the rasengan to make it seem like the body of the blade

