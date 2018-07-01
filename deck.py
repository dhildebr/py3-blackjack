import random

from card import Card

class Deck():
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
    
    self._cards = [Card(rank, suit) for rank in Card.CARD_RANKS for suit in Card.CARD_SUITS]
    self._num_cards_drawn = 0
    random.shuffle(self._cards)
  
  def is_empty(self):
    """ Returns whether this deck is exhausted of cards. """
    return self._num_cards_drawn < len(self._cards)
  
  def shuffle(self):
    """ Shuffles this deck, effectively reconstructing it. """
    random.shuffle(self._cards)
    self._num_cards_drawn = 0
  
  def draw_card(self):
    """
    Returns the next card this deck has to offer, or None if it
    is empty.
    """
    
    if not self.is_empty():
      drawn = self._cards[self._num_cards_drawn]
      self._num_cards_drawn += 1
      return drawn
    else:
      return None
