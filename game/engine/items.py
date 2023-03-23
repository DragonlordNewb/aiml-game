from game import data

class Item:
    def __init__(self, name, quantity: int=1) -> None:
        self.name = name
        self.quantity = quantity
        self.desc="Description: your mother"
    def get_desc(self):
        return self.desc
    def use_item(self):
        return 0
    
    def __str__(self) -> str:
        if self.quantity == 1:
            if self.name[0] in data.VOWELS:
                return "an " + str(self.name)
            return "a " + str(self.name)
        return str(self.quantity) + " " + self.name + "s"

    def __repr__(self) -> str:
        return str(self)

    def __iadd__(self, n: int) -> object:
        return type(self)(self.name, quantity + n)

    def __isub__(self, n: int) -> object:
        return type(self)(self.name, quantity - n)

class Melee_Weapon(Item):
    damage=0
    desc=""

    def __init__(self, dmg, descr):
        self.damage= (-1 * abs(dmg))
        self.desc= descr
    
    def use_item(self):
        return self.damage

    def give_desc(self):
        return self.desc


class Range_Weapon(Item):
    damage=0
    desc=""
    max_range = 0
    current_range=0

    def __init__(self, dmg, rango, descr):
        self.damage= (-1 * abs(dmg))
        self.desc= descr
        self.max_range=rango
    
    def find_range(self, range):
        self.current_range=range

    def use_item(self):
        if self.max_range >= self.current_range:
            return self.damage
        elif self.max_range<self.current_range:
            print("out of range bozo kys")
            return 0

    def give_desc(self):
        return self.desc

    def get_range(self):
        return self.current_range

class Potion(Item):
    health_gain=0
    
    def __init__(self, hG):
        self.health_gain=abs(hG)
    def use_item(self):
        return self.health_gain
