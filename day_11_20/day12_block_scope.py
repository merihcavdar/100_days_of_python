## there is no block scope

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]


## if statement, while, for loop etc -> doesn't create block scope. those are included in global scope
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)