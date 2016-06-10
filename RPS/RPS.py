'''Rock, Paper, Scissors'''
from random import randint
from time import sleep

options = ["R", "P", "S"]
lost_message = "You Lost!"
win_message = "You Win!"

def decide_winner(user_choice, computer_choice):
  print "You selected %s" %(user_choice)
  print "Computer selecting..."
  sleep(1)
  print "Computer selected %s" %(computer_choice)
  user_choice_index = options.index(user_choice)
  computer_choice_index = options.index(computer_choice)
  if user_choice_index == computer_choice_index:
    print "Tie!"
    return
  elif user_choice_index == 0:
    if computer_choice_index == 1:
      print lost_message
    else:
      print win_message
  elif user_choice_index == 1:
    if computer_choice_index == 2:
      print lost_message
    else:
      print win_message
  elif user_choice_index == 2:
    if computer_choice_index == 0:
      print lost_message
    else:
      print win_message
  else:
    print "Invalid input"
    return
    
def play_RPS():
  print "Rock, Paper, Scissors!"
  user_choice = raw_input("Select R for Rock, P for Paper, or S for Scissors: ").upper()
  sleep(1)
  computer_choice = options[randint(0, len(options) - 1)]
  decide_winner(user_choice, computer_choice)

play_RPS()
    
    
    
  