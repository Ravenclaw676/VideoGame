class Item():
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return self.name

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def set_name(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, weight, damage):
        self.damage = damage
        super().__init__(name, weight)
