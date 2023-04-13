# THE ACCOMPANYING PROGRAM IS PROVIDED UNDER THE TERMS OF THIS ECLIPSE
# PUBLIC LICENSE ("AGREEMENT"). ANY USE, REPRODUCTION OR DISTRIBUTION
# OF THE PROGRAM CONSTITUTES RECIPIENT'S ACCEPTANCE OF THIS AGGREMENT.

# imports
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


class Item:
	def __init__(self, damage, effects):
		self.dmg = damage
		self.eff = effects


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
