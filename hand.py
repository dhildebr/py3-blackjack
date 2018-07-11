"""
Contains a representation of a player's hand. Hands start out with a
size equal to the value of the HAND_START_SIZE constant, which is set to
two. The HAND_LIMIT constant, set to 21, denotes the value limit of
players' hands before they bust.
"""

from card import RANK_VALUES
from deck import Deck

HAND_START_SIZE = 2
HAND_LIMIT = 21

class Hand(object):
  """
  A blackjack player's hand, which contains two or more cards. The hand
  can have more cards added to it, or be re-drawn anew. Re-generating
  the hand does not itself shuffle the deck from which it sources
  its cards.
  """
  
  def __init__(self, deck):
    """ Initializes this hand with two cards from the given deck. """
    
    self._cards = []
    for _ in range(HAND_START_SIZE):
      self._cards.append(deck.draw_card())
  
  def get_new_hand(self, deck):
    """ Starts this hand over again with two new cards. """
    
    self._cards.clear()
    for _ in range(HAND_START_SIZE):
      self._cards.append(deck.draw_card())
  
  def draw_card(self, deck):
    """ Draws an additional crd into this hand from the given deck. """
    
    self._cards.append(deck.draw_card())
  
  def __len__(self):
    """ Returns the number of cards in this hand. """
    return len(self._cards)
  
  def __str__(self):
    """
    Returns a string representation of this hand. That string will be a
    list of this hand's contents: one to a line if there are three or
    fewer cards, or in two to four columns if there are more. Additional
    columns are added in order to avoid orphan list items, for up to
    eight items (if there are 9+4n cards, the last will be on its
    own line).
    """
    
    # Print the cards on to a line if there are fewer than four
    if len(self._cards) < 4:
      return "\n".join([str(crd) for crd in self._cards])
    
    formatted_cards = []
    num_columns = 1
    
    if len(self._cards) < 5:
      num_columns = 2
    elif len(self._cards) < 7:
      num_columns = 3
    else:
      num_columns = 4
    
    for offset in range(0, len(self._cards), num_columns):
      max_subindex = min(len(self._cards) - offset, offset + num_columns)
      for index in range(max_subindex):
        if index < (max_subindex - 1):
          formatted_cards.append(str(self._cards[index + offset]).ljust(18))
          formatted_cards.append(" ")
        else:
          formatted_cards.append(str(self._cards[index + offset]))
          if (index + offset) < (len(self._cards) - 1):
            formatted_cards.append("\n")
    return "".join(formatted_cards)
  
  def num_aces(self):
    """ Returns the number of aces in this hand. """
    num_aces = 0
    for crd in self._cards:
      if crd.is_ace():
        num_aces += 1
    return num_aces
  
  def soft_value(self):
    """
    Returns the soft value of this hand. This is the value calculated
    when treating aces as having a value of one.
    """
    
    total = 0
    for crd in self._cards:
      for rnk, sft, _ in RANK_VALUES:
        if crd.rank_ == rnk:
          total += sft
    return total
  
  def hard_value(self):
    """
    Returns the hard value of this hand. This is the value calculated
    when treating aces as having a value of eleven.
    """
    
    total = 0
    for crd in self._cards:
      for rnk, _, hrd in RANK_VALUES:
        if crd.rank_ == rnk:
          total += hrd
    return total
  
  def optimal_value(self):
    """
    Returns the optimal value for this hand. If the hard value of this
    hand is alreadty under the limit, the optimal value is identical.
    Otherwise, aces are converted to their soft value until either the
    total falls under the limit or all aces are expended.
    """
    
    hard = self.hard_value()
    if hard <= HAND_LIMIT:
      return hard
    
    optimized_score = hard
    convertible_aces = self.num_aces()
    while convertible_aces > 0 and optimized_score > HAND_LIMIT:
      optimized_score -= 10
      convertible_aces -= 1
    return optimized_score
  
  def is_blackjack(self):
    """ Returns whether this hand has a blackjack/natural. """
    return len(self._cards) == HAND_START_SIZE and self.optimal_value() == HAND_LIMIT
  
  def is_bust(self):
    """ Returns whether this hand has a value above the hand limit. """
    return self.optimal_value() > HAND_LIMIT


if __name__ == "__main__":
  example_deck = Deck()
  example_hand = Hand(example_deck)
  print()
  
  while len(example_hand) <= 8:
    print(f"The hand has {len(example_hand)} cards.")
    print(example_hand, end = "\n\n")
    example_hand.draw_card(example_deck)
  
