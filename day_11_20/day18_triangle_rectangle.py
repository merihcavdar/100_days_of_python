import turtle as t

tim = t.Turtle()

def draw_shape(num_of_sides):
    for _ in range(num_of_sides):
        angle = 360 / num_of_sides
        tim.forward(100)
        tim.right(angle)

for _ in range(3, 11):
    tim.color("red")
    draw_shape(_)