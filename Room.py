class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.items = []
        self.enemies = []
        self.total_enemies = 0

    def __repr__(self):
        string = self.name + "\n"
        string += self.description + "\n"
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            string += "The " + room.get_name() + " is " + direction + "\n"
        for item in self.items:
            string += str(item) + "\n"

        string += f"there is {self.total_enemies}"

        return string

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_item_by_name(self, name):
        for item in self.items:
            if item.get_name() == name:
                return item

    def get_total_enemies(self):
        return self.total_enemies

    def set_description(self, description):
        self.description = description

    def set_name(self, room_name):
        self.name = room_name

    def add_item(self, item):
        self.items.append(item)

    def add_enemy(self, enemy):
        self.enemies.append(enemy)
        self.total_enemies += 1

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)
        self.total_enemies -= 1

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
