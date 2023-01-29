class Entity():
    def __init__(self, name, starting_location):
        self.location = starting_location
        self.name = name
        self.inventory = []

    def get_name(self):
        return self.name

    def get_inventory(self):
        return self.inventory

    def get_location(self):
        return self.location

    def set_name(self, name):
        self.name = name

    def equip_item(self, item):
        try:
            self.inventory.append(item)
            self.location.items.remove(item)
        except ValueError:
            print("That item does not exist.")

    def in_inventory(self, item):
        for held_item in self.inventory:
            if held_item == item:
                return True
        return False

    def move(self, direction):
        try:
            self.location = self.location.linked_rooms[direction]
            print("you moved", direction)
            print(self.location)
        except KeyError:
            print("invalid move direction")


class Player(Entity):
    def __init__(self, starting_location, carry_capacity):
        self.carry_capacity = carry_capacity
        self.current_weight = 0
        super().__init__("Player", starting_location)

    def get_carry_capacity(self):
        return self.carry_capacity

    def get_current_weight(self):
        return self.current_weight

    def set_carry_capacity(self, carry_capacity):
        self.carry_capacity = carry_capacity

    def get_item(self, item):
        try:
            if self.current_weight + item.get_weight() > self.carry_capacity:
                print(f"you can't equip the {item.get_name()}, it's too heavy")
            else:
                self.inventory.append(item)
                self.location.items.remove(item)
                self.current_weight += item.get_weight()
        except ValueError:
            print("That item does not exist.")
