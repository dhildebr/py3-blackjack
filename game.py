"""

"""

import re

REPLY_PATTERN_YES = r"(?i)^\s*(Y(?:ES|EA)?)\s*$"
REPLY_PATTERN_NO =  r"(?i)^\s*(N(?:O|AY)?)\s*$"

REPLY_PATTERN_HIT =   r"(?i)^\s*(HIT(?: ME(?:,? BABY,? ONE MORE TIME)))\s*$"
REPLY_PATTERN_STAND = r"(?i)^\s*((?:I )?STAND|WOULD THE REAL \w+(?: \w+)* PLEASE STAND UP\??)\s*$"
REPLY_PATTERN_MONEY = r"(?i)^\s*(\$?(?P<amt>\d+(?:\.\d\d)?))\s*$"

class Game(object):
  """
  
  """
  
  def __init__(self, starting_money = 100.00)
    self._player_money = starting_money
