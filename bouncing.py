from turtle import *
# import turtle
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
    global leftq
    turtle.forward(5)
    if leftq:
        turtle.left(10)
    elif rightq:
        turtle.right(10)
    if turtle.xcor()<=-240:
        turtle.setheading(180-turtle.heading())
        turtle.setx(-240)
    if turtle.xcor()>=240:
        turtle.setheading(-180-turtle.heading())
        turtle.setx(240)
    if abs(turtle.ycor())>=240:
        turtle.setheading(0-turtle.heading())
        turtle.sety(240*turtle.ycor()/abs(turtle.ycor()))
    pastpos=(turtle.xcor(),turtle.ycor())
    window.ontimer(move,10)
leftq=False
rightq=False
window = Screen()
window.bgcolor("black")
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
turtle=Turtle()
turtle.begin_fill()
window.listen()
window.onkeypress(turn_left, "Left")
window.onkey(unturn_left,"Left")
window.onkeypress(turn_right, "Right")
window.onkey(unturn_right,"Right")
turtle.speed(0)

move()

window.mainloop()