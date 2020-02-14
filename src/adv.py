from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("Iphone", "Unforutnately uses Sprint, no phone calls can be made")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Stick of Gum", "Your breath stinks, you'll probably need this!")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Lego", "Stepped on this when you walked in, probably hurt like hell!")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("Chinese Delivery Menu", "Old menu but from a trusty establishment, too bad you have no phone to order on...")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("Opened Treasure Chest", "Only contains a piece of paper with an I.O.U. written on it.")]),
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

player = Player("John", room["outside"], [])
print(f"Player {player.name} is currently in {player.current_room.roomName}")

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


m = ""

while m != "q":

    m = input("Move by inputting n, s, e, or w to move or press q to quit  ")

    if m == "n":
        if player.current_room.n_to is not None:
            player.current_room = player.current_room.n_to
            print(f"{player.name} has moved to {player.current_room.roomName}. {player.current_room.description}")
        else:
            print("Nothing appears to be in that direction!")
    
    elif m == "s":
        if player.current_room.s_to is not None:
            player.current_room = player.current_room.s_to
            print(f"{player.name} has moved to {player.current_room.roomName}. {player.current_room.description}")
        else:
           print("Nothing appears to be in that direction!")

    elif m == "e":
        if player.current_room.e_to is not None:
            player.current_room = player.current_room.e_to
            print(f"{player.name} has moved to {player.current_room.roomName}. {player.current_room.description}")
        else:
           print("Nothing appears to be in that direction!")

    elif m == "w":
        if player.current_room.w_to is not None:
            player.current_room = player.current_room.w_to
            print(f"{player.name} has moved to {player.current_room.roomName}. {player.current_room.description}")
        else:
           print("Nothing appears to be in that direction!")

    elif m == "q":
        print("Goodbye!")
        exit()
    else:
        print('Move by inputting n, s, e, or w')

    
