import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint (0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

# python tuples (1, 3, 8)
# python list [1, 3, 8]
