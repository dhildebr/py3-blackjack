"""

"""

import re

from deck import Deck

REPLY_PATTERN_YES = r"(?i)^\s*(Y(?:ES|EA)?)\s*$"
REPLY_PATTERN_NO =  r"(?i)^\s*(N(?:O|AY)?)\s*$"

REPLY_PATTERN_HIT =   r"(?i)^\s*(HIT(?: ME(?:,? BABY,? ONE MORE TIME)?)?)\s*$"
REPLY_PATTERN_STAND = r"(?i)^\s*((?:(?:I )?STAND)|WOULD THE REAL \w+(?: \w+)* PLEASE STAND UP\??)\s*$"
REPLY_PATTERN_MONEY = r"(?i)^\s*(\$?(\d+(?:\.\d\d)?))\s*$"


def parse_reply_yn(self, prompt):
  """
  Requests a yes/no input with the given prompt, and keeps asking until
  a valid response is received. Input is compared against the
  REPLY_PATTERN_YES and REPLY_PATTERN_NO regex patterns.
  """
  
  reply_line = input(prompt)
  while True:
    if re.match(REPLY_PATTERN_YES, reply_line):
      return True
    elif re.match(REPLY_PATTERN_NO, reply_line):
      return False
    print("Unrecognized input.", end = "\n\n")
    reply_line = input(prompt)


class Game(object):
  """
  A wrapper for an ongoing game of Blackjack.
  """
  
  def __init__(self, starting_money = 100.00)
    self._player_money = starting_money
    self._deck = Deck()
