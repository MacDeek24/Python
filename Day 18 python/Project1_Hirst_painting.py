# def generate_random_colors(num_colors=20):
#     colors = []
#     for _ in range(num_colors):
#         r = random.randint(0, 255)
#         g = random.randint(0, 255)
#         b = random.randint(0, 255)
#         colors.append((r, g, b))
#     return colors

# random_colors = generate_random_colors()
# print(random_colors)



import turtle as t
import random

t.colormode(255)
tim = t.Turtle()

color_list = [(147, 42, 253), (206, 218, 63), (51, 52, 7), (254, 235, 178), (31, 3, 50), (127, 53, 117), (133, 117, 119), (207, 65, 101), (251, 9, 155), (233, 73, 247), (73, 58, 102), (25, 254, 123), (204, 124, 89), (251, 239, 152), (37, 83, 64), (236, 70, 166), (231, 243, 6), (254, 185, 158), (107, 5, 70), (239, 241, 29)]


tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
num_of_dots = 100
for dot_count in range(1, num_of_dots + 1):
    tim.dot(20 , random.choice(color_list))
    tim.forward(50)


    if dot_count %10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500) 
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()