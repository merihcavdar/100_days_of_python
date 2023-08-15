# Modifying Global Scope

enemies = 1 # global variable

def increase_enemies():
    global enemies
    enemies = 2 # local variable
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#### another approach

friends = 1

def increase_friends():
    print(f"friends inside function: {friends}")
    return friends + 1

friends = increase_friends()
print(f"friends outside function: {friends}")


