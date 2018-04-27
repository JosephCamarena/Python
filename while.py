# msg = input("What's the secret password? ")
# while msg != "bananas":
# 	print("WRONG!")
# 	msg = input("What's the secret password? ")
# print("CORRECT!")

# for num in range(1,11):
# 	print(num)

# num = 1
# while num < 11:
# 	print(num)
# 	num += 1

# cannot be duplicated in a For Loop
msg = input("Hey how's it going? ")
while msg != "stop copying me":
	print(msg)
	msg = input()
print("UGH FINE YOU WIN")

msg = input("Hey how's it going? ")
while msg != "stop copying me":
	msg = input(f"{msg}\n")
print("UGH FINE YOU WIN")