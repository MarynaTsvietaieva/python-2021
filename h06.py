# -*- coding: utf-8 -*-
from time import sleep
from random import random, choices

def load_balance(name):
    sleep(1)
    return round(random() * 10000, 2)


def get_balances(names):
    balances = list()
    dict = {}
    for name in names:
        if dict.get(name) is None: 
            dict[name] = load_balance(name)
        balances.append((name, dict[name]))
    return balances



if __name__ == '__main__':
    names_in_db = [
        "Alex Lifeson", "John Rutsey", "Geddy Lee", "Jeff Jones",
        "Neil Peart", "Lindy Young", "Joe Perna", "Mitchel Bossi",
        "Steven Tyler", "Tom Hamilton", "Joey Kramer", "Joe Perry",
        "Brad Whitford", "Ray Tabano", "Jimmy Crespo", "Rick Dufay",
        "Ronnie James Dio", "Vivian Campbell", "Craig Goldy", "Rowan Robertson",
        "Jimmy Bain", "Rudy Sarzo", "Vinny Appice", "Simon Wright",
        "Claude Schnell", "Jens Johansson", "Scott Warren",
        "Steve Harris", "Dave Murray", "Adrian Smith", "Bruce Dickinson",
        "Nicko McBrain", "Janick Gers", "Doug Sampson", "Paul Di'Anno",
        "Dennis Stratton", "Clive Burr", "Blaze Bayley"
    ]
    # change this number to test your implementation
    test_no = 100
    test_names = choices(names_in_db, k=test_no)

    print(get_balances(test_names))
