class Hand:
    def __init__(self, ownerName, isDealer = False):
        self.ownerName = ownerName
        self.isDealer = isDealer
        self.cards = []
        self.totals = [0]
        
    
    def addCard(self, card):
        self.cards.append(card)
        
    # def calculateTotal(self):
    #     card = self.cards