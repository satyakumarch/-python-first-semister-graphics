
from ctypes import LibraryLoader
from turtle import Turtle, TurtleScreen


obj = library.apj()
t =Turtle.Turtle()
TurtleScreen.speed(0)
t.penup()
t.goto(360,40)
t.pendown()
t.pencolor("blue")
t.write("A.P.J",align="center",font=("arial",30))

t.penup()
t.goto(360,00)
t.pendown()
t.pencolor("red")
t.write("A.P.J",align="center",font=("arial",30))

t.penup()
t.goto(360,-40)
t.pendown()
t.pencolor("green")
t.write("A.P.J",align="center",font=("arial",30))

t.penup()
t.goto(360,-80)
t.pendown()
t.pencolor("gray")
t.write("A.P.J",align="center",font=("arial",30))
obj.draw()
turtle.done()