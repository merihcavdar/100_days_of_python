while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
