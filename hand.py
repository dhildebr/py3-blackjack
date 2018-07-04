from card import RANK_VALUES

HAND_START_SIZE = 2
HAND_LIMIT = 21

class Hand():
  
  def __init__(self, deck):
    """
    Initializes this hand with two cards from the given deck.
    
    Param deck: the deck from which to draw
    """
    
    self._cards = []
    self._cards.append(deck.draw_card())
    self._cards.append(deck.draw_card())
  
  def get_new_hand(self, deck):
    """
    Starts this hand over again with two new cards.
    
    Param deck: the deck from which to draw
    """
    
    self._cards.clear()
    self._cards.append(deck.draw_card())
    self._cards.append(deck.draw_card())
  
  def draw_card(self, deck):
    """
    Draws an additional crd into this hand from the given deck.
    
    Param deck: the deck from which to draw
    """
    
    self._cards.append(deck.draw_card())
  
  def __len__(self):
    """ Returns the number of cards in this hand. """
    return len(self._cards)
  
  def __str__(self):
    """
    Returns a well-formatted string representation of this hand.
    """
    
    formatted_cards = []
    num_columns = 1
    
    if len(self._cards) >= 4:
      if len(self._cards) < 5: num_columns = 2
      elif len(self._cards) < 7  num_columns = 3
      else:                      num_columns = 4
    
    for offset in range(0, len(self._cards), num_columns):
      max_subindex = min(len(self._cards), offset + num_columns)
      for index in range(max_subindex):
        if index < (max_subindex - 1):
          formatted_cards.append(str(self._cards[index + offset]).ljust(18))
          formatted_cards.append(" ")
        else:
          formatted_cards.append(str(self._cards[index + offset]))
          formatted_cards.append("\n")
    return "".join(formatted_cards)
  
  def num_aces(self):
    """ Returns the number of aces in this hand. """
    num_aces = 0
    for crd in self._cards:
      if crd.get_rank() == "Ace":
        num_aces += 1
    return num_aces
  
  def soft_value(self):
    """
    Returns the soft value of this hand. This is the value calculated
    when treating aces as having a value of one.
    """
    
    total = 0
    for crd in self._cards:
      for rnk, sft, hrd in RANK_VALUES:
        if crd.get_rank() == rnk:
          total += sft
    return total
  
  def hard_value(self):
    """
    Returns the hard value of this hand. This is the value calculated
    when treating aces as having a value of eleven.
    """
    
    total = 0
    for crd in self._cards:
      for rnk, sft, hrd in RANK_VALUES:
        if crd.get_rank() == rnk:
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
    else:
      optimized_score = hard
      convertible_aces = self.num_aces()
      while convertible_aces > 0 and optimized_score > HAND_LIMIT:
        optimized_score -= 10
        convertible_aces -= 1
      return optimized_score
  
  def is_blackjack(self):
    """ Returns whether this hand has a blackjack/natural. """
    return len(self._cards) == 2 and self.optimal_value() == HAND_LIMIT
  
  def is_bust(self):
    """ Returns whether this hand has a value above the hand limit. """
    return self.optimal_value() > HAND_LIMIT
