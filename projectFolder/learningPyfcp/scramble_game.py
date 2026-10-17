import random
# learning lists part 1

skills = ['Python', 'Java', 'C++']
years = [3, 5, 2]

# print(skills)
# print(years)

# learning lists part 2

play_list = ['Drake', 'Burna Boy', 'Wizkid', 'Davido']
print()
# print(play_list)


tickets = ['Ada', 'Tobi', 'Chidi', 'Emeka']

# print(f"Now helping: {tickets[0]}")
# print(f"Next in line: {tickets[1]}")
# print(f"Last in line: {tickets[-1]}")

# The list function
# this turn the string into list this is how we convert to list in python list()

letters = list("listen")
# print(letters)

# print(sorted(letters))

# Random module
lunch_spots = ['KFC', 'Dominos', 'Pizza Hut', 'Chicken Republic', 'Taco Bell']
# print(random.choice(lunch_spots))

random.shuffle(lunch_spots)
# print(lunch_spots)

players = ['Tobi', 'Chidi', 'Emeka', 'Ada']
random.shuffle(players)
# print(f"Our players are: {players}")
# print(f"{random.choice(players)} deals first")

# Join function it transforms a list into a string

result = "=".join(players)
# print(result)

letters = ['p', 'y', 't', 'h', 'o', 'n']
# print("".join(letters))


# Equality operator


promo_code = "FLASH50"

# input_promo_code = input("Enter your promo code: ")

# print(f"promo code entered is: {input_promo_code == promo_code}")


# if else
# input_score = int(input("Enter your score: "))

# if input_score >= 60:
#     # print("You passed the test!")
# else:
#     # print("You failed the test!")

# elif statement

signal = 2

if signal == 0:
    print(f"50% off, sorry for the WIFI issues")
elif signal == 1 or signal == 2:
    print(f"20% off, sorry for the WIFI issues")
elif signal == 3 or signal == 4:
    print(f"10% off, sorry for the WIFI issues")
elif signal == 5:
    print("Full bar no discount today")
else:
    print("Enter a WIFI strength within the range of 0-5")


# string method
# calling .stripe only removes whitespace from the beginning and end of a string, not in between words


# Tuple
# Tuples are similar to lists, but they are immutable, meaning their values cannot be changed after they are created. Tuples are defined using parentheses () instead of square brackets [].

# unpacking tuples
# unpacking is a way to assign the values of a tuple to individual variables in a single line of code. This can be useful when you want to extract specific values from a tuple without having to access them by index.

steel_blue = (70, 130, 180)

# unpacking in action
red, green, blue = steel_blue

inventory = [("apple", 10), ("banana", 5), ("orange", 8)]

item, quantity = inventory[0]
print(f"{item}: {quantity} in stock")

item, quantity = inventory[1]
print(f"{item}: {quantity} in stock")

item, quantity = inventory[2]
print(f"{item}: {quantity} in stock")
