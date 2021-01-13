
import turtle
ob = turtle.Turtle()
cl =["red","blue","green","orange"]
ob.speed(50)

def draw_Art(d, angle, x, y):
     c = 0
     ob.up()
     ob.goto(x,y)
     ob.down()
     for i in range(1, 200):

         ob.pencolor(cl[c])
         ob.forward(d)
         ob.left(angle)
         c = c + 1
         if(c>2):
            c = 0
            d = d-1



#draw_Art(200,200,0,0)
#draw_Art(200,140,-100,0)
draw_Art(250,170,0,0)
draw_Art(150,160,-20,-200)
