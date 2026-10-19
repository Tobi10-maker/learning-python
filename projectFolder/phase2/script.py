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
print(f"With tax, that comes to ${tax_together}")

full_name("Tobi", "Odumasa")
