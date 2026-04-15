from turtle import *
import random
ct=0
def playing_area():
    backdrop=Turtle()
    backdrop.speed(False)
    backdrop.setposition(-240,240)
    backdrop.left(180)
    backdrop.color("white")
    backdrop.hideturtle()
    backdrop.begin_fill()
    backdrop.left(90)
    backdrop.forward(480)
    backdrop.left(90)
    backdrop.forward(480)
    backdrop.left(90)
    backdrop.forward(480)
    backdrop.left(90)
    backdrop.forward(480)
    backdrop.end_fill()
def mmv(turtle):
    global turtles
    global ct
    turtle.forward(5)
    if abs(turtle.xcor())>=240:
        turtle.setheading(180-turtle.heading())
        turtle.setx(240*turtle.xcor()/abs(turtle.xcor()))
        turtles[f'turtle{ct}']=Turtle()
        turtles[f'turtle{ct}'].pu()
        turtles[f'turtle{ct}'].setpos(turtle.pos())
        turtles[f'turtle{ct}'].speed(0)
        turtles[f'turtle{ct}'].setheading(random.randint(0,360))
        col=f'{random.randint(0,16777216):X}'
        col='0'*(6-len(col))+col
        turtles[f'turtle{ct}'].color(f'#{col}')
        ct+=1
    if abs(turtle.ycor())>=240:
        turtle.setheading(-turtle.heading())
        turtle.setx(240*turtle.ycor()/abs(turtle.ycor()))
        turtles[f'turtle{ct}']=Turtle()
        turtles[f'turtle{ct}'].pu()
        turtles[f'turtle{ct}'].setpos(turtle.pos())
        turtles[f'turtle{ct}'].speed(0)
        turtles[f'turtle{ct}'].setheading(random.randint(0,360))
        col=f'{random.randint(0,16777216):X}'
        col='0'*(6-len(col))+col
        turtles[f'turtle{ct}'].color(f'#{col}')
        ct+=1
def mv(turtle):
    turtle.forward(5)
    if abs(turtle.xcor())>=240:
        turtle.setheading(180-turtle.heading())
        turtle.setx(240*turtle.xcor()/abs(turtle.xcor()))
    if abs(turtle.ycor())>=240:
        turtle.setheading(-turtle.heading())
        turtle.setx(240*turtle.ycor()/abs(turtle.ycor()))
def mvall():
    global turtles
    global turtle
    global mv
    mmv(turtle)
    key=list(turtles.keys()).copy()
    for i in key:
        mv(turtles[i])
    window.ontimer(mvall,20)

window = Screen()
window.bgcolor("black")

playing_area()
turtles={
    
}
turtle=Turtle()
turtle.speed(0)
turtle.setheading(random.randint(0,360))
turtle.begin_fill()
turtle.color("teal")
turtle.pencolor('black')


mvall()
window.mainloop()