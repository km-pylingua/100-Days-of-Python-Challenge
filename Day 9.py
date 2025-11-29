gavel = r"""
 ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                   jgs/_______________\" \" \
"""
print(gavel)

print("Welcome to the secret auction program.")
auction_on = True

def find_winner(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for name in bidding_dictionary:
        bid = bidding_dictionary[name]
        if bid > highest_bid:
            highest_bid = bid
            winner = name
    print(f"The winner is {winner} with {highest_bid}.")

#dictionary {name:bid}
auction = {}

while auction_on == True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    auction[name] = bid
    auction.update({name: bid})

    cont_bidding = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if cont_bidding == 'yes':
        auction_on = True
        print("\n" * 100)
    elif cont_bidding == 'no':
        auction_on = False
        find_winner(auction)
        

