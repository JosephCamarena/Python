# advanced version of Rock Paper Scissors, with computer AI, using a While loop
# Includes score tracking. First to 2 wins.
# My Code:
from random import choice
player_wins = 0
computer_wins = 0
winning_score = 2

while player_wins < winning_score and computer_wins < winning_score:
	ai = choice(['rock', 'paper', 'scissors'])
	print(f"Player Score: {player_wins}\nComputer Score: {computer_wins}")
	print("rock...\npaper...\nscissors...")
	print("Computer has chosen.")
	player = input("Player, enter your choice of rock, paper, or scissors: ").lower()
	if player == "quit" or player == "q":
		break
	print("SHOOT!")
	if player:
		if (ai == "rock" and player == "scissors") or (ai == "paper" and player == "rock") or (ai == "scissors" and player == "paper"):
			print(f"Computer wins!\nComputer chose {ai}")
			computer_wins += 1
		elif (ai == "paper" and player == "scissors") or (ai == "scissors" and player == "rock") or (ai == "rock" and player == "paper"):
			print(f"You win!\nComputer chose {ai}")
			player_wins += 1
		elif ai == player:
			print("Tie!")
		else:
			print("Woops, something went wrong!")		
	else:
		print("Type rock, paper, or scissors!")

if player_wins > computer_wins:
	print("Congrats, you won!")
elif player_wins == computer_wins:
	print("It's a tie!")
else:
	print("Oh no, the computer won :(")
