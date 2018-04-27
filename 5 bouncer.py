# this program will not work if input is a string or float
# nested statements
# Program is a bouncer at an 18+ club

# ask for age
age = input("How old are you? ")

# refactored
if age: #if an input is given
	age = int(age)
	if age >= 21:
		print("You are good to enter and can drink!")
	elif age >= 18:
		print("You can enter, but need a wristband!")
	else:
		print("You can't come in, little one! :(")
else:
	print("Please enter an age!")

# Option 1
# if age: #if an input is given
# 	age = int(age)
# 	if age >= 18 and age < 21:
# 		# 18-21 wristband
# 		print("You can enter, but need a wristband!")
# 	elif int(age) >= 21:
# 			# 21+ can drink, normal entry
# 		print("You are good to enter and can drink!")
# 	else:
# 		# too young, sorry
# 		print("You can't come in, little one! :(")
# else:
# 	print("Please enter an age!")

# Option 2
# if age != "":
# 	if int(age) >= 18 and int(age) < 21:
# 		# 18-21 wristband
# 		print("You can enter, but need a wristband!")
# 	elif int(age) >= 21:
# 			# 21+ can drink, normal entry
# 		print("You are good to enter and can drink!")
# 	else:
# 		# too young, sorry
# 		print("You can't come in, little one! :(")
# else:
# 	print("Please enter an age!")
