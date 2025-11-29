letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(message, shifted_amount, encode_or_decode):
    output_text = "" 
    if encode_or_decode == "decode":
        shifted_amount *= -1

    for char in message:
        if char not in letters:
            output_text += char
        else:
            shifted_position = letters.index(char) + shifted_amount
            shifted_position %= len(letters)
            output_text += letters[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

stop_game = False
while stop_game == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(message=text, shifted_amount=shift, encode_or_decode=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "yes":
        stop_game = False
        print("Goodbye")
    else:
        stop_game = True

       
   
