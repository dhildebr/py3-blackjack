"""
The main program entry point for the game of Blackjack. 
"""

from game import Game
from game import parse_reply_yn, parse_reply_bet_amt

if __name__ == "__main__":
  print("Welcome to Blackjack. Try not to lose your shirt.")
  print("If at any point you need some help, type \"help\" at any input prompt.")
  
  blackjack = Game(100.00)
  print(f"You'll be starting out with ${blackjack.player_money()} to your name.")
  
  continue_game = True
  while continue_game:
    bet_amt = parse_reply_bet_amt("How much would you like to bet? ")
    blackjack.play_round(bet_amt)
    
    print(f"You have ${blackjack.player_money()} remaining.")
    continue_game = parse_reply_yn("Do you want to play again? ")
  print("Goodbye.")
