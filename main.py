import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

your_cards =[]
computer_cards =[]

def deal_card():
    return random.choice(cards)

your_cards.append(deal_card())
your_cards.append(deal_card())

computer_cards.append(deal_card())
computer_cards.append(deal_card())

computer_total = sum(computer_cards)

print(logo)
print(f"Your cards:[{your_cards}]")
print(f"Your total is {sum(your_cards)}")
print(f"Computer's first card is {computer_cards[0]}")

def calculate_score(your_cards):
    your_total = sum(your_cards)
    while your_total > 21 and 11 in your_cards:
        ace = your_cards.index(11)
        your_cards[ace]= 1
        your_total = sum(your_cards)
    return your_total

def stand():
    your_total = calculate_score(your_cards)
    print(f"Your cards:[{your_cards}]")
    print(f"Your total is {your_total}")
    print(f"Computer's cards:[{computer_cards}]")
    print(f"Computer total is {computer_total}")

    if your_total > 21:
        print("You lost")
        return
    elif computer_total < your_total <= 21:
        print("You win")
    elif your_total == computer_total:
        print("It's a draw")
    elif your_total < computer_total < 21:
        print("Computer wins")

def hit():
    your_cards.append(deal_card())
    your_total = calculate_score(your_cards)
    print(f"Your cards:[{your_cards}]")
    print(f"Your new total is {your_total}")
    print(f"Computer's first card is {computer_total}")

    if your_total > 21:
        print("You lost")

    proceed = input("Do you wanna hit? y/n: ")
    if proceed == "y":
        hit()
    elif proceed == "n":
        stand()

Blackjack = input("Do you wanna hit? y/n: ")
if Blackjack == "y":
    hit()
elif Blackjack == "n":
    stand()




