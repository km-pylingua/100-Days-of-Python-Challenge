#TODO-1: Create logo & welcome to the game
from random import randint

#TODO-3: Create way to choose between easy and hard; variable sets amount of guesses the user gets
easy_level = 10
hard_level = 5

def choose_difficulty_level():
    '''chooses the difficulty level: easy or hard'''
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty_level == "easy":
        return easy_level
    elif difficulty_level == "hard":
        return hard_level

#TODO-5: Create a function that compares guess to correct number
def compare_guesses(chosen_number, guessed_number, turns):
    '''compares two numbers and returns remaining attempts reduced by 1'''
    if chosen_number == guessed_number:
        print("You win!")
        return
    elif chosen_number > guessed_number:
        print("Too low.\nGuess again.")
        return turns - 1
    elif chosen_number < guessed_number:
        print("Too high.\nGuess again.")
        return turns - 1

logo = ''' _   _                 _                                                
| \ | |_   _ _ __ ___ | |__   ___ _ __                                  
|  \| | | | | '_ ` _ \| '_ \ / _ \ '__|                                 
| |\  | |_| | | | | | | |_) |  __/ |                                    
|_|_\_|\__,_|_| |_| |_|_.__/ \___|_|        ____                      _ 
 / ___|_   _  ___  ___ ___(_)_ __   __ _   / ___| __ _ _ __ ___   ___| |
| |  _| | | |/ _ \/ __/ __| | '_ \ / _` | | |  _ / _` | '_ ` _ \ / _ \ |
| |_| | |_| |  __/\__ \__ \ | | | | (_| | | |_| | (_| | | | | | |  __/_|
 \____|\__,_|\___||___/___/_|_| |_|\__, |  \____|\__,_|_| |_| |_|\___(_)
                                   |___/                                '''

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

def game():
    #TODO-2: Create a random # for player to guess
    number_to_guess = random.randint(1,100)
    print(number_to_guess)

    attempts_allowed = choose_difficulty_level()

    #TODO-4: Create a loop that allows player to keep guessing amount of times allowed until win or loss
    while attempts_allowed > 0:
        print(f"You have {attempts_allowed} attempts remaining to guess the number.")
        player_guess = int(input("Make a guess: "))
        attempts_allowed = compare_guesses(number_to_guess, player_guess, attempts_allowed)
        if attempts_allowed == 0:
            print("You've run out of guesses, you lose.")
            break

game()