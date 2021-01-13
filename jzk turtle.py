
import turtle
ob = turtle.Turtle()
ob.speed(0)
cl = ["red","blue","pink","orange","green","indigo"]

def drawArt(d,angle,x,y):
    c = 0
    ob.up()
    ob.goto(x,y)
    ob.down()
    for i in range(1,200):
        ob.forward(d)
        ob.left(angle)
        ob.pencolor(cl[c])
        d = d - 1
        c = c + 1
        if (c>5):
            c = 0

drawArt(200,-70,0,0)



