from turtle import Turtle, Screen

timmy = Turtle()
timmy.speed(0)

# changing properties(color)

'''timmy.shape("turtle")
timmy.pencolor("red")
timmy.color("red")
timmy.forward(100)'''

# Making different shapes(triangle to decagon)

colors = ["dark orchid", "deep pink", "forest green", "red", "pale turquoise"]

def shape(x):
    timmy.color("green")
    for i in range(x):
        timmy.forward(100)
        timmy.right(360/x) 
x = 3
for i in range(360):
    shape(x)
    x+=1



screen = Screen()
screen.exitonclick()