def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_left():
    print('left')


def move():
    print('move')


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


for step in range(6):
    jump()
