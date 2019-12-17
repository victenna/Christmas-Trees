import turtle
import random
import time
t=turtle.Turtle()
t1=turtle.Turtle()
wn=turtle.Screen()
wn.setup(900,900)
wn.bgcolor('light blue')
image='christmas1.gif'
wn.addshape(image)
t.shape(image)
t.up()
wn.tracer(3)

t1=[]
clr=['red','yellow','blue','gold','gray','green','pink','violet']
posit=[(-20,270),(54,210),(-30,120),(32,92),(0,0),(75,-30),(-18,38),(-90,-130),\
       (47,-64),(0,-200),(50,-290),(100,-320),(-66,-300),(90,-190)]

def tree():
    for n in range(14):
        t1.append(turtle.Turtle('circle'))
        a=random.choice(clr)
        t1[n].color(a)
        t1[n].shapesize(1.5)
        t1[n].up()
        t1[n].setposition(posit[n])
        t1[n].showturtle()
        t1[n].stamp()

while True:
    tree()
    time.sleep(0.1)

         
       
    
    
