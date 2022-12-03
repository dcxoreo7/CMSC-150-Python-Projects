# north,east,south, or west


room_list = []
room = ["You are in a large field. There is a town to the east. There is a bleak looking castle north.", 6, 1, 3, 5]
room_list.append(room)
room = ["You are in a town. You feel a light breeze coming from a passage to the south.", None, None, 2, 0]
room_list.append(room)
room = ["You are in a dense and somewhat mystical forest. There is a sound rushing water to the west", 1, None, None, 3]
room_list.append(room)
room = ["You find yourself looking upon a giant lake. You see a trail of sand that leads further west", 0, 2, None, 4]
room_list.append(room)
room = ["You are now in a large desert. You know of a chapel to the north", 5, 3, None, None]
room_list.append(room)
room = ["You are in a temple that contains a powerful and ancient magic. There is a vast field east", None, 0, 4, None]
room_list.append(room)
room = ["You are in a castle and feel an evil presence. There is a field south of here", None, None, 0, None]
room_list.append(room)

current_room = 0



done = False
while done == False:

    print(room_list[current_room][0])
    user_choice = input("What do you want to do? ")
    if user_choice.upper() == "N" or user_choice.upper() == "NORTH":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("Can't go that way.")
        else:
            current_room = next_room

    elif user_choice.upper() == "E" or user_choice.upper() == "EAST":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("Can't go that way.")
        else:
            current_room = next_room

    elif user_choice.upper() == "S" or user_choice.upper() == "SOUTH":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("Can't go that way.")
        else:
            current_room = next_room

    elif user_choice.upper() == "W" or user_choice.upper() == "WEST":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("Can't go that way.")
        else:
            current_room = next_room

    elif user_choice.upper() == "Q" or user_choice.upper() == "QUIT":
        done = True

    else:
        print("Invalid command")






