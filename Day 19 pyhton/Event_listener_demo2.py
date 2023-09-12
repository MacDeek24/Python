from turtle import Turtle,Screen

tm= Turtle()
screen = Screen()

def move_forwerd():
    tm.forward(10)
def move_backwerd():
    tm.back(10)
def move_left():
    tm.left(15)
def move_right():
    tm.right(15)

def clear():
    tm.clear()
    tm.penup()
    tm.home()
    tm.pendown()

screen.listen()
screen.onkey(key="w",fun=move_forwerd)
screen.onkey(key="s",fun=move_backwerd)
screen.onkey(key="a",fun=move_left)
screen.onkey(key="d",fun=move_right)
screen.onkey(key="c",fun=clear)
screen.exitonclick()