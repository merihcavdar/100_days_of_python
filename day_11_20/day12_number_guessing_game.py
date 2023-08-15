logo = """
                                              .__            __   
   ____  __ __   ____   ______ ______ __  _  _|  |__ _____ _/  |_ 
  / ___\|  |  \_/ __ \ /  ___//  ___/ \ \/ \/ /  |  \\__  \\   __\
 / /_/  >  |  /\  ___/ \___ \ \___ \   \     /|   Y  \/ __ \|  |  
 \___  /|____/  \___  >____  >____  >   \/\_/ |___|  (____  /__|  
/_____/             \/     \/     \/               \/     \/      

"""
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0
def check_answer(guess, answer, turns):
    """returns remaining turns"""
    if guess > answer:
        print("too high")
        return turns -1
    elif guess < answer:
        print("too low")
        return turns -1
    else:
        print("you did it !")

def set_difficulty():
    level = input("choose a difficulty, type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
def game():
    print(logo)
    print("welcome to the number guessing game")
    print("im thinking of a number between 1 and 100")
    turns = set_difficulty()

    answer = randint(1, 100)
    print(f"psst, {answer}")

    guess = 0
    while guess != answer:
        guess = int(input("make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print(f"you lose")
            return
        elif guess != answer:
            print("gues again.")

        print(f"you have {turns} attempts remaining to guess the number.")

game()