###Rock, Paper, Scissors 
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
game_image = [rock, paper, scissors]

user_choice = int(input("Rock for 0. Paper for 1. Scissors for 2."))
computer_choice = random.randint(0,2)

if user_choice < 0 or user_choice > 2:
    print("Break Rules.\nGet out!")
elif user_choice == 0 and computer_choice == 1:
    print(f"{game_image[user_choice]}\n{game_image[computer_choice]}\nYou win!")
elif user_choice == 1 and computer_choice == 0:
    print(f"{game_image[user_choice]}\n{game_image[computer_choice]}\nYou win!")
elif user_choice == 2 and computer_choice == 1:
    print(f"{game_image[user_choice]}\n{game_image[computer_choice]}\nYou win!")
elif user_choice == computer_choice:
    print(f"{game_image[user_choice]}\n{game_image[computer_choice]}\nYou win!")
else:
    print("You lose.")