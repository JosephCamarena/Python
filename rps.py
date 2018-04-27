 # basic version; on  my own
# ...rock...
# ...paper...
# ...scissors...
# (enter player 1's choice): rock
# (enter player 2's choice): paper
# SHOOT!
# player2 wins

print("...rock...\n...paper...\n...scissors...")
player1 = input("Player 1, enter your choice: ")
player2 = input("Player 2, enter your choice: ")
print("SHOOT!")
if player1 and player2:
	if (player1 == "rock" and player2 == "scissors") or (player1 == "paper" and player2 == "rock") or (player1 == "scissors" and player2 == "paper"):
		print("Player 1 wins!")
	elif (player1 == "paper" and player2 == "scissors") or (player1 == "scissors" and player2 == "rock") or (player1 == "rock" and player2 == "paper"):
		print("Player 2 wins!")
	elif player1 == player2: #teacher code
	# elif (player1 == "rock" and player2 == "rock") or (player1 == "paper" and player2 == "paper") or (player1 == "scissors" and player2 == "scissors"):
		print("Tie!")
	else:
		print("Woops, something went wrong!")		
else:
	print("Type rock, paper, or scissors!")

	# elif (player1 == "rock" and player2 == "rock") or (player1 == "paper" and player2 == "paper") or (player1 == "scissors" and player2 == "scissors"):
	# 	print("Tie!")

# instructor code
# if player1 == player2:
# 	print("Its a tie!")
# elif player1 == "rock":
# 	if player2 == "scissors":
# 		print("Player 1 wins!")
# 	elif player2 == "paper":
# 		print("Player 2 wins!")
# elif player1 == "paper":
# 	if player2 == "rock":
# 		print("Player 1 wins!")
# 	elif player2 == "scissors":
# 		print("Player 2 wins!")
# elif player1 == "scissors":
# 	if player2 == "paper":
# 		print("Player 1 wins!")
# 	elif player2 == "rock":
# 		print("Player 2 wins!")
# else:
# 	print("something went wrong")