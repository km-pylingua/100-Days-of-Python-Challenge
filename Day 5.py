import random

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols = ['0','1','2','3','4','5','6','7','8','9']
numbers = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the Python Password Generator!")
letter_nbr = int(input("How many letters would you like in your password? "))
symb_nbr = int(input("How many symbols would you like? "))
numb_nbr = int(input("How many numbers would you like? "))

password = []
for letter in range(letter_nbr):
    pass_letter = random.choices(letters)
    password += pass_letter
for symbol in range(symb_nbr):
    pass_symb = random.choices(symbols)
    password += pass_symb
for number in range(numb_nbr):
    pass_number = random.choices(numbers)
    password += pass_number

random.shuffle(password)
final_password = ''
for item in password:
    final_password += item
print(f"Your new password is: {final_password}")