# Program was supposed to display smiley emojis in a pyramid order
# emoji did not work, so I used 'x' instead
# my code
num = 1
while num < 11:
	for x in range(1,11):
		print(f"{x}"*num)

# instructor code
# for num in range(1,11):
# 	print("x" * num)

# times = 1
# while times < 11:
# 	print("x" * times)
# 	times += 1

# nested loop
# for x in range(3):
# 	for num in range(1,11):
# 		print("x" * num)


# without string multiplication - ugly solution
# for num in range(1,11):
# 	count = 1
# 	smily = ""
# 	while count < num:
# 		smily += "x"
# 		count += 1
# 	print(smily)
