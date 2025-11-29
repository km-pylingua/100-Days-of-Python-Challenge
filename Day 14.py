import game_data
import random

#create function that decides whether A or B is the correct answer
def correct_answer(A_followers, B_followers):
    """compares A followers to B followers and returns which has higher followers"""
    if A_followers > B_followers:
        return "A"
    else:
        return "B"

#create function that compares guess with correct answer
def compare_guess(guess, answer):
    """returns True if guess is same as answer and false if it is not"""
    if guess == answer:
        return True
    else:
        return False
    
def format_data(choice):
    choice_name = choice['name']
    choice_description = choice['description']
    choice_country = choice['country']
    return f"{choice_name}, a {choice_description}, from {choice_country}"

#create logos
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

def game():
     #create variables for A & B
    choice_B = game_data.data[random.randint(0,50)]

    #create a variable score set to 0 to keep track of the user's score
    score = 0
    game_over = False

    #make a guess variable for the user to submit their guess
    #create a function that turns the variable B into A if the user is correct  
    #add 1 to the score if the user is correct
    #trigger end of game and return the final score if the user is wrong
    while game_over == False:
        choice_A = choice_B
        choice_B = game_data.data[random.randint(0,50)]

        if choice_B == choice_A:
            choice_B = game_data.data[random.randint(0,50)]
        
        print(f"Compare A: {format_data(choice_A)}.")
        print(vs)
        print(f"Against B: {format_data(choice_B)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        choice_A_followers = choice_A["follower_count"]
        choice_B_followers = choice_B["follower_count"]
        
        answer = correct_answer(choice_A_followers, choice_B_followers)
        correct = compare_guess(guess, answer)

        if correct == True:
            score += 1
            print(" \n" * 50)
            print(logo)

            print(f"You're right! Current score: {score}.")

        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            game_over = True

game()