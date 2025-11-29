import random

rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

game_images = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors? "))
if player_choice >= 0 and player_choice <=2:
    print(game_images[player_choice])

computer_choice = random.randint(0,2)
print("Computer choice:")
print(game_images[computer_choice])

if player_choice >= 3 or player_choice < 0:
    print("You typed an invalid number. You lose!")
elif computer_choice == 2 and player_choice == 0:
    print("You win!")
elif computer_choice == 0 and player_choice ==2:
    print("Computer wins!")
elif player_choice > computer_choice:
    print("You win!")
elif computer_choice > player_choice:
    print("Computer wins!")
elif computer_choice == player_choice:
    print("Tie!")