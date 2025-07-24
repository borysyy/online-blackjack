from .hand import Hand
from random import randint


class BlackJack:
    def __init__(self, shoe, players):
        self.shoe = shoe
        self.players = players
        
    def burn(self):
        self.shoe.pop(0)
        
    def add_cut_card(self):
        cutCard = {
            'card': 'cut'
        }
        
        randomCutIndex = randint(50, 85)
        
        cut = len(self.shoe) - randomCutIndex 
        self.shoe.insert(cut, cutCard)