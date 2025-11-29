import random

def deal_card():
    '''Returns a random card from the deck'''
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(hand):
    '''Take a list of cards and return the score calculated from the cards'''
    if sum(hand) == 21 and len(hand) == 2:
        return 21
    
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)

    return sum(hand)

def compare(p_total, d_total):
    if p_total == d_total:
        return "It's a draw."
    elif d_total == 21:
        return "Lose, opponent has a Blackjack." 
    elif p_total == 21:
        return "You win with a Blackjack."
    elif p_total > 21:
        return "You lose, you went over."
    elif d_total > 21:
        return "Opponent went over, you win."
    elif p_total > d_total:
        return "You win."
    else:
        return "You lose."
    
def play_game():
    player_cards = []
    dealer_cards = []
#define variables player and dealaer total in empty variable space incase while looops are skipped, the variable will be defined
#this will help with debuggin later, because -1 is an easy number identify as being wrong
    player_total = -1
    dealer_total = -1
    is_game_over = False

    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while is_game_over == False:
        player_total = calculate_score(player_cards)
        dealer_total = calculate_score(dealer_cards)
        print(f"Your cards: {player_cards}, current score: {player_total}")
        print(f"Computer's first card: {dealer_cards[0]}")

        if player_total == 21 or dealer_total == 21 or player_total > 21:
            is_game_over = True
        else:
            hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if hit == "y":
                player_cards.append(deal_card())
            else:
                is_game_over = True

    while dealer_total != 21 and dealer_total < 17:
        dealer_cards.append(deal_card())
        dealer_total = calculate_score(dealer_cards)  

    print(f"Your final hand: {player_cards}, final score: {player_total}")
    print(f"Computer's final hand: {dealer_cards}, final score: {dealer_total}")
    print(compare(player_total, dealer_total))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    print("\n" * 20)
    play_game()