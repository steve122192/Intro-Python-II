from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons",
                     [Item('Torch','light your way')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
[Item('Bread','gain energy'), Item('Meat','build strength')]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
[Item('Coin',' buy items')])
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
player1 = Player('Steve', room['outside'])

while True:
    print(player1.current_room.name)
    print(player1.current_room.description)
    if len(player1.current_room.items) != 0:
        items_list = player1.current_room.items.copy()
        for item in items_list:
            good_answer = False
            print(f"You Found:\n{item.name} to {item.description}")
            while good_answer is False:
                ans = input('Take Item?(y/n):')
                if ans == 'y':
                    player1.items.append(item)
                    player1.current_room.items.remove(item)
                    good_answer = True
                elif ans == 'n':
                    good_answer = True
                else:
                    print('Choose yes or no!')

        
        items_list = []
        for item in player1.items:
            items_list.append(item.name)
        print(f'Your Inventory:{str(items_list)[1:-1]}')

        good_answer = False
        while good_answer is False:
            ans = input('Manage Inventory?(y/n):')
            if ans == 'y':
                good_answer = True
                items_list = player1.items.copy()
                for item in items_list:
                    rem = input(f'Remove {item.name}?(y/n)')
                    if rem == 'y':
                        player1.items.remove(item)
                        player1.current_room.items.append(item)
                        item_list = []
                        for item in player1.items:
                            item_list.append(item.name)
                        print(f'Your Inventory:{str(item_list)[1:-1]}')
                    elif rem == 'n':
                        pass
                    else:
                        pass
            elif ans == 'n':
                good_answer = True
            else:
                print('Choose yes or no!')




    else:
        print('No itmes to be found in this room...')
    direction = input('Which direction do you move?(n,s,e,w):')
    if direction == 'n':
        try:
            player1.current_room = player1.current_room.n_to
        except:
            print('You can not move in this direction!')
    if direction == 's':
        try:
            player1.current_room = player1.current_room.s_to
        except:
            print('You can not move in this direction!')
    if direction == 'e':
        try:
            player1.current_room = player1.current_room.e_to
        except:
            print('You can not move in this direction!') 
    if direction == 'w':
        try:
            player1.current_room = player1.current_room.w_to
        except:
            print('You can not move in this direction!')
    if direction == "inventory":
        item_list = []
        for item in player1.items:
            item_list.append(item.name)
        print(f'Your Inventory:{str(item_list)[1:-1]}')
    if direction == 'q':
        break 

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
