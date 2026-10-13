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
print(result)

letters = ['p', 'y', 't', 'h', 'o', 'n']
print("".join(letters))


# Equality operator
