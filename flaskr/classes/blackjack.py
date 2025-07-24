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
        
    def initialize_hands(self):
        
        for username, playerData in self.players.items():
            playerData['hand'] = Hand()
        
        dealerHand = Hand(isDealer = True)
        
        self.players['dealer']['hand'] = dealerHand
        
        for _ in range(2):
            for username, playerData in self.players.items():
                card = self.get_card()
                playerData['hand'].addCard(card)
        
     
                   
                
    
    def get_card(self):
        card = self.shoe.pop(0)
        
        return card
    
        
            