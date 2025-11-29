import random

#TODO-1: update the word list to use the 'word_list' from hangman_words.py

lives = 6

#TODO-3: import the logo from hangman_art.py and print it at the start of the game

word_list = ['aardvark', 'babboon', 'camel']

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

placeholder = ""
for i in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"YOU HAVE {lives} LIVES LEFT")
    guess = (input("Guess a letter: ")).lower()

    display = ""

    if guess in correct_letters:
        print("You've already guessed: " + guess)

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters += letter
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed: {guess}. That's not in the word. You lose a life")
        if lives == 0:
            game_over = True
            print("The correct word was: " + chosen_word)
            print("YOU LOSE")

    if "_" not in display:
        game_over = True
        print("YOU WIN")

#TODO-2: update the code below to use the stages List from the file hamgman_art.py
