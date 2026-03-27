class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"
    import random

class Deck:
    def __init__(self):
        self.build_deck()

    # Create a full deck of 52 cards
    def build_deck(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        self.cards = [Card(suit, value) for suit in suits for value in values]

    # Shuffle the deck
    def shuffle(self):
        # Ensure the deck always has 52 cards before shuffling
        if len(self.cards) != 52:
            self.build_deck()

        random.shuffle(self.cards)

    # Deal one card
    def deal(self):
        if len(self.cards) == 0:
            return "No more cards in the deck."

        return self.cards.pop()
    deck = Deck()

# Shuffle the deck
deck.shuffle()

# Deal some cards
print(deck.deal())
print(deck.deal())
print(deck.deal())

# Check remaining cards
print("Cards left:", len(deck.cards))