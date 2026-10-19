import random

# List of words to choose from
words = ["apple", "banana", "cherry", "date",
         "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine",]

# Select a random word from the list
random_words = random.choice(words)


# print(random_words)

letters = list(random_words)

# Jumble the letters
random.shuffle(letters)
# print(letter


print(f"Scrambled word: {''.join(letters)}")


# Equality operator

users_choice = input(
    "Type your guess or type 'skip' to skip the word and see the correct answer: ").strip().lower()

if users_choice == 'skip':
    print(f"The correct answer is: {random_words}")
elif users_choice == random_words:
    print("Congratulations! You guessed the correct word!")
else:
    print(f"Sorry, the correct answer is: {random_words}")
