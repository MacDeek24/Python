from turtle import Turtle,Screen

tm= Turtle()
screen = Screen()

def move_forwerd():
    tm.forward(10)

screen.listen()
screen.onkey(key="space",fun=move_forwerd)
screen.exitonclick()