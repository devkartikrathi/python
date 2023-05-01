from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def aage():
    tim.forward(10)
def peeche():
    tim.backward(10)
def daae():
    tim.right(15)
def baae():
    tim.left(15)
def saaf():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=aage)
screen.onkey(key="s", fun=peeche)
screen.onkey(key="d", fun=daae)
screen.onkey(key="a", fun=baae)
screen.onkey(key="c", fun=saaf)

screen.exitonclick()