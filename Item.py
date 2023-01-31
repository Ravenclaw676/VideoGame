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
    
    def attack(self, target):
        target.set_health(target.get_health() - self.damage)
        if target.get_health() == 0:
            target.get_location().remove_enemy(target)
            print("The enemy is dead")

