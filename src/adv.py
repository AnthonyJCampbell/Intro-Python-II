from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# INTRO
print("\n\n========= WELCOME TO ROOM CRAWLER (TM) =========\n\n")
playerName = input("What is your name, brave adventurer? ")
player = Player(playerName, room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


active = True

while active is True:
    # Destructuring values
    
    current_room = player.current_room
    print("\n===================================================")
    print(f"Current location: {current_room.name}")
    print(f"Description: {current_room.description}")
    print("===================================================\n\n")

    # Get Command
    command = input("\nPlease provide a direction to move to (n/s/w/e): ")

    # North
    if command == "n":
        if player.current_room.n_to:
            player.current_room = player.current_room.n_to
            print("\n\n")

        else:
            print("\n\nThat's not possible!\n\n")

    # South
    elif command == "s":
        if player.current_room.s_to:
            player.current_room = player.current_room.s_to
            print("\n\n")

        else:
            print("\n\nThat's not possible!\n\n")

    # East
    elif command == "e":
        if player.current_room.e_to:
            player.current_room = player.current_room.e_to
            print("\n\n")

        else:
            print("\n\nThat's not possible!\n\n")
    
    # West
    elif command == "w":
        if player.current_room.w_to:
            player.current_room = player.current_room.w_to
            print("\n\n")

        else:
            print("\n\nThat's not possible!\n\n")


    # If command is "q", set active to False and quit loop
    elif command == "q":
        active = False
    

    # In case of invalid input, return error
    else:
        print(f"""
                {command} is not a valid command!
        Use 'n', 's', 'w' or 'e' to move to a different room.
                    Or use `q` to quit
        """)


print("\n\nGoodbye!\n\n")