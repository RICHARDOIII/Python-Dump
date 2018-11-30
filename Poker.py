#  File: Poker.py

#  Description: Runs a single round of poker.
#  Supports 2 to 6 players.
#  Determines win based on hand type, then
#  cumulative score of cards in hand

#  Student's Name: Mark Simmons

#  Student's UT EID: mjs5839

#  Partner's Name: Daniel Espinoza

#  Partner's UT EID: dee467

#  Course Name: CS 313E 

#  Unique Number: 51350

#  Date Created: 9/25/18

#  Date Last Modified: 9/28/18

import random

class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('C', 'D', 'H', 'S')

  # constructor
  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12

    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  # string representation of a Card object 
  def __str__ (self):
    if (self.rank == 14):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str (self.rank)
    return rank + self.suit

  # equality tests
  def __eq__ (self, other):
    return self.rank == other.rank

  def __ne__ (self, other):
    return self.rank != other.rank

  def __lt__ (self, other):
    return self.rank < other.rank

  def __le__ (self, other):
    return self.rank <= other.rank

  def __gt__ (self, other):
    return self.rank > other.rank

  def __ge__ (self, other):
    return self.rank >= other.rank

class Deck (object):
  # constructor
  def __init__ (self, n = 1):
    self.deck = []
    for i in range (n):
      for suit in Card.SUITS:
        for rank in Card.RANKS:
          card = Card (rank, suit)
          self.deck.append (card)

  # shuffle the deck
  def shuffle (self):
    random.shuffle (self.deck)

  # deal a card
  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)

class Poker (object):
  HANDS = ('Royal Flush', 'Straight Flush', 'Four of a Kind',\
      'Full House', 'Flush', 'Straight', 'Three of a Kind',\
     'Two Pair', 'One Pair', 'High Card')

  def __init__ (self, num_players = 2, num_cards = 5):
    self.deck = Deck()
    self.deck.shuffle()
    self.all_hands = []
    self.numCards_in_Hand = num_cards

    # deal all the hands
    for i in range (num_players):
      hand = []
      for j in range(self.numCards_in_Hand):
        if((i*5)%50==0):
            self.deck=Deck()
            self.deck.shuffle()
        hand.append(self.deck.deal())

      self.all_hands.append(hand)
       
  # simulates the play of the game
  def play (self):
    # sort the hands of each player and print
    for i in range (len(self.all_hands)):
      sorted_hand = sorted (self.all_hands[i], reverse = True)
      self.all_hands[i] = sorted_hand
      hand_str = ''
      for card in sorted_hand:
        hand_str = hand_str + str(card) + ' '
      print ('Player {a}: {b}'.format(a = i+1, b = hand_str))
  
    # determine the type of each hand and print
    points_hand = []   # create a list to store points for each hand
    for i in range (len(self.all_hands)):
        score = self.get_hand_score(self.all_hands[i])
        hand_type = self.HANDS[score[0]]
        points_hand.append(score[0])
        print('Player {a}: {b}'.format(a = i+1, b = hand_type))
    # determine winner and print
    win = 10
    pot_winners=[]
    win_idx = 0
    for i in range(len(points_hand)):
        if points_hand[i] < win: # indicates higher scoring hand type
            win=points_hand[i]
            pot_winners=[]
            pot_winners.append(i)
        elif (points_hand[i] == win):
            pot_winners.append(i)
    if (len(pot_winners)>1): # indicates a tie in hand types
        orderedwin=[]
        for x in pot_winners:
            max=self.get_hand_score(self.all_hands[x])
            # check raw score of hand
            max=max[1]
            temp=[x,max]
            orderedwin.append(temp)
        orderedwin=sorted(orderedwin,key=lambda l:l[1],reverse=True)
        for x in orderedwin:
            print('Player {a} ties.'.format(a = x[0]+1))
        return
    print('Player {a} wins.'.format(a = pot_winners[0]+1))


  # calls methods for different hand types on hand
  # checks from highest to lowest scoring hand types
  # once a match is found, returns index of string for
  # hand type in HANDS and score of hand in a list
  def get_hand_score(self, hand):
    if self.is_royal(hand) > 0:
        return [0, self.is_royal(hand)]
    elif self.is_straight_flush(hand) > 0:
        return [1, self.is_straight_flush(hand)]
    elif self.is_four_kind(hand) > 0:
        return [2, self.is_four_kind(hand)]
    elif self.is_full_house(hand) > 0:
        return [3, self.is_full_house(hand)]
    elif self.is_flush(hand) > 0:
        return [4, self.is_flush(hand)]
    elif self.is_straight(hand) > 0:
        return [5, self.is_straight(hand)]
    elif self.is_three_kind(hand) > 0:
        return [6, self.is_three_kind(hand)]
    elif self.is_two_pair(hand) > 0:
        return [7, self.is_two_pair(hand)]
    elif self.is_one_pair(hand) > 0:
        return [8, self.is_one_pair(hand)]
    else: # high card only option
        return [9, self.is_high_card(hand)]

  # determine if a hand is a royal flush
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_royal (self, hand):
    if not (self.is_same_suit(hand) and self.is_sequence(hand, 14)):
      return 0
    else:
        return self.calc_points(hand, 10)

  # determine if a hand is a straight flush
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_straight_flush (self, hand):
    if not (self.is_same_suit(hand) and self.is_sequence(hand)):
        return 0
    else:
        hand2=sorted(hand2)
        return self.calc_points(hand2, 9)

  # determine if a hand is a four of a kind
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_four_kind (self, hand):
      test = self.count_repeats(hand)
      if test[1] == 4:
          temp = []
          temp2 = []
          for x in hand:
              if x.rank == test[0]:
                  temp.append(x)
              else:
                  temp2.append(x)
          temp2 = sorted(temp2)
          temp.extend(temp2)
          return self.calc_points(temp, 2)
      else:
          return 0

  # determine if a hand is a full house
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_full_house (self, hand):
      test = self.count_repeats(hand)
      if test[0] == [3, 2]:
          temp=[]
          temp2=[]
          for x in range(len(hand)):
              if hand[x].rank == hand[1].rank:
                  temp.append(x)
              else:
                  temp2.append(x)
          if temp[0]>temp2[0]:
              temp.extend(temp2)
          else:
              temp2.extend(temp)
              temp=temp2
          return self.calc_points(temp, 7)
      else:
          return 0
    
  # determine if a hand is a flush
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_flush (self, hand):
      if self.is_same_suit(hand):
          hand2=sorted(hand)
          return self.calc_points(hand2, 6)
      else:
          return 0

  # determine if a hand is a straight
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_straight (self, hand):
      if self.is_sequence(hand):
          hand2=sorted(hand)
          return self.calc_points(hand2, 5)
      else:
          return 0

  # determine if a hand is a three of a kind
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_three_kind (self, hand):
      test = self.count_repeats(hand)
      if test[1] == 3:
          temp = []
          temp2 = []
          for x in hand:
              if x.rank == test[0]:
                  temp.append(x)
              else:
                  temp2.append(x)
          temp2 = sorted(temp2)
          temp.extend(temp2)
          return self.calc_points(temp, 4)
      else:
          return 0

  # determine if a hand is a two pair
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_two_pair (self, hand):
      test = self.count_repeats(hand)
      if len(test)>2:
        print(test[2])
      else:
          return 0
      if test[1:] == [2,2]:
              pairs=[test[0],test[1]]
              pairs=sorted(pairs)
              temp = []
              temp2 = []
              temp3= []
              for x in hand:
                  if x.rank == pairs[0]:
                      temp.append(x)
                  elif x.rank == pairs[1]:
                      temp2.append(x)
                  else:
                      temp3.append(x)
              temp2 = temp2
              temp.extend(temp2)
              temp.extend(temp3)
              return self.calc_points(temp, 3)
      else:
          return 0
    


  # determine if a hand is one pair
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_one_pair (self, hand):
    test = self.count_repeats(hand) 
    if test[1] == 2:
        temp=[]
        temp2=[]
        for x in hand:
            if x.rank==test[0]:
                temp.append(x)
            else:
                temp2.append(x)
        temp2=sorted(temp2)
        temp.extend(temp2)
        return self.calc_points(temp, 2)
    else:
        return 0

  # called if hand is high card
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_high_card (self, hand):
    hand2=sorted(hand)
    return self.calc_points(hand2, 1)

  # checks if all items in a list of 5 Card objects
  # have the same suit
  # returns bool
  def is_same_suit(self, hand):
    for i in range (len(hand) - 1):
        if (hand[i].suit != hand[i + 1].suit):
            return False
    return True

  # checks if all items in a list of 5 Card objects
  # form a decremental sequence
  # returns bool
  def is_sequence (self, hand, init = 0):
    if init == 0:
        init = hand[0]
    for i in range (len(hand)):
      if (hand[i].rank != hand[0].rank - 1):
          return False
    return True

  # checks if any card value repeats in a list of
  # 5 Card objects
  # returns list containing rank of repeating cards
  # and number of repeats
  # if multiple repeats, 2d list returned
  def count_repeats (self, hand):
      repeats = []
      temp_hand = hand.copy()
      indx=[[]]
      for card in hand:
          temp_repeats = 1
          if card in temp_hand:
            temp_hand.remove(card) 
          else:
            continue # if not found in temp_hand
            # val has already been checked
          i = len(temp_hand)-1
          while i >= 0: # iterate thru temp_hand to find matches
              if temp_hand[i] == card:
                  tempcard=card
                  temp_hand.remove(temp_hand[i])
                  temp_repeats += 1
              i-=1
          if temp_repeats > 1:
                indx[0].append(tempcard.rank)
                repeats.append(temp_repeats)
      #if len(repeats) == 1:
       #   repeats = repeats[0]
      #else:
      repeats.sort(reverse = True) # does indx need to be sorted to?
      if len(indx[0])==0:
          return [0, 0]
      elif len(indx[0])==1:
          indx[0]=indx[0][0]
      if len(repeats) == 1:
          repeats = repeats[0]
      indx.append(repeats)
      return indx

  # determines points for a hand based on vals of each card in hand
  # and multiplier for hand type, fed from calling function
  def calc_points(self, hand, mult):
    points = mult * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)
    return points




def main():
  # prompt the user to enter the number of players
  num_players = int (input ('Enter number of players: '))
  while ((num_players < 2) or (num_players > 50)):
    num_players = int (input ('Enter number of players: '))

  # create the Poker object
  game = Poker (num_players)
  hand = [1, 1, 2, 2, 4]
  # play the game - poker
  game.play()



# do not remove this line above main()
if __name__ == '__main__':
  main()
