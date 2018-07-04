RANK_VALUES = (
    ("Ace", 1, 11),   ("Two", 2, 2),     ("Three", 3, 3), ("Four", 4, 4), ("Five", 5, 5),
    ("Six", 6, 6),    ("Seven", 7, 7),   ("Eight", 8, 8), ("Nine", 9, 9), ("Ten", 10, 10),
    ("Jack", 10, 10), ("Queen", 10, 10), ("King", 10, 10)
)

CARD_RANKS = tuple([rank for rank, soft, hard in RANK_VALUES])
CARD_SUITS = ("Clubs", "Diamonds", "Hearts", "Spades")

class Card():
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
    
    caps_rank, caps_suit = rank.capitalize(), suit.capitalize()
    self._rank = (caps_rank if (caps_rank in CARD_RANKS) else CARD_RANKS[0])
    self._suit = (caps_suit if (caps_suit in CARD_SUITS) else CARD_SUITS[0])
  
  def get_rank(self):
    """ Returns this card's rank as a string. """
    return self._rank
  
  def get_suit(self):
    """ Returns this card's suit as a string. """
    return self._suit
  
  def is_ace(self):
    """ Returns whether this card is an ace. """
    return self._rank == "Ace"
  
  def __str__(self):
    """
    Returns a string representation of this playing card in the format
    "{rank} of {suit}". For example, the "Ace of Clubs".
    """
    
    return f"{self._rank} of {self._suit}"
