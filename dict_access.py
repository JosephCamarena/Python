from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# YOUR CODE GOES BELOW:
if food == bakery_stock.keys():
    if food == "toffee cookie":
        print("3 left")
    elif food == "morning bun":
        print("1 left")
    elif food == "tea cake":
        print("25 left")
    else:
       print("We don't make that")
else:
    print("We don't make that")