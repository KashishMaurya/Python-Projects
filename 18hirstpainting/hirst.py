# import colorgram

# rgb_colors = []
# colors = colorgram.extract('images.jpg', 50)

# for color in colors :
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_clr = (r,g,b)
#     rgb_colors.append(new_clr)
    
# print(rgb_colors)

# got color list from above code
color_list = [(248, 247, 240), (239, 250, 245), (251, 241, 247), (237, 243, 250), (235, 226, 87), (210, 161, 109), (113, 177, 212), (201, 5, 68), (230, 52, 128), (196, 77, 19), (217, 133, 177), (193, 164, 15), (34, 106, 166), (11, 21, 
62), (32, 189, 114), (232, 224, 4), (18, 28, 171), (122, 188, 161), (204, 
32, 127), (233, 165, 197), (14, 183, 211), (10, 45, 24), (38, 132, 72), (45, 15, 10), (105, 92, 210), (139, 219, 203), (185, 13, 6), (135, 218, 232), (229, 73, 45), (169, 180, 229), (79, 7, 25), (12, 97, 49), (233, 173, 163), (253, 5, 47), (22, 36, 246), (13, 85, 101), (58, 82, 16), (255, 8, 4), (47, 249, 96)]

from turtle import Screen
import turtle as t
import random

t.colormode(255)
timmy = t.Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()

timmy.setheading(220)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots+1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)
    
    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


screen = Screen()
screen.setup(width=600, height=500)
screen.exitonclick()