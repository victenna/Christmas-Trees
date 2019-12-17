import turtle,random

turtle.hideturtle()

wn=turtle.Screen()
wn.setup(1500,1300)
turtle.bgcolor('deep sky blue')

s=turtle.Shape('compound')
b=5
poly1=((40*b,-10*b),(40*b,20*b),(10*b,20*b),(40*b,50*b),\
       (20*b,50*b),(40*b,70*b),(30*b,70*b),(50*b,90*b),(70*b,70*b),(60*b,70*b),\
      (80*b,50*b),(60*b,50*b),(90*b,20*b),(60*b,20*b),(60*b,-10*b))
s.addcomponent(poly1,'green')

#star
turtle.up()
turtle.color('deep sky blue')
turtle.goto(220,400)
turtle.down()
turtle.setheading(35)
turtle.hideturtle()

turtle.begin_poly()
turtle.begin_fill()    
for i in range(5):
    turtle.fd(90)
    turtle.lt(144)
turtle.end_fill()
turtle.end_poly()

star=turtle.get_poly()
s.addcomponent(star,'gold')

def circle(R):
    turtle.begin_fill()    
    turtle.circle(R)
    turtle.end_fill()

turtle.goto(250,270)
turtle.begin_poly()
circle(15)
turtle.end_poly()
circ=turtle.get_poly()
s.addcomponent(circ,'blue')

turtle.goto(220,140)
turtle.begin_poly()
circle(20)
turtle.end_poly()
circ=turtle.get_poly()
s.addcomponent(circ,'red')

turtle.goto(340,140)
turtle.begin_poly()
circle(25)
turtle.end_poly()
circ=turtle.get_poly()
s.addcomponent(circ,'pink')

turtle.goto(370,250)
turtle.begin_poly()
circle(22)
turtle.end_poly()
circ=turtle.get_poly()
s.addcomponent(circ,'yellow')

turtle.goto(170,270)
turtle.begin_poly()
circle(22)
turtle.end_poly()
circ=turtle.get_poly()
s.addcomponent(circ,'violet')

wn.addshape('tree',s)
t=turtle.Turtle(shape='tree')
t.up()
t.tilt(90)
t.shapesize(0.3)

claus=turtle.Turtle()
claus.up()
image='Santa.gif'
wn.addshape(image)
claus.shape(image)
claus.goto(395,-350)

maiden=turtle.Turtle()
maiden.up()
image2='snow_maiden.gif'
wn.addshape(image2)
maiden.shape(image2)
maiden.goto(-395,350)

t.stamp()
q=0
for i in range(5):
    q=q+1
    q1=q%2
    if q1==0:
        shift=100
    if q1==1:
        shift=0
    
    for m in range(5):
        t.goto(-400+200*m+shift,-400+200*i)
        t.stamp()