# Loop through nums 1-20
# for 4 and 13, print 'x is unlucky'
# for even nums, print 'x is even'
# for odd nums, print 'x is odd'
for num in range(1,21):
	if num % 2 == 0 and not num == 4:
		print(f"{num} is even")
		num += 1 #I do not need to += as the for loop already does that
	elif num == 4 or num == 13:
		print(f"{num} is unlucky!")
		num += 1
	else:
		print(f"{num} is odd")
		num += 1

# instructor v1
# for num in range(1,21):
# 	if num == 4 or num == 13:
# 		print(f"{num} is unlucky")
# 	elif num % 2 == 0:
# 		print(f"{num} is even")
# 	else:
# 		print(f"{num} is odd")

# instructor v2
for num in range(1,21):
	if num == 4 or num == 13:
		state = "unlucky"
	elif num % 2 == 0:
		state = "even"
	else:
		state = "odd"
	print(f"{num} is {state}")