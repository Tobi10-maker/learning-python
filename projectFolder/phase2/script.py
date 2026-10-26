import random
import math

# functions
# functions in python is defined using `def` meaning define


def roll_dice():
    roll = random.randint(1, 6)
    print(f"You rolled a {roll}")


# roll_dice()
# roll_dice()


def coffee_shop():
    print("\nIm headed to the coffee shop who wants a latte?")


def coffee_cost():
    print(f"\nThe total cost of coffee is {5*6}\n")


def thank_you():
    print("You are welcome !!")
    print("You are welcome !!")


def coffee_run():
    coffee_shop()
    coffee_cost()
    thank_you()
    thank_you()
    thank_you()


# coffee_run()


# function parameters and function arguements


def add_number(num1, num2):
    sum = num1+num2
    print(f"the sum of {num1} and {num2} is {sum}")


def scramble(words):
    letters = list(words)
    random.shuffle(letters)
    print(f"{words} is scrambled to: {''.join(letters)}")


add_number(20, 12)
scramble("animal")

# return values
# this is how we get a value out of a statement rather than just displaying it


def room_area(length, width):
    area = length * width
    return area


def add_tax(price):
    total_tax = price * 1.08
    return total_tax


def full_name(first, last):
    print(f"Welcome, {first} {last}")


room_size = room_area(32, 9)
print(f"The room size is {room_size}")

tax_together = round(add_tax(87), 0)
print(f"With tax, that comes to ${tax_together}\n\n\n")

full_name("Tobi", "Odumasa")


# for loop

guests = ["Dara", "Taye", "Kenny", "Odun"]

for guest in guests:
    print(guest)


nominees = ["pixapal", "TaskTanic", "SnackMap", "MoodTunes"]

awards = ["Best payment app", "Best productivity app",
          "Best snacking app", "Best music app"]

for nominee in nominees:

    print(f"\nNominated for best app {nominee}")


print("\nAnd those are your nominees")


# Loop through list of tuples

guests = [("Marcus", "Lasagna"), ("Lena", "Salad"), ("Sarah", "Brownies")]

for guest in guests:
    name, dish = guest
    print(f"\n{name} is bringing {dish}")


lineups = [
    ("The Wailers", "reggae", 45),
    ("Daft Punk", "electronic", 90),
    ("Adele", "pop", 60),
    ("Metallica", "metal", 100)]


for lineup in lineups:
    band, genre, minutes = lineup

    if minutes >= 90:
        print(f"\n{band} ({genre}) plays a long set: {minutes} minutes")
    else:
        print(f"\n{band} ({genre}) plays {minutes} minutes")


# pop
# the diference between pop and remove is that pop remove item by index while .remove remove item by value

lineup_pop = lineups.pop(0)
print(lineup_pop)


# .insert() this command is used to insert in a specific index with a specific value
