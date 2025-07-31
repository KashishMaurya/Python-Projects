import random
import os

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, d_score):
    if u_score == d_score:
        return "Draw"
    elif u_score == 0:
        return "Lose, opponent has Blackjack!"
    elif d_score == 0:
        return "Win with a Blackjack!"
    elif u_score > 21:
        return "You went over. You lose."
    elif d_score > 21:
        return "Opponent went over. You win!"
    elif u_score > d_score:
        return "You win!"
    else:
        return "You lose."

def play_game():
    user_cards = []
    dealers_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        dealers_cards.append(deal_card())

    # Ensure scores are calculated immediately after initial deal
    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealers_cards)

    while not is_game_over:
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Dealer's first card: {dealers_cards[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)  # update after drawing
            else:
                is_game_over = True

    # Dealer's turn if no Blackjack
    while dealer_score != 0 and dealer_score < 17:
        dealers_cards.append(deal_card())
        dealer_score = calculate_score(dealers_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Dealer's final hand: {dealers_cards}, final score: {dealer_score}")
    print(compare(user_score, dealer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    os.system('cls' if os.name == 'nt' else 'clear')
    play_game()
