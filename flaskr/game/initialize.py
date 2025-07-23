

from classes.card import Cards
from classes.hand import Hand

 
def initialize_game():
    cards = Cards
    decks = cards.create_deck(6)
    shoe = cards.shuffle(decks)
    
    return shoe
    