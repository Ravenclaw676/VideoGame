class Player():
    def __init__(self, starting_location, carry_capacity):
        self.location = starting_location
        self.inventory = []
        self.carry_capacity = carry_capacity
        self.current_weight = 0

    def get_inventory(self):
        return self.inventory

    def get_location(self):
        return self.location

    def get_carry_capacity(self):
        return self.carry_capacity

    def get_current_weight(self):
        return self.current_weight

    def set_carry_capacity(self, carry_capacity):
        self.carry_capacity = carry_capacity

    def equip_item(self, item):
        try:
            if self.current_weight + item.weight > self.carry_capacity:
                print("you can not pick up the item, it is too heavy")
            else:
                self.inventory.append(item)
                self.location.items.remove(item)
                self.current_weight += item.weight
        except ValueError:
            print("That item does not exist.")

    def in_inventory(self, item):
        for held_item in self.inventory:
            if held_item == item:
                return True
        else:
            return False

    def move(self, direction):
        try:
            self.location = self.location.linked_rooms[direction]
            print("you moved", direction)
            print(self.location)
        except KeyError:
            print("invalid move direction")
