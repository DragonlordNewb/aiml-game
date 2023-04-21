# THE ACCOMPANYING PROGRAM IS PROVIDED UNDER THE TERMS OF THIS ECLIPSE
# PUBLIC LICENSE ("AGREEMENT"). ANY USE, REPRODUCTION OR DISTRIBUTION
# OF THE PROGRAM CONSTITUTES RECIPIENT'S ACCEPTANCE OF THIS AGGREMENT.

# imports
from x1 import ent
import math, random

# , room_Database, engine
# rooms = ['cabins', 'kitchen', 'pool', 'fitness center', 'casino', 'smoking area', 'shopping center', 'the bridge', 'start']
rooms = ['C', 'k', 'p', 'f', 'c', 's', 'S', 'B', '⌂']
rooms_obj = {0: "C",
			 1: "k",
			 2: "p",
			 3: "f",
			 4: "c",
			 5: "s",
			 6: "S",
			 7: "B",
			 8: "⌂"}
xdist = 0
ydist = 0
layout = [['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'],
		  ['-', '-', '-', '-', '-']]
layout[2][2] = 6
layout[4][2] = 7


# classes:
class Player:
	def __init__(self, health, experience, inventory, strength, dexterity, resistances, immunities, effects):
		self.hp = health
		self.exp = experience
		self.str = strength
		self.dex = dexterity
		self.inv = inventory
		self.res = resistances
		self.imm = immunities
		self.eff = effects
		self.inv = []
		self.res = []
		self.imm = []
		self.eff = []

	def gain_item(self, item):
		self.inv.append(item)

	def gain_res(self, resist):
		self.inv.append(resist)

	def gain_imm(self, immune):
		self.inv.append(immune)

	def gain_effect(self, effect):
		self.inv.append(effect)


# usage: Player = Player(health, experience, inventory, strength, dexterity, intelligence, wisdom, charisma, resistances, immunities, effects)

class Zombie:
	def __init__(self, health, attack, effects, loot):
		self.hp = health
		self.atk = attack
		self.eff = effects
		self.loot = loot
		self.loot = []

	def set_loot(self, item):
		self.loot.append(item)

    
#------------------------------------------------------------------------------------------------------------------------
		
class Item:
    def __init__(self, name, description, quantity: int=1) -> None:
        self.name = name
        self.quantity = quantity
        self.description=description
    def get_desc(self):
        return self.description
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

    def __init__(self, damage, description):
        self.damage= (-1 * abs(damage))
        self.description= description
    
    def use_item(self):
        return self.damage


class Range_Weapon(Item):
    damage=0
    max_range = 0
    current_range=0

    def __init__(self, damage, range, description):
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
    
    def __init__(self, damage, bludgeoning, description):
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
        return self.defenseclass Item:
    def __init__(self, name, description, quantity: int=1) -> None:
        self.name = name
        self.quantity = quantity
        self.description=description
    def get_desc(self):
        return self.description
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

    def __init__(self, damage, description):
        self.damage= (-1 * abs(damage))
        self.description= description
    
    def use_item(self):
        return self.damage


class Range_Weapon(Item):
    damage=0
    max_range = 0
    current_range=0

    def __init__(self, damage, range, description):
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
    
    def __init__(self, damage, bludgeoning, description):
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
    
#------------------------------------------------------------------------------------------------------------------------

class Room:
	def __init__(self, modifiers, effects, loot, zombies, resources):
		self.mod = modifiers
		self.eff = effects
		self.loot = loot
		self.zom = zombies
		self.reso = resources


class ship:
	def __init__(self, xdistance, ydistance, map, flavortext):
		self.xdist = xdistance
		self.ydist = ydistance
		self.map = map
		self.flav = flavortext
		self.map = []
		self.flav = []


# functions:
def display_current_map():
	global xdist
	global ydist
	print(layout[ydist][xdist])


def connect(x, y, loop):
	xstart = x
	ystart = y
	while loop >= 1:
		try:
			place = random.randint(1, 4)
			if place == 1:
				y -= 1
				if layout[x][y] == "-":
					layout[x][y] = "C"
			if place == 2:
				x -= 1
				if layout[x][y] == "-":
					layout[x][y] = "C"
			if place == 3:
				x += 1
				if layout[x][y] == "-":
					layout[x][y] = "C"
			else:
				y += 1
				if layout[x][y] == "-":
					layout[x][y] = "C"
			loop -= 1
		except:
			x = xstart
			y = ystart
#useless, traps itself half the time, doesnt even recurse


def map_generate():
	xstart = random.randint(0, 4)
	ystart = random.randint(0, 1)
	layout[ystart][xstart] = '⌂'

	#for i in range(len(layout)): #useless
		#for j in range(len(layout[i])):
			#if layout[i][j] == '⌂':
				#xstart = i
				#ystart = j
	#connect(xstart, ystart, 100)


# def store_user_input():

# def output_info():

# def combat():


# variables
for i in range(5):
	(y, x) = random.randint(0, len(layout) - 1), random.randint(0, len(layout) - 1)
	while (y, x) == (2, 2) or (4, 2):
		(y, x) = random.randint(0, len(layout) - 1), random.randint(0, len(layout) - 1)
	layout[y][x] = rooms.pop(1)

for i in range(len(layout)):
	for j in range(len(layout[i])):
		if layout[i][j] == '-':
			#place = random.randint(0, 1) #what is this for?
			#if place == 1:
				#pass
			layout[i][j] = 'C'


def human_readable_map_line(the_map_line):
	iterator = 0
	for cellvalue in the_map_line:
		# repr = representation
		repr = rooms_obj.get(cellvalue)
		if repr is not None:
			the_map_line[iterator] = repr
		iterator += 1
	return the_map_line


while 1:
	map_generate()
	display_current_map()
	for i in range(len(layout)):
		print(human_readable_map_line(layout[i]))
	ydist = int(input('y'))
	xdist = int(input('x'))
