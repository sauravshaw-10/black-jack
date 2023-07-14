
############### Our Blackjack House Rules ################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

#########################################################

import random
from replit import clear
from art import logo
from collections import Counter

play_again = True

while play_again:
  print(logo)
  
  def user_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    #selecting random cards for user and comp
    user_cards = []
    user_cards += random.sample(cards,2)
    print(f"Your hand: {user_cards}")
    return user_cards
  
  def comp_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    comp_cards = []
    comp_cards += random.sample(cards,2)
    total = sum(comp_cards)
    if total == 21:
      print(f"Computer's Card: {comp_cards}\nComputer's Score: {total}")
    else:  
      print("Computer's first card: " + str(comp_cards[0]))
    return comp_cards
  
  def initial_score():  
    """Add up the user and computers score"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    draw_card = True
    user_score = 0
    comp_score = 0
    user_cards = user_card()
    comp_cards = comp_card()
    for card in user_cards:
      user_score += card
    for card in comp_cards:
      comp_score += card   
    print(f"User's score: {user_score}")
    # print(comp_score)
    if user_score == 21:
      print("You win. It's a blackjack")
    elif comp_score == 21:
      print("You lose. Computer wins.")
    else:
      while draw_card:
        updated_deck_user = list((Counter(cards)-Counter(user_cards)).elements())
        get_another_card = input("Type 'y' if you want to get another card else type 'n' to pass: ")
        if get_another_card == 'y':
          user_cards += random.sample(updated_deck_user,1)
          print(f"User's hand: {user_cards}")
          user_score = sum(user_cards)
          if user_score >21 and (11 not in user_cards):
            print(f"User's score: {user_score}")
            print("You lose. Computer wins.")
            draw_card = False
          elif user_score >21 and (11 in user_cards):
            user_score -= 10
            print(f"User's score: {user_score}")
            if user_score == 21:
              print("You win. It's a blackjack")
              draw_card = False
            elif user_score>21:
              print("You lose. Computer wins.")
              draw_card = False
          elif user_score == 21:
              print(f"User's score: {user_score}")
              print("You win. It's a blackjack")
        elif get_another_card == 'n':
          draw_card = False
          while comp_score < 17:
            updated_deck_comp = list((Counter(cards)-Counter(comp_cards)).elements())
            comp_cards += random.sample(updated_deck_comp,1)
            comp_score = sum(comp_cards)
            print(f"Computer's hand: {comp_cards}")
          # print(f"Computer's score: {comp_score}")
          if comp_score >21 and (11 not in comp_cards):
            print(f"Computer's score: {comp_score}")
            print("You Win. Computer went over.")
          elif comp_score >21 and (11 in comp_cards):
            comp_score -= 10
            print(f"Computer's score: {comp_score}")
            if comp_score == 21:
              print("You lose. Computer wins.")
            elif comp_score>21:
              print("You win. Computer went over.")
            elif comp_score<21:
              if user_score > comp_score:
                print("You win. :)")
              elif user_score == comp_score:
                print("It's a draw.")
              else:
               print("You lose. Computer wins.") 
          elif comp_score <=21:
            print(f"Computer's score: {comp_score}")
            if user_score > comp_score:
                print("You win. :)")
            elif user_score == comp_score:
              print("It's a draw.")
            else:
             print("You lose. Computer wins.")
        
  initial_score()
  restart = input("Type 'y' if you want to restart the game, else type 'n' to exit: ")
  if restart == 'n':
    play_again = False
  else:
    clear()
  


