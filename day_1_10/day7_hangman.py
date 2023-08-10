from replit import clear
import random
import day7_word_list as wList
import day7_art as art

chosen_word = random.choice(wList.word_list)
print(f"psst, chosen word is {chosen_word}")
print(art.logo)
end_of_game = False
lives = 6
display = []
wrong_guesses = []

for _ in chosen_word:
    display += "_"
print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
        print("you already chose this letter correctly.")
        continue
    if guess in wrong_guesses:
        print("you already chose this letter incorrectly.")
        continue
    if guess not in chosen_word:
        lives -= 1
        print(art.stages[lives])
        print(lives)

        if lives == 0:
            end_of_game = True
            print("you lost")
            print(chosen_word)
        wrong_guesses += guess
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess
    print(display)
    if "_" not in display:
        end_of_game = True
        print("you win")
