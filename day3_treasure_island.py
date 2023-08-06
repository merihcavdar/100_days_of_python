print('''
*******************************************************************************

                                          =||=
                         o   |\ ,'`. /||\ ,'`. /|    o
 _   _   _   |\__      /\^/\ | `'`'`' || `'`'`' |  /\^/\   |\__     _   _   _
| |_| |_| | /   o\__  |  /  ) \      /  \      /  |  /  ) /   o\__ | |_| |_| |
 \       / |    ___=' | /  /   |    |    |    |   | /  / |    ___=' \       /
  |     |  |    \      Y  /    |    |    |    |    Y  /  |    \      |     |
  |     |   \    \     |  |    |    |    |    |    |  |   \    \     |     |
  |     |    >    \    |  |    |    |    |    |    |  |    >    \    |     |
 /       \  /      \  /    \  /      \  /      \  /    \  /      \  /       \
|_________||________||______||________||________||______||________||_________|
    __         __       __       __        __       __       __         __
   (  )       (  )     (  )     (  )      (  )     (  )     (  )       (  )
    ><         ><       ><       ><        ><       ><       ><         ><
   |  |       |  |     |  |     |  |      |  |     |  |     |  |       |  |
  /    \     /    \   /    \   /    \    /    \   /    \   /    \     /    \
 |______|   |______| |______| |______|  |______| |______| |______|   |______|
*******************************************************************************
''')

print("welcome to treasure island")
print("your mission is to find the treasure")
choice1 = input("you're at a cross road. where do you want to go? type \"left\" or \"right\" \n").lower()

if choice1 == "right":
    print("you fell into a hole. game over.")
    exit()
elif choice1 == "left":
    choice2 = input("you've come to a lake. there is an island in the middle of the lake. type \"wait\" to wait for a boat. type \"swim\" to swim across. \n").lower()
    if choice2 == "swim":
        print("you got attacked by an angry trout. game over")
        exit()
    elif choice2 == "wait":
        choice3 = input(
            "you came to a lake. there is an island in the middle of the lake. type \"wait\" to wait for a boat. type \"swim\" to swim across. \n").lower()
        if choice3 == "red":
            print("it s a room full of fire. game over")
            exit()
        elif choice3 == "blue":
            print("you entered a room of beasts. game over")
            exit()
        elif choice3 == "yellow":
            print("you found the treasure. you win")
        else:
            print("you chose a door that doesnt exist. game over")
