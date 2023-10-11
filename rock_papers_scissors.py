"""

Computer choice = rock/papers/scissors

User choice = input

Compare

"""

import random

options = ['rock', 'papers', 'scissors']

computer_choice = random.choice(options)

user_choice = input("Enter rock/papers/scissors : ")

if user_choice!="paper" and user_choice!="rock" and user_choice!="scissors":
    print("invalid choice, please enter right one")
elif user_choice == "paper" and computer_choice == "rock":
    print('you won!!')
elif user_choice == "rock" and computer_choice == "scissors":
    print('you won!!')
elif user_choice == "scissors" and computer_choice == "paper":
    print('you won!!')
elif user_choice == computer_choice:
    print("its a tie")
else:
    print(f"you lost, computer choice was {computer_choice}") 