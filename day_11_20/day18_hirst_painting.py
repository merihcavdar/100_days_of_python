import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()


# import colorgram
#
# colors = colorgram.extract("hirst.jpg", 30)
# rgb_colors = []
# print(colors)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r,g,b))

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

color_list = [(233, 233, 232), (230, 233, 237), (235, 230, 233), (225, 233, 227), (206, 159, 83), (55, 89, 130), (145, 92, 40), (221, 206, 109), (139, 27, 49), (133, 176, 202), (156, 47, 83), (46, 55, 103), (169, 160, 40), (129, 188, 143), (83, 20, 44), (37, 43, 68), (185, 94, 107), (187, 140, 168), (85, 120, 179), (59, 40, 32), (88, 157, 92), (79, 153, 165), (195, 80, 72), (79, 74, 44), (45, 74, 77), (58, 124, 116), (162, 201, 218), (218, 176, 187), (166, 207, 165), (221, 182, 167)]
for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()