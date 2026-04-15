from turtle import *
import random
ct=0
mflag=False
def handle():
    global ismoving
    global turtles
    global mflag
    if mflag:
        mflag=not mflag
        key=list(turtles.keys()).copy()
        for i in key:
            if i not in ismoving:
                ismoving.append(i)
                exec(f"mvelse('{i}')")
    window.ontimer(handle,20)
def mvelse(turtle):
    global turtles
    turtles[turtle].forward(5)
    if turtles[turtle].xcor()<=-240:
        turtles[turtle].setheading(180-turtles[turtle].heading())
        turtles[turtle].setx(-240)
    if turtles[turtle].xcor()>=240:
        turtles[turtle].setheading(-180-turtles[turtle].heading())
        turtles[turtle].setx(240)
    if abs(turtles[turtle].ycor())>=240:
        turtles[turtle].setheading(0-turtles[turtle].heading())
        turtles[turtle].sety(240*turtles[turtle].ycor()/abs(turtles[turtle].ycor()))
    window.ontimer(exec(f'mvelse("{turtle}")'),20)
def turn_left():
    global leftq
    leftq=True
def turn_right():
    global rightq
    rightq=True
def unturn_left():
    global leftq
    leftq=False
def unturn_right():
    global rightq
    rightq=False
pastpos=(0,0)
def move():
    global ct
    global leftq
    global turtles
    global mflag
    turtle.forward(5)
    if leftq:
        turtle.left(10)
    elif rightq:
        turtle.right(10)
    if turtle.xcor()<=-240:
        turtles[f'turtle{ct}']=Turtle()
        turtles[f'turtle{ct}'].pu()
        turtles[f'turtle{ct}'].speed(0)
        turtles[f'turtle{ct}'].setpos(turtle.pos())
        turtles[f'turtle{ct}'].pd()
        turtles[f'turtle{ct}'].setheading(random.randint(0,360))
        col=f'{random.randint(0,16777216):X}'
        col='0'*(6-len(col))+col
        turtles[f'turtle{ct}'].color(f'#{col}')
        ct+=1
        mflag=True
        turtle.setheading(180-turtle.heading())
        turtle.setx(-240)
    if turtle.xcor()>=240:
        turtles[f'turtle{ct}']=Turtle()
        turtles[f'turtle{ct}'].pu()
        turtles[f'turtle{ct}'].speed(0)
        turtles[f'turtle{ct}'].setpos(turtle.pos())
        turtles[f'turtle{ct}'].pd()
        turtles[f'turtle{ct}'].setheading(random.randint(0,360))
        col=f'{random.randint(0,16777216):X}'
        col='0'*(6-len(col))+col
        turtles[f'turtle{ct}'].color(f'#{col}')
        ct+=1
        mflag=True
        turtle.setheading(-180-turtle.heading())
        turtle.setx(240)
    if abs(turtle.ycor())>=240:
        turtles[f'turtle{ct}']=Turtle()
        turtles[f'turtle{ct}'].pu()
        turtles[f'turtle{ct}'].speed(0)
        turtles[f'turtle{ct}'].setpos(turtle.pos())
        turtles[f'turtle{ct}'].pd()
        turtles[f'turtle{ct}'].setheading(random.randint(0,360))
        col=f'{random.randint(0,16777216):X}'
        col='0'*(6-len(col))+col
        turtles[f'turtle{ct}'].color(f'#{col}')
        ct+=1
        mflag=True
        turtle.setheading(0-turtle.heading())
        turtle.sety(240*turtle.ycor()/abs(turtle.ycor()))
    window.ontimer(move,10)
leftq=False
rightq=False
window = Screen()
window.bgcolor("black")
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
playing_area()
turtles={
    
}
ismoving=[]
turtle=Turtle()
turtle.begin_fill()
turtle.color("teal")
turtle.pencolor('black')
window.listen()
window.onkeypress(turn_left, "Left")
window.onkey(unturn_left,"Left")
window.onkeypress(turn_right, "Right")
window.onkey(unturn_right,"Right")
turtle.speed(0)

move()
handle()
window.mainloop()