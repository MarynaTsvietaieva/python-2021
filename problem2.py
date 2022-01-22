# -*- coding: utf-8 -*-

# Zadanie 1.2 - Fold, Check, Call, Raise...

# Meno: Maryna Tsvietaieva
# Spolupráca: Vladyslav Yerofeiev
# Použité zdroje: 
# Čas: veľmi ťažko povedať

from copy import deepcopy
import collections
from itertools import combinations

# hearts, clubs, spades, diamonds
SUITS = ['H', 'C', 'S', 'D']
VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
DECK = [(s, v) for s in SUITS for v in VALUES]


def generate_setup():
    # helper function for generating test cases
    from random import sample
    deck = deepcopy(DECK)
    player1_hand = sample(deck, 2)
    for card in player1_hand:
        deck.remove(card)
    player2_hand = sample(deck, 2)
    for card in player2_hand:
        deck.remove(card)
    flop = sample(deck, 3)
    for card in flop:
        deck.remove(card)
    turn = sample(deck, 1)
    for card in turn:
        deck.remove(card)

    return player1_hand, player2_hand, flop, turn


def is_royal_flush(hand):
    red_cards = tuple(sorted([hand[i][1] for i in range(len(hand)) if ((hand[i][0] == 'H') and (hand[i][1] >= 10))]))
    re1_cards = tuple(sorted([hand[i][1] for i in range(len(hand)) if ((hand[i][0] == 'C') and (hand[i][1] >= 10))]))
    black_cards = tuple(sorted([hand[i][1] for i in range(len(hand)) if ((hand[i][0] == 'D') and (hand[i][1] >= 10))]))
    blac1_cards = tuple(sorted([hand[i][1] for i in range(len(hand)) if ((hand[i][0] == 'S') and (hand[i][1] >= 10))]))
    if len(red_cards) == 5:
        return True, tuple([14])
    elif len(re1_cards) == 5:
        return True, tuple([14])
    elif len(black_cards) == 5:
        return True, tuple([14])
    elif len(blac1_cards) == 5:
        return True, tuple([14])
    else:
        return False, None



def is_straight_flush(hand):
    red_cards_hearts = tuple(sorted([hand[i][1] for i in range(len(hand)) if hand[i][0] == 'H']))
    red_cards_clubs = tuple(sorted([hand[i][1] for i in range(len(hand)) if hand[i][0] == 'C']))
    black_cards_spades = tuple(sorted([hand[i][1] for i in range(len(hand)) if hand[i][0] == 'S']))
    black_cards_diamonds = tuple(sorted([hand[i][1] for i in range(len(hand)) if hand[i][0] == 'D']))
    if len(red_cards_hearts) == 5:
        if all(red_cards_hearts[0] == red_cards_hearts[i]-i for i in range(5)):
            return True, tuple([int(max(red_cards_hearts))])
        else:
            return False, None
    elif len(red_cards_clubs) == 5:
        if all(red_cards_clubs[0] == red_cards_clubs[i]-i for i in range(5)):
            return True, tuple([int(max(red_cards_clubs))])
        else:
            return False, None
    elif len(black_cards_spades) == 5:
        if all(black_cards_spades[0] == black_cards_spades[i]-i for i in range(5)):
            return True, tuple([int(max(black_cards_spades))])
        else:
            return False, None
    elif len(black_cards_diamonds) == 5:
        if all(black_cards_diamonds[0] == black_cards_diamonds[i]-i for i in range(5)):
            return True, tuple([int(max(black_cards_diamonds))])
        else:
            return False, None
    else:
        return False, None

def is_four_of_a_kind(hand):
    cards = tuple(sorted([hand[i][1] for i in range(5)]))
    cards = collections.Counter(cards).most_common()
    if cards[0][1] == 4:
        return True, tuple([int(cards[0][0])])
    return False, None

def is_full_house(hand):
    cards = tuple(sorted([hand[i][1] for i in range(5)]))
    cards = collections.Counter(cards).most_common()
    if cards[0][1] == 3 and cards[1][1] == 2:
          return True, tuple([int(cards[0][0]),int(cards[1][0])])
    return False, None


def is_flush(hand):
    red_cards_hearts = tuple(sorted([hand[i][1] for i in range(len(hand)) if hand[i][0] == 'H']))
    red_cards_clubs = tuple(sorted([hand[i][1] for i in range(len(hand)) if hand[i][0] == 'C']))
    black_cards_spades = tuple(sorted([hand[i][1] for i in range(len(hand)) if hand[i][0] == 'S']))
    black_cards_diamonds = tuple(sorted([hand[i][1] for i in range(len(hand)) if hand[i][0] == 'D']))
    if len(red_cards_hearts) == 5:
        return True, tuple([int(max(red_cards_hearts))])
    elif len(red_cards_clubs) == 5:
        return True, tuple([int(max(red_cards_clubs))])
    elif len(black_cards_diamonds) == 5:
        return True, tuple([int(max(black_cards_diamonds))])
    elif len(black_cards_spades) == 5:
        return True, tuple([int(max(black_cards_spades))])
    else:
        return False, None



def is_straight(hand):
    cards = tuple(sorted([hand[i][1] for i in range(len(hand))]))

    if all(cards[0] == cards[i]-i for i in range(5)):
        return True, tuple([int(max(cards))])
    else:
        return False, None


def is_three_of_a_kind(hand):
    cards = tuple(sorted([hand[i][1] for i in range(5)]))
    cards = collections.Counter(cards).most_common()
    if cards[0][1] == 3:
        return True, tuple([int(cards[0][0])])
    return False, None



def is_two_pairs(hand):
    cards = tuple(sorted([hand[i][1] for i in range(5)]))
    cards = collections.Counter(cards).most_common()
    if cards[0][1] == 2 and cards[1][1] == 2:
        if cards[0][0]> cards[1][0] :
           return True, tuple([int(cards[0][0]), int(cards[1][0])])
        else:
           return True, tuple([int(cards[1][0]), int(cards[0][0])])
    return False, None


def is_pair(hand):
    cards = tuple(sorted([hand[i][1] for i in range(5)]))
    cards = collections.Counter(cards).most_common()
    if cards[0][1] == 4:
        return False, None
    elif cards[0][1] == 3 and cards[1][1] == 2:
        return True, tuple([int(cards[1][0])])
    elif cards[0][1] == 2 and cards[1][1] != 2:
        return True, tuple([int(cards[0][0])])
    return False, None


def evaluate_hand(hand):
    res = is_royal_flush(hand)
    if res[0]:
        return 9, res[1]

    res = is_straight_flush(hand)
    if res[0]:
        return 8, res[1]

    res = is_four_of_a_kind(hand)
    if res[0]:
        return 7, res[1]

    res = is_full_house(hand)
    if res[0]:
        return 6, res[1]

    res = is_flush(hand)
    if res[0]:
        return 5, res[1]

    res = is_straight(hand)
    if res[0]:
        return 4, res[1]

    res = is_three_of_a_kind(hand)
    if res[0]:
        return 3, res[1]

    res = is_two_pairs(hand)
    if res[0]:
        return 2, res[1]

    res = is_pair(hand)
    if res[0]:
        return 1, res[1]

    return 0, None


def compare_highest_card(hand_1, hand_2):
    tuple_hand_1 = evaluate_hand(hand_1)
    tuple_hand_2 = evaluate_hand(hand_2)
    if tuple_hand_1[0] != 0:
      for i in range(0,len(tuple_hand_1)):
        if tuple_hand_1[i] > tuple_hand_2[i]:
           return hand_1
        elif tuple_hand_1[i] <tuple_hand_2[i]:
           return hand_2
    list1 = []
    list2 = []
    for i in range (0,5):
             list1.append(hand_1[i][1])
             list2.append(hand_2[i][1])
    list1 = sorted(list1)[::-1]
    list2 = sorted(list2)[::-1]
    i = 0
    while list1[i] == list2[i] and i != 4:
        i = i+1
    if list2[i] > list1[i]:
          return hand_2
    elif list1[i] > list2[i]:
         return hand_1
    else:
         None
          

def get_all_combinations(hand, flop, turn, river):
    my_cards = hand + flop + turn + river
    my_cards = list(combinations(my_cards, 5))
    return my_cards


def find_better(hand_1, hand_2):
    tuple_hand_1 = evaluate_hand(hand_1)
    tuple_hand_2 = evaluate_hand(hand_2)
    if tuple_hand_1[0] < tuple_hand_2[0]:
        return hand_2
    elif tuple_hand_1[0] > tuple_hand_2[0]:
        return hand_1
    elif tuple_hand_2[0] == tuple_hand_1[0] and tuple_hand_1[0] != 0 and tuple_hand_2[1] != tuple_hand_1[1]:
       return compare_highest_card(hand_1, hand_2)
    else:
          list1 = []
          list2 = []
          for i in range (0,5):
             list1.append(hand_1[i][1])
             list2.append(hand_2[i][1])
          list1 = sorted(list1)[::-1]
          list2 = sorted(list2)[::-1]
          i = 0
          while list1[i] == list2[i] and i != 4:
              i = i+1
          if list2[i] > list1[i]:
              return hand_2
          elif list1[i] > list2[i]:
              return hand_1
          else:
              None
              

def select_best(hand, flop, turn, river):
    my_cards = get_all_combinations(hand, flop, turn, river)
    better = my_cards[0]
    for ind in range(1, len(my_cards)):
      best = find_better(better, my_cards[ind])
      if best == None:
          cards = my_cards[ind]
          list1 = []
          list2 = []
          for i in range (0,5):
             list1.append(better[i][1])
             list2.append(cards[i][1])
          list1 = sorted(list1)[::-1]
          list2 = sorted(list2)[::-1]
          i = 0
          while list1[i] == list2[i] and i != 4:
              i = i+1
          if list2[i] > list1[i]:
              best = my_cards[ind]
          else:
              best = better
      better = best
    return list(best)

def calculate_chances(player1_hand, player2_hand, flop, turn):
    all = player1_hand+player2_hand+ flop+ turn
    list = [] 
    d = 0
    for i in SUITS:
        for j in VALUES:
            for k in all:
              if((i,j) != k):
                 d = d+1
            if d == 8:
                list.append((i,j))
            d = 0
    i1 = 0
    i2 = 0
    rem = 0
    for i in list:
        hand1 =select_best(player1_hand, flop, turn, [i])
        hand2 =select_best(player2_hand, flop, turn, [i])
        hand = find_better(hand1,hand2)
        if hand == hand1:
         i1 = i1+1
        elif hand == hand2:
         i2 = i2+1
        elif hand == None:
         
         rem = rem +1
    i1 = i1/44
    i2 = i2/44
    rem = rem/44
    return i1,i2,rem


if __name__ == '__main__':
    player1_hand, player2_hand, flop, turn = generate_setup()

    print("PLAYER 1:", player1_hand)
    print("PLAYER 2:", player2_hand)
    print("FLOP:", flop)
    print("TURN:", turn)

    p1_win, p2_win, draw = calculate_chances(
        player1_hand, player2_hand, flop, turn)

    print("PLAYER 1 has a {} chance of winning".format(p1_win))
    print("PLAYER 2 has a {} chance of winning".format(p2_win))
    print('There\'s a {} chance of a draw'.format(draw))
