from Room import Room
from Entity import Player
from Item import Weapon

sword = Weapon("sword", 15, 10)

kitchen = Room("kitchen")
kitchen.set_description("A kitchen")

dining_hall = Room("Dining hall")
dining_hall.set_description("you eat food here bro")

ballroom = Room("Ballroom")
ballroom.set_description("you do be dancing bro")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")

dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
ballroom.add_item(sword)

player1 = Player(kitchen, 999)
print(player1)

while not player1.in_inventory(sword):
    print("\n")
    print(player1.location)
    command = input("Please enter what you want to do: ")
    match command:
        case "equip":
            name_of_item = input("what is the name of the item: ")
            item = player1.location.get_item_by_name(name_of_item)
            player1.equip_item(item)
        case "move":
            direction = input("Please enter the direction: ")
            player1.move(direction)

    print("you have: ", *player1.get_inventory())

print("your won")
