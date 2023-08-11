import math

test_h = int(input("height of wall: "))
test_w = int(input("width of wall: "))
coverage = 5


def paint_calc(height, width, cover):
    print(f"needed number of cans: {math.ceil(height * width / 5)}")


paint_calc(height=test_h, width=test_w, cover=coverage)
