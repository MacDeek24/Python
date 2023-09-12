from turtle import Turtle
from random import random,choice

tim = Turtle()

color = ["hot pink","olive","indian red","deep sky blue", "navy","lime"]
direction =[0,90,180,270]
tim.pensize(15)

for _ in range(100):
    tim.color(choice(color))
    tim.forward(30)
    tim.setheading(choice(direction))