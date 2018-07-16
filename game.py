"""
Contains a class representing a game of blackjack, as well as related
helper functions.
"""

import re

from deck import Deck
from hand import Hand

REPLY_PATTERN_YES = r"(?i)^\s*(Y(?:ES|EA)?)\s*$"
REPLY_PATTERN_NO =  r"(?i)^\s*(N(?:O|AY)?)\s*$"

REPLY_PATTERN_HIT =   r"(?i)^\s*(HIT(?: ME(?:,? BABY,? ONE MORE TIME)?)?)\s*$"
REPLY_PATTERN_STAND = r"(?i)^\s*((?:(?:I )?STAND)|WOULD THE REAL \w+(?: \w+)* PLEASE STAND UP\??)\s*$"
REPLY_PATTERN_MONEY = r"(?i)^\s*(\$?(\d+(?:\.\d\d)?))\s*$"

DEALER_STAND_THRESHOLD = 17


def parse_reply_yn(prompt):
  """
  Requests a yes/no input with the given prompt, and keeps asking until
  a valid response is received. Input is compared against the
  REPLY_PATTERN_YES and REPLY_PATTERN_NO regex patterns. Returns True if
  the accepted answer is yes, False if no.
  """
  
  reply_line = input(prompt)
  while True:
    if re.match(REPLY_PATTERN_YES, reply_line):
      return True
    elif re.match(REPLY_PATTERN_NO, reply_line):
      return False
    print("Unrecognized input.", end = "\n\n")
    reply_line = input(prompt)

def parse_reply_hit_stand(prompt):
  """
  Requests that the player hit or stand with the given prompt, and
  keeps asking until a valid response is received. Input is compared
  against the REPLY_PATTERN_HIT and REPLY_PATTERN_STAND regex patterns.
  Returns the string "HIT" if the player chooses to take another card,
  or the string "STAND" if not.
  """
  
  reply_line = input(prompt)
  while True:
    if re.match(REPLY_PATTERN_HIT, reply_line):
      return "HIT"
    elif re.match(REPLY_PATTERN_STAND, reply_line):
      return "STAND"
    print("Unrecognized input.", end = "\n\n")
    reply_line = input(prompt)

def parse_reply_bet_amt(prompt):
  """
  Parses an input line containing a monetary value, and keeps asking
  until a valid response is received. Input is compared against the
  REPLY_PATTERN_MONEY regex pattern. Returns the quantity input as a
  floating-point number.
  """
  
  reply_line = input(prompt)
  while True:
    money_pattern_search = re.search(REPLY_PATTERN_MONEY, reply_line)
    if money_pattern_search:
      return float(money_pattern_search.group(2))
    print("Unrecognized input. Money is formatted as a number with zero or two "
        "decimal places, and an optional dollar sign: [$]##...#[.##].",
        end = "\n\n")
    reply_line = input(prompt)


class Game(object):
  """
  A wrapper for an ongoing game of Blackjack.
  """
  
  def __init__(self, starting_money = 100.00):
    self._src_deck = Deck()
    self._player_hand = None
    self._dealer_hand = None
    self._player_money = starting_money
    self._have_built_hand_player = False
    self._have_built_hand_dealer = False
  
  def build_player_hand(self):
    """
    Builds the player's hand until they either bust or stand. Returns
    True if the player busts in the process, of False if not. This
    method must be called before build_dealer_hand in a given round.
    """
    
    if self._player_hand is None:
      self._player_hand = Hand(self._src_deck)
    else:
      self._player_hand.get_new_hand(self._src_deck)
    
    if self._player_hand.is_blackjack():
      print("Blackjack!")
      print("The onus now falls to the dealer to one-up you.", end = "\n\n")
      self._have_built_hand_player = True
      return False
    
    while True:
      print(f"Your hand has a soft value of {self._player_hand.soft_value()}")
      print(f"Your hand has a hard value of {self._player_hand.hard_value()}")
      print("You have {} aces, and your hand's optimal value is {}".format(
          self._player_hand.num_aces(), self._player_hand.optimal_value()))
      print(self._player_hand, end = "\n\n")
      
      response_hit_stand = parse_reply_hit_stand("Do you wish to hit again, or stand? ")
      if response_hit_stand == "HIT":
        self._player_hand.draw_card(self._src_deck)
        if self._player_hand.is_bust():
          print("BUST!")
          self._have_built_hand_player = True
          return True
      else:
        print(f"You've stood with a hand worth {self._player_hand.optimal_value()} points")
        print("The onus now falls to the dealer to better your score.", end = "\n\n")
        self._have_built_hand_player = True
        return False
  
  def build_dealer_hand(self):
    """
    Builds the dealer's hand automatically, standing on seventeen.
    Returns True if the dealer busts, or False if not. If the player's
    hand has not yet been built this round, this method has no effect
    and merely returns None. If the player previously busted, the
    dealer's hand will not be built, but this method will return False
    as though it had been.
    """
    
    if not self._have_built_hand_player:
      return None
    elif self._player_hand.is_bust():
      return False
    
    if self._dealer_hand is None:
      self._dealer_hand = Hand(self._src_deck)
    else:
      self._dealer_hand.get_new_hand(self._src_deck)
    
    if self._dealer_hand.is_blackjack():
      print("The end is nigh! The dealer has drawn a blackjack.", end = "\n\n")
      return False
    
    while self._dealer_hand.optimal_value() < DEALER_STAND_THRESHOLD:
      self._dealer_hand.draw_card(self._src_deck)
    if self._dealer_hand.is_bust():
      print("Praise the gods! The dealer has busted.", end = "\n\n")
      return True
    else:
      print("The dealer stands. Their their hand is worth {} points.".format(
          self._dealer_hand.optimal_value()), end = "\n\n")
      return False


if __name__ == "__main__":
  example_game = Game()
  example_game.build_player_hand()
  example_game.build_dealer_hand()
