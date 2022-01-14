import random


def pull_card(deck):
    pulled_card = random.choice(deck)
    deck.remove(pulled_card)
    if pulled_card == 1:
        pulled_card = draw(player_hand)
    return pulled_card


def draw(player_hand):
    if sum(player_hand) + 11 > 21:
        return 1
    else:
        return 11

def check(hand):
    if 1 in hand:
        if sum(hand) < 22:
            hand.remove(1)
            hand.append(11)
    if 11 in hand:
        if sum(hand) > 21:
            hand.remove(11)
            hand.append(1)
    return hand

deck = []
for i in range(4):
    for i in range(1,11):
        deck.append(i)
    deck.append(10)
    deck.append(10)
    deck.append(10)

player_hand = []
dealer_hand = []

#ace.value = ace.draw(player_hand)

def deal(player_hand, dealer_hand):
    pulled_card = pull_card(deck)
    player_hand.append(pulled_card)
    print(f"first card: {pulled_card}")
    pulled_card = pull_card(deck)
    player_hand.append(pulled_card)
    print(f"second card: {pulled_card}")
    print(f"total hand: {sum(player_hand)}")
    dealer_card = pull_card(deck)
    dealer_hand.append(dealer_card)
    print(f"dealer card: {dealer_card}")
    dealer_card = pull_card(deck)
    dealer_hand.append(dealer_card)

    return (player_hand, dealer_hand)

player_hand, dealer_hand = deal(player_hand,dealer_hand)

choice = "h"

while choice == "h" and sum(player_hand) < 21:

    choice = input("Stand or Hit s/h: ")

    if choice == "h":
        pulled_card = pull_card(deck)
        player_hand.append(pulled_card)
        player_hand = check(player_hand)
        print(f"added card: {pulled_card}")
        print(f"total hand: {sum(player_hand)}")

if choice == "s":
    if sum(player_hand) < sum(dealer_hand):
        game_end = "Lose"
    else:
        while sum(dealer_hand) < sum(player_hand) and sum(dealer_hand) < 21:
            add_card = pull_card(deck)
            dealer_hand.append(add_card)
            dealer_hand = check(dealer_hand)

if sum(player_hand) == sum(dealer_hand) or sum(player_hand) < sum(dealer_hand):
    game_end = "Lose"


if sum(dealer_hand) > 21:
    game_end = "Win"
else:
    game_end = "Lose"

if sum(player_hand) == 21:
    game_end = "Win"

print(f"Dealer hand: {sum(dealer_hand)}    Player hand: {sum(player_hand)}")
print(f"You {game_end}!")
