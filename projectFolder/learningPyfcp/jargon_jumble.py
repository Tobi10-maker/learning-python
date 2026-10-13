import random

# List of words to choose from
words = ["apple", "banana", "cherry", "date",
         "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine",]

# Select a random word from the list
random_words = random.choice(words)


print(random_words)

letters = list(random_words)

# Jumble the letters
random.shuffle(letters)
# print(letters)


print(f"Scrambled word: {''.join(letters)}")


# Equality operator
