
count = 0

for num in range(1, 10):
    if num % 2 == 0:
        count += 1
        print(f"{num} is even")

print(f"we have {count} even numbers")


def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}! Welcome to the program.")
    print("This function greets the user.")


greet("Odumasa", "Tobi")


def get_greeting(name):
    return f"Hello, {name}"


message = get_greeting("Odumasa")
print(message)
