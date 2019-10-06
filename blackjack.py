'''
Jenny Han

This is a modified Blackjack game that is meant to be run in Terminal
'''

import os
import random
DECK = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
PLAYER_WINS = 0
DEALER_WINS = 0

#hit gives the hand a random card from the deck
def hit(hand):
  random.shuffle(DECK)
  card = DECK.pop()
  if card == 11:
    card = "J"
  if card == 12:
    card = "Q"
  if card == 13:
    card = "K"
  if card == 14:
    card = "A"
  hand.append(card)
  return hand

#total assigns the hand the correct value, picking A as 11 or 1 depending on 
#the rest of the cards
def total(hand):
  total = 0
  for card in hand:
    if card == "J":
      total += 10
    elif card == "K":
      total += 10
    elif card == "Q":
      total += 10
    
    elif card == "A":
      #check if adding 11 does not put hand over 21 
      if total + 11 > 21:
        total += 1
      else:
        total += 11
    else:
      total += card

  return total

#main runs the game simulation in the terminal
if __name__ == "__main__":
  print ("********************************************\n"+
    "** Welcome to Jenny's Modified Blackjack! **\n"+
    "********************************************\n"+"Try to get as close to 21 as possible without going over. "+
    "You are playing against the Dealer. \nPress q to quit the game at any time.")
  #initialize the first hands of the dealer and the player
  player_hand = []
  dealer_hand = []
  dealer_hand = hit(dealer_hand)
  player_hand = hit(player_hand)

  #constnatly run until player hits "q"
  while True:
    #if over 21 the player automatically loses
    if total(player_hand) > 21:
      print ("YOU LOST! Your hand is over 21. Hand: " + str(player_hand) + ", Total: " + str(total(player_hand)))
      DEALER_WINS += 1
      print("\n")
      print("Player: ",PLAYER_WINS, " Dealer: ",DEALER_WINS)
      print("\nStarting new hand....")
      dealer_hand = []
      player_hand = []
      DECK = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
      dealer_hand = hit(dealer_hand)
      player_hand = hit(player_hand)

    #if hand is exactly 21 then player wins
    if total(player_hand) == 21:
      print ("PLAYER BLACKJACK! Your hand is exactly 21. Hand: " + str(player_hand))
      PLAYER_WINS += 1
      print("\n")
      print("Player: ",PLAYER_WINS, " Dealer: ",DEALER_WINS)
      print("\nStarting new hand....")
      dealer_hand = []
      player_hand = []
      DECK = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
      dealer_hand = hit(dealer_hand)
      player_hand = hit(player_hand)

    #if dealer gets a blackjack then player loses
    if total(dealer_hand) == 21:
      print ("DEALER BLACKJACK! Dealer's hand is exactly 21. Hand: " + str(dealer_hand))
      DEALER_WINS += 1
      print("\n")
      print("Player: ",PLAYER_WINS, " Dealer: ",DEALER_WINS)
      print("\nStarting new hand....")
      dealer_hand = []
      player_hand = []
      DECK = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
      dealer_hand = hit(dealer_hand)
      player_hand = hit(player_hand)


    print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
    operation = input("\nPress 'h' to hit. Press 'w' to wait. Press 'b' to bet on your hand: ").lower()
    
    #add a card to player hand and dealer if needed
    if operation == "h":
      print("You chose to HIT!")
      player_hand = hit(player_hand)
      if total(dealer_hand)<17:
        dealer_hand = hit(dealer_hand)

    #don't do anything to player hand but add to dealer if needed
    elif operation == "w":
      print("You chose to WAIT!")
      if total(dealer_hand)<17:
        dealer_hand = hit(dealer_hand)

    #see who is closest to 21 without going over 21
    elif operation == "b":
      print("You chose to BET!")
      print("The Dealers hand was "+ str(dealer_hand) + " for a total of "+ str(total(dealer_hand)))
      d = abs(total(dealer_hand) - 21)
      p = abs(total(player_hand) - 21)

      if p < d and total(player_hand) <=21:
        print("YOU WIN!")
        PLAYER_WINS += 1
      elif d == p:
        print("TIE!")
      else:
        print("DEALER WINS!")
        DEALER_WINS += 1

      #reset cards
      print("\n")
      print("Player: ",PLAYER_WINS, " Dealer: ",DEALER_WINS)
      print("Starting new hand....")
      dealer_hand = []
      player_hand = []
      DECK = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
      dealer_hand = hit(dealer_hand)
      dealer_hand = hit(player_hand)

    #player quit the game
    elif operation == "q":
      print ("\nThanks for playing!")
      exit()

