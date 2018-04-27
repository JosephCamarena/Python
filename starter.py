from random import randint
rand_num = randint(1,10)
again = None
while  again != "n":
	user = int(input("Guess a number between 1 and 10: ")) # handle user guesses
	if user == rand_num:  # if they guess correct, tell them they won
		print("You guessed it! You won!")
		rand_num = randint(1,10)
		again = input("Do you want to keep playing? (y/n) ") # BONUS - let player play again if they want!
	elif user > rand_num: # otherwise tell them if they are too high or too low
		print("Too high, try again!")
	else:
		print("Too low, try again!")

# instructor code
random_number = randint(1,10)
while True:
	guess = input("Pick a number from 1 to 10: ")
	guess = int(guess)
	if guess < random_number:
		print("Too low!")
	elif guess > random_number:
		print("Too high!")
	else:
		print("You Won!!")
		play_again = input("Do you want to play again? (y/n) ")
		if play_again == "y":
			random_number = randint(1,10)
			guess = None
		else:
			print("Thank you for playing!")
			break