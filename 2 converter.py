#converting kilometers to miles
print("How many kilometers did you cycle today?")
kms = input()
miles = float(kms)/1.60934
miles = round(miles, 2)
print(f"Your {kms}km ride was {miles}mi")
# print(f"That is equal to {round(miles, 2)} miles") | returns miles with 2 decimal places
# print(f"That is equal to {miles} miles") | prints a long decimal number
# round(thing to round, how many decimal points)
