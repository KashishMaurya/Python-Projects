from turtle import Turtle, Screen
import turtle as t
import random

timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("green")
t.colormode(255)
timmy.speed("fastest")

def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)

# # square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# # dashed line
# for _ in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# # all shapes
# def draw_shape(num_side) :
#     angle = 360 / num_side
#     for _ in range(num_side):
#         timmy.forward(100)
#         timmy.right(angle)
        
# for shape in range(3, 9):
#     draw_shape(shape)
#     timmy.color(random_color())  

# # random walk
# timmy.pensize(10)
# direction = [0,90,180,270]

# for _ in range(100) :
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(direction))


# spirograph
for _ in range(36):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.setheading(timmy.heading() + 10)
    

screen = Screen()
screen.setup(width=600, height=500)
screen.exitonclick()