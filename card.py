"""
Contains a representation of a card from the standard deck of 52.
At the root level are constants CARD_RANKS, which is a tuple of strings
for all the ranks (such as aces or eights); amd CARD_SUITS, another
tuple containing strings for all possible suits (such as diaonds or
clubs.)

The final root-level constant, RANK_VALUES, is a tuple containing nested
3-tuples mapping each rank for its soft and hard values, such as
("Ace", 1, 11). The outer tuple can thus be iterated over using tuple
unpacking, such as the form:

for rnk, sft, hrd in RANK_VALUES:
  pass
"""

RANK_VALUES = (
    ("Ace", 1, 11),   ("Two", 2, 2),     ("Three", 3, 3), ("Four", 4, 4), ("Five", 5, 5),
    ("Six", 6, 6),    ("Seven", 7, 7),   ("Eight", 8, 8), ("Nine", 9, 9), ("Ten", 10, 10),
    ("Jack", 10, 10), ("Queen", 10, 10), ("King", 10, 10)
)

CARD_RANKS = tuple([rnk for rnk, sft, hrd in RANK_VALUES])
CARD_SUITS = ("Clubs", "Diamonds", "Hearts", "Spades")

class Card(object):
  """
  A playing card from the standard 52-card deck. Cards have one of four
  suits and one of thirteen ranks.
  """
  
  def __init__(self, rank, suit):
    """
    Initializes this playing card with the given rank and suit. The
    arguments provide must be strings. If the rank given is not in
    CARD_RANKS, it will default to the first element thereof. If the
    given suit is not in CARD_SUITS, it will similarly default to the
    first element of that.
    """
    
    # Default values for rank, values
    super(Card, self).__setattr__("rank_", CARD_RANKS[0])
    super(Card, self).__setattr__("soft_value_", 0)
    super(Card, self).__setattr__("hard_value_", 0)
    
    # Search for rank and corresponding values
    caps_rank, caps_suit = rank.capitalize(), suit.capitalize()
    for rnk, sft, hrd in RANK_VALUES:
      if caps_rank == rnk:
        super(Card, self).__setattr__("rank_", rnk)
        super(Card, self).__setattr__("soft_value_", sft)
        super(Card, self).__setattr__("hard_value_", hrd)
    
    # Assign suit, defaulting to first if invalid
    super(Card, self).__setattr__("suit_", (caps_suit if (caps_suit in CARD_SUITS) else CARD_SUITS[0]))
  
  def __getattribute__(self, attr):
    """ Prevents the reading of private attributes. """
    if attr.startswith("_"):
      raise AttributeError(f"Attribute '{attr}' is inaccessible.")
    return super(Card, self).__getattribute__(attr)
  
  def __setattr__(self, key, value):
    """ Prevents the overwriting of read-only attributes. """
    if key.endswith("_"):
      raise AttributeError(f"Attribute '{key}' cannot be overwritten.")
    super(Card, self).__setattr__(key, value)
  
  def is_ace(self):
    """ Returns whether this card is an ace. """
    return self._rank == "Ace"
  
  def __str__(self):
    """
    Returns a string representation of this playing card in the format
    "{rank} of {suit}". For example, the "Ace of Clubs".
    """
    
    return f"{self.rank_} of {self.suit_}"
