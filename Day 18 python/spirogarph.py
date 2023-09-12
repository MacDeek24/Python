from turtle import Turtle,Screen
from random import random,choice
tim = Turtle()
color = ["hot pink","olive","indian red","deep sky blue", "navy","lime"]
tim.speed(11)

def draw_spirograph(size_gap):
    for _ in range(int(360/size_gap)):
        tim.color(choice(color))
        tim.circle(100)
        tim.setheading(tim.heading() + size_gap)    


draw_spirograph(6)

screen= Screen()
screen.exitonclick()