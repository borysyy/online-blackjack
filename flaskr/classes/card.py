from math import floor
from random import random

class Cards:
    suits = ['c', 'd', 's', 'h']
    
    ranks = {
            '2': 2, 
            '3': 3, 
            '4': 4, 
            '5': 5, 
            '6': 6, 
            '7': 7, 
            '8': 8, 
            '9': 9, 
            '10': 10, 
            'j': 10, 
            'q': 10, 
            'k': 10, 
            'a': [1, 11]
        }
    
    def create_deck(decks):
        
        deck = []
        
        for _ in range(decks):
            for suit in Cards.suits:
                for rank, value in Cards.ranks.items():
                    card = {
                        'card': suit + rank,
                        'suit': suit,
                        'rank': rank,
                        'value': value
                    }
                    deck.append(card)
        
        return deck
    
    
    def shuffle(deck):
        currentIndex = len(deck)
        randomIndex = 0
        
        while currentIndex != 0:
            randomIndex = floor(random() * currentIndex)
            
            currentIndex -= 1
            
            [deck[currentIndex], deck[randomIndex]] = [deck[randomIndex], deck[currentIndex]]
            
        return deck