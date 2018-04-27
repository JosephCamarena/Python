 # advanced version with computer AI; on  my own
from random import choice
ai = choice(['rock', 'paper', 'scissors'])
print("rock...\npaper...\nscissors...")
print("Computer has chosen.")
player = input("Player, enter your choice of rock, paper, or scissors: ").lower()
# Line 7: .lower() converts string input to lowercase so user can use any combination of string casing with no error
print("SHOOT!")
if player:
	if (ai == "rock" and player == "scissors") or (ai == "paper" and player == "rock") or (ai == "scissors" and player == "paper"):
		print(f"Computer wins!\nComputer chose {ai}")
	elif (ai == "paper" and player == "scissors") or (ai == "scissors" and player == "rock") or (ai == "rock" and player == "paper"):
		print(f"You win!\nComputer chose {ai}")
	elif ai == player:
		print("Tie!")
	else:
		print("Woops, something went wrong!")		
else:
	print("Type rock, paper, or scissors!")

# # instructor code
# from random import randint
# rand_num = randint(0,2)
# if rand_num == 0:
# 	computer = "rock"
# elif rand_num == 1:
# 	computer = "paper"
# else:
# 	computer = "scissors"
# print("rock...\npaper...\nscissors...")
# print("Computer has chosen.")
# player = input("Player, enter your choice of rock, paper, or scissors: ").lower()
# if player == computer:
# 	print("Its a tie!")
# elif player == "rock":
# 	if computer == "scissors":
# 		print("Player wins!")
# 	else:
# 		print("Computer wins!")
# elif player == "paper":
# 	if computer == "rock":
# 		print("Player wins!")
# 	else:
# 		print("Computer wins!")
# elif player == "scissors":
# 	if computer == "paper":
# 		print("Player wins!")
# 	else:
# 		print("Computer wins!")
# else:
# 	print("something went wrong")