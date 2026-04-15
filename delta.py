from turtle import *
import random
def upd():
    global turtle
    if abs(turtle.xcor())>=240:
        deltax*=-1
    if abs(turtle.ycor())>=240:
        deltay*=-1
    turtle.setx(turtle.xcor()+deltax)
    turtle.sety(turtle.ycor()+deltay)
window=Screen()
deltax=random.random()*2
deltay=random.random()*2
window.setup(-480,480)
turtle=Turtle()
window.mainloop()
    

