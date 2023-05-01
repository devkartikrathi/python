from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter your color : ")

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
y_positions = [-90, -60, -30, 0, 30, 60, 90]
all_turtles = []

for i in range(7):
    turtle = Turtle("turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=-230, y=y_positions[i])
    turtle.pendown()
    all_turtles.append(turtle)

if user_bet:
    is_on = True

while is_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 220:
            is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} won.")
            else:
                print(f"You've lost! The {winning_color} won.")
        turtle.forward(random.randint(0,10))

screen.exitonclick()