#
from turtle import Turtle,Screen
from random import random,choice

tim = Turtle()
color = ["hot pink","olive","indian red","deep sky blue", "navy","lime"]

def draw_shape(num_side):
    angle = 360/num_side
    for _ in range(num_side):
        tim.forward(100)
        tim.left ( angle )

for shape_side in range(3,11):
    tim.color(choice(color))
    draw_shape(shape_side)

screen= Screen()
screen.exitonclick()
