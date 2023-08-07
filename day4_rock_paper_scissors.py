import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = ["rock", "paper", "scissors"]
choices_ascii = rock,paper,scissors
user_choice = int(input("what do you choose? type 0 for Rock, 1 for Paper, 2 for Scissors. "))
computer_choice = random.randint(0,2)
print(f"you chose {choices[user_choice]}")
print(choices_ascii[user_choice])

print(f"computer chose {choices[computer_choice]}")
print(choices_ascii[computer_choice])


if user_choice > 3 or user_choice<0:
    print("you typed invalid number, you lose")
elif user_choice == 0 and computer_choice == 2:
    print("you win")
elif computer_choice == 0 and user_choice == 2:
    print("you lose!")
elif computer_choice > user_choice:
    print("computer wins!")
elif computer_choice < user_choice:
    print("you win!")
elif computer_choice == user_choice:
    print("it s a draw")
