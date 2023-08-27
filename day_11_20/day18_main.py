from turtle import Turtle, Screen
#import turtle as t
tim = Turtle()

# import turtle
# tim = turtle.Turtle()

# from turtle import Turtle
# tim = Turtle()
# tom = Turtle()
# terry = Turtle()


tim.shape("turtle")
#timmy_the_turtle.color("red")
#timmy_the_turtle.forward(100)
#timmy_the_turtle.right(90)

# from turtle import *

for _ in range(4):
    tim.forward(100)
    tim.left(90)
screen = Screen()
screen.exitonclick()

import heroes
print(heroes.gen())