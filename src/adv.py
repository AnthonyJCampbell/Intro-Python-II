from room import Room

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
current_room = "outside"

while active is True:
    print("\n\n========= WELCOME TO ROOM CRAWLER (TM) =========\n\n")
    print(f"Current location: {room[current_room].name}")
    print(f"Description: {room[current_room].description}\n")

    command = input("\nPlease provide a command to get the adventure started: ")

    if any(dir in command for dir in ("n", "e", "s", "w")):
        print('test') 
    #   check if current room has a room in the given direction
    #       if so, move there
    #       if not, return an error message


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