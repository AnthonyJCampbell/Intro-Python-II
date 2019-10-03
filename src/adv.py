from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("sword", "Pointy!")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("saddle", "Seems comfortable")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("rope", "I don' think I could use this to clim across")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("torch", "It's been lit recently...")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("gold", "Oooohhh shiny!")]),
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
    items_in_room = [item.name for item in current_room.item_list]
    
    print("\n===================================================")
    print(f"Current location: {current_room.name}")
    print(f"Description: {current_room.description}")
    print(f"Items in the room: {items_in_room}")
    print("===================================================\n\n")

    # Get Command
    command = input("\nPlease provide a direction to move to (n/s/w/e): ").lower().split(" ")


    if len(command) < 2:
        command = command[0]
        # No spaces in input means it's for directions
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
    
    else:
        # Case: len(command) > 1
        if command[0] == "get" or command[0] == "g" or command[0] == "take" or command[0] == "t":

            # look at the contents of the current `Room` to see if the item is there.
            if command[1] in items_in_room:
                # If it is there, remove it from the `Room` contents, and add it to the `Player` contents.

                player.inventory[command[1]] = current_room.item_list[0]
                current_room.item_list.pop()
                
                player.inventory[command[1]].on_take()

            else: 
                print(f"There's no item called '{command[1]}' in the {current_room.name}")
            
        
        # Drop item:
        elif command[0] == "drop" or "d":
            if command[1] in player.inventory:
                current_room.item_list.append(player.inventory[command[1]])
                del player.inventory[command[1]]

            else: 
                print(f"You don't have an item called '{command[1]}' in your inventory silly! \n")
                


print("\n\nGoodbye!\n\n")