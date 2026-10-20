queue = [("Tobi", "Ojo", "Seun", "obi")]


def show_queue(queue):
    # the """ is called a DOCSTRING it is used to tell what a string is supposed to do its a bit different from a comment
    """ Print everyone currently in the queue """
    print("[the queue goes here!]")


def add_singer(queue):
    """This will add new singers"""
    print("\n[add a singer!]")


def remove_singer(queue):
    """This removed a singer"""
    print("\n[remove a singer!]")


def run_app(queue):
    print("=" * 44)
    print("Welcome to Sign Out: A Karaoke Queue Manager")
    print("=" * 44)

    is_running = True

    while is_running:
        show_queue(queue)
        print("\nOptions: add / remove / quit")
        command = input(">")

        if command == "quit":
            is_running = False
            print("Good night!")
        elif command == "add":
            add_singer(queue)
        elif command == "remove":
            remove_singer(queue)
        else:
            print(f"\nSorry i dont know the command '{command}'")


run_app(queue)
