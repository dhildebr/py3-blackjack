class Card():
  """
  A playing card from the standard 52-card desk.
  """
  
  RANK_VALUES = (
      ("Ace", 1),   ("Two", 2),    ("Three", 3), ("Four", 4), ("Five", 5),
      ("Six", 6),   ("Seven", 7),  ("Eight", 8), ("Nine", 9), ("Ten", 10),
      ("Jack", 10), ("Queen", 10), ("King", 10)
  )
  
  CARD_RANKS = tuple([rank for rank, value in RANK_VALUES])
  CARD_SUITS = ("Clubs", "Diamonds", "Hearts", "Spades")
  
  def __init__(self, rank, suit):
    caps_rank, caps_suit = rank.capitalize(), suit.capitalize()
    self._rank = (caps_rank if (caps_rank in self.CARD_RANKS) else self.CARD_RANKS[0])
    self._suit = (caps_suit if (caps_suit in self.CARD_SUITS) else self.CARD_SUITS[0])
    for rnk, val in self.RANK_VALUES:
      if rnk == self.rank:
        self._value = val
  
  def get_rank(self):
    return self._rank
  
  def get_suit(self):
    return self._suit
  
  def get_value(self):
    return self._value
  
  def __str__(self):
    return f"{self._rank} of {self._suit}"
