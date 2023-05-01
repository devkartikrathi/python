from turtle import Turtle, Screen
import random
import turtle


tim = Turtle()
screen = Screen()
tim.speed(0)
tim.pensize()
screen.bgcolor("Black")
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

'''direction = [0, 90, 180, 270]
distance = 30

while True:
    tim.forward(distance)
    tim.color(random_color())
    tim.setheading(random.choice(direction))'''

# drawing a spirograph

'''x = 11
for i in range(x):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(tim.heading()+(360/x))'''



screen.exitonclick()