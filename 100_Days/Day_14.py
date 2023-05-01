from turtle import Turtle, Screen

ttl = Turtle()
my_screen = Screen()

'''
ttl.circle(50)
ttl.penup()
ttl.backward(25)
ttl.pendown()
for i in range (0,8):
    ttl.forward(45)
    ttl.left(45)
    
my_screen.exitonclick()
'''
ttl.color("red","yellow")
ttl.begin_fill()
for i in range(0,50):
    ttl.speed(0)
    ttl.forward(200)
    ttl.left(170)
ttl.end_fill()
my_screen.exitonclick()