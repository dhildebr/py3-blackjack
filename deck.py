"""
Contains a representation of a deck of the standard 52 cards. A deck's
cards are shuffled at initialization and when manually re-shuffled, and
cards afterwards are drawn in constant time.
"""

import random

from card import Card
from card import CARD_RANKS
from card import CARD_SUITS

class Deck(object):
  """
  A standard deck of 52 cards. Drawing from the desk will return
  instances of Card until the deck is exhausted, after which doing so
  will return None.
  """
  
  def __init__(self):
    """
    Initializes this deck with the usual 52 cards, formed of the
    combinations of Card.CARD_RANKS and Card.CARD_SUITS. The deck will
    be shuffled upon initialization.
    """
    
    self._cards = [Card(rank, suit) for rank in CARD_RANKS for suit in CARD_SUITS]
    self._num_drawn = 0
    random.shuffle(self._cards)
  
  def __len__(self):
    """ Returns the number of cards left in the deck """
    return len(self._cards) - self._num_drawn
  
  def is_empty(self):
    """ Returns whether this deck is exhausted of cards. """
    return len(self) <= 0
  
  def reshuffle(self):
    """ Shuffles this deck, effectively reconstructing it. """
    random.shuffle(self._cards)
    self._num_drawn = 0
  
  def draw_card(self):
    """
    Returns the next card this deck has to offer, or raises an
    IndexError if it is exhausted of cards.
    """
    
    if not self.is_empty():
      drawn = self._cards[self._num_drawn]
      self._num_drawn += 1
      return drawn
    raise IndexError("The deck has been exhausted of cards.")


# If deck.py is used as the program entry point, prints out a random
# deck in four columns, thirteen high
if __name__ == "__main__":
  example_deck = Deck()
  example_cards = []
  
  while not example_deck.is_empty():
    example_cards.append(example_deck.draw_card())
  for offset in range(0, len(example_cards), 4):
    print(
        str(example_cards[offset]).ljust(18),
        str(example_cards[offset + 1]).ljust(18),
        str(example_cards[offset + 2]).ljust(18),
        str(example_cards[offset + 3]).ljust(18)
    )
