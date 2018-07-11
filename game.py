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
    self._player_hand = Hand(self._src_deck)
    self._player_money = starting_money
  
  def build_player_hand(self):
    """
    Builds the player's hand until they either bust or stand. Returns
    True if the player busts in the process, of False if not.
    """
    
    self._player_hand.get_new_hand(self._src_deck)
    while True:
      print(f"Your hand has a soft value of {self._player_hand.soft_value()}")
      print(f"Your hand has a hard value of {self._player_hand.hard_value()}")
      print(f"You have {self._player_hand.num_aces()} aces, and your hand's "
          "optimal value is {self._player_hand.optimal_value()}")
      print(self._player_hand, end = "\n\n")
      
      response_hit_stand = parse_reply_hit_stand("Do you wish to hit again, or stand?")
      if response_hit_stand == "HIT":
        self._player_hand.draw_card(self._src_deck)
        if self._player_hand.is_bust():
          print("BUST!")
          return True
      else:
        print(f"You've stood with a hand worth {self._player_hand.optimal_value()} points")
        print("The onus now falls to the dealer to better your score.")
        return False
