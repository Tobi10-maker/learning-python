import math

queue = [("Wizkid", "Essence"),
         #  ("Davido", "Unavailable"),
         #  ("Burna Boy", "Last Last"),
         #  ("Rema", "Calm Down"),
         ("Asake", "Lonely At The Top")]


def show_queue(queue):

    # the """ is called a DOCSTRING it is used to tell what a string is supposed to do its a bit different from a comment
    """ Print everyone currently in the queue """
    if len(queue) == 0:
        print("The queue is empty")
        return
    else:
        print("Current Queue:\n")
        for i, singer in enumerate(queue):
            # enumerate this command is used to index
            name, song = singer
            print(f"{i + 1} {name} - {song}")


def prompt_for_singer():
    name = input("Name:")
    song = input("Song:")
    return [(name.strip().title()), (song.strip().title())]


def add_singer(queue):
    """This will add new singers"""

    singer, song = prompt_for_singer()
    if len(singer) == 0 or len(song) == 0:
        print("\nU entered a blank input\n")
        return
    print(f"Added {singer} to the queue\n")
    queue.append((singer, song))


def next_singer(queue):
    if len(queue) == 0:
        print("Oops there is no one left to call up!")
        return

    first_singer = queue.pop(0)
    name, song = first_singer
    print(f"NOW UP: {name} - {song}\n")
    # return first_singer


def remove_singer(queue):
    """This removed a singer"""
    if len(queue) == 0:
        print("The queue is empty no singer to remove")
        return
    who_to_remove = input("Who do you wan to remove: ").strip().title()

    for singer in queue:
        if singer[0] == who_to_remove:
            queue.remove(singer)
            print(f"\n{who_to_remove} was removed from the queue\n")
            return
    print(f"\nThere is no match for {who_to_remove}\n")


def move_to_top(queue):
    if len(queue) <= 1:
        print("The current queue is at the top")
        return
    position_move_to = int(input(
        "Who do u want to move to the top? Enter a number: \n"))
    if position_move_to > {len(queue + 1)}:
        print("Number entered is not in the queue")
        return
    remove_from_queue = queue.pop(position_move_to - 1)
    name, song = remove_from_queue
    queue.insert(0, remove_from_queue)
    print(f"\nMoved {name} to the top of the queue!\n")


def run_app(queue):
    print("=" * 44)
    print("Welcome to Sign Out: A Karaoke Queue Manager")
    print("=" * 44)

    is_running = True

    while is_running:
        show_queue(queue)
        print("\nOptions: add / remove / quit / next / top")
        command = input(">")

        if command == "quit":
            is_running = False
            print("Good night!")
        elif command == "add":
            add_singer(queue)
        elif command == "remove":
            remove_singer(queue)
        elif command == "next":
            next_singer(queue)
        elif command == "top":
            move_to_top(queue)
        else:
            print(f"\nSorry i dont know the command '{command}'")


run_app(queue)
