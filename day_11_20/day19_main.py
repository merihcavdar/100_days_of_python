from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_left():
    tim.setheading(tim.heading() + 10)


def turn_right():
    tim.setheading(tim.heading() - 10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="k", fun=move_forwards)
screen.onkey(key="a", fun=move_backwards)
screen.onkey(key="e", fun=turn_left)
screen.onkey(key="m", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
