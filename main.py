from Room import Room
from Entity import Entity, Player
from Item import Weapon


def main():
    sword = Weapon("sword", 15, 10)

    kitchen = Room("kitchen")
    kitchen.set_description("A kitchen")

    dining_hall = Room("Dining hall")
    dining_hall.set_description("you eat food here bro")

    ballroom = Room("Ballroom")
    ballroom.set_description("you do be dancing bro")

    boss = Entity("boss", ballroom, 10)
    ballroom.add_enemy(boss)

    dining_hall.link_room(ballroom, "west")
    ballroom.link_room(dining_hall, "east")
    ballroom.add_item(sword)

    quitting = False
    while not quitting or ballroom.get_total_enemies() > 0:
        print("\n")
        command = input("Please enter what you want to do: ")
        match command:
            case "equip":
                name_of_item = input("what is the name of the item: ")
                item = player1.location.get_item_by_name(name_of_item)
                player1.equip_item(item)
            case "move":
                direction = input("Please enter the direction: ")
                player1.move(direction)
            case "attack":
                player1.weapon.attack(player1.location.enemies[0])
            case "quit":
                quitting = True
                continue
            case _:
                print("Invalid input")

        print(player1)

        if quitting:
            print("You quit")
        else:
            print("your won")


if __name__ == "__main__":
    main()
