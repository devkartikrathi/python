from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

start_posi = [0,-20,-40]

segements = []

for i in start_posi:
    turtle=Turtle("square")
    turtle.color("white")
    turtle.penup()
    turtle.goto(x=i, y=0)
    segements.append(turtle)

screen.update()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg in segements:
        seg.forward(20)

screen.exitonclick()