
import turtle
ob = turtle.Turtle()
ob.speed(0)

cl = ["red","blue","green"]

def drawArt(d,angle,x,y):
    ob.up()
    ob.goto(x,y)
    ob.down()
    c = 0
    for i in range(1,300):
        ob.forward(d)
        ob.left(angle)
        d = d - 1
        ob.pencolor(cl[c])
        c = c + 1
        if (c>2):
            c = 0



drawArt(200,60,-10,-110)

