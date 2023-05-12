from game import data

class Item:
    def __init__(self, name, description, quantity: int=1) -> None:
        self.name = name
        self.quantity = quantity
        self.description=description
    def get_desc(self):
        return self.description
    def use_item(self):
        return 0
    #temp solution to bludgeoning problem
    def get_bludgeoning(self):
        return 0
    def to_string(self):
        return self.name
    
   
class Melee_Weapon(Item):
    def __init__(self, name, damage, description, quantity: int=1):
        self.name = name
        self.quantity = quantity
        self.damage= (-1 * abs(damage))
        self.description= description
    
    def use_item(self):
        return self.damage


class Range_Weapon(Item):
    damage=0
    max_range = 0
    current_range=0

    def __init__(self, name, damage, range, description):
        self.name=name
        self.damage= (-1 * abs(damage))
        self.description= description
        self.max_range=range
    
    def find_range(self, range):
        self.current_range=range

    def use_item(self):
        if self.max_range >= self.current_range:
            return self.damage
        elif self.max_range<self.current_range:
            print("out of range bozo kys")
            return 0

    def get_range(self):
        return self.current_range


class Bludgeoning_Weapon(Item):
    damage = 0
    #blugeoning should be a decimal, never more than 1
    bludgeoning=0
    
    def __init__(self, name, damage, bludgeoning, description):
        self.name=name
        self.damage = (-1 * abs(damage))
        self.bludgeoning = bludgeoning
        self.description=description
   
    def get_bludgeoning(self):
        return self.bludgeoning

    def use_item(self):
        return self.damage

class Energy_Drink(Item):
    speed_boost=0
    
    def __init__(self, speed_boost):
        self.speed_boost=speed_boost

    def use_item(self):
        return self.speed_boost

        
class Iced_Tea(Item):
    health_gain=0
    
    def __init__(self, health_gain):
        self.health_gain=abs(health_gain)
    def use_item(self):
        return self.health_gain


class Pre_Workout(Item):
    dmg_boost=0
    
    def __init__(self, dmg_boost):
        self.dmg_boost=abs(dmg_boost)

    def use_item(self):
        return self.dmg_boost


class Budget_Steriods(Item):
    health_gain=0
    dmg_boost =0
    
    def __init__(self, health_gain=0, speed_boost=0, dmg_boost=0):
        self.health_gain-=health_gain
    def use_item(self):
        return self.health_gain
    



class Armor(Item):
    #defense should always be a decimal value
    defense=0
    
    def __init__(self, defense):
    
        self.defense = defense
   
    def get_defense(self):
        return self.defense
