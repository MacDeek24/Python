from turtle import Turtle,Screen

t_turtle = Turtle()
t_turtle.shape("turtle")
t_turtle.color("red")
for _ in range(4):
    t_turtle.forward(100)
    t_turtle.right(90)


screen = Screen()
screen.exitonclick()
