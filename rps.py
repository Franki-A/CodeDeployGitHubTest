import sys 
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("")
playerchoice = input("Hi Joshua let's play rock, paper and scissor\n Enter...\n 1 for Rock,\n 2 for Paper, or \n 3 for Scissor:\n\n")

player = int(playerchoice)

if player < 1 or player> 3:
    sys.exit("You must enter 1, 2, or 3.")

computerchoice = random.choice("123")

computer = int(computerchoice)

print("")
print("You chose " + str(RPS(player)).replace('RPS.','') + ".")
print("AI chose " + str(RPS(computer)).replace('RPS.','') + ".")
print("")

if player == 1 and computerchoice == 3: 
    print("You win! 🎉 Rock beats Scissor")
elif player == 2 and computerchoice == 1: 
    print("You win! 🎉 Paper beats Rock")
elif player == 3 and computerchoice == 2: 
    print("You win! 🎉 Scissor beats Paper")
elif player == computer:
    print("😲 Tie game, do it again")
else:
    print("AI 🤖 Wins")

