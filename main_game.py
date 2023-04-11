# THE ACCOMPANYING PROGRAM IS PROVIDED UNDER THE TERMS OF THIS ECLIPSE
# PUBLIC LICENSE ("AGREEMENT"). ANY USE, REPRODUCTION OR DISTRIBUTION
# OF THE PROGRAM CONSTITUTES RECIPIENT'S ACCEPTANCE OF THIS AGGREMENT.

#imports
import math, random
#, room_Database, engine
#rooms = ['cabins', 'kitchen', 'pool', 'fitness center', 'casino', 'smoking area', 'shopping center', 'the bridge']
rooms = ['🛏', '🍳', '🏊', '🏋', '⛁', '🚬', '🛍', '🚢']
xdist = 0
ydist = 0
layout = [['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-']]

#classes:
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
		

#usage: Player = Player(health, experience, inventory, strength, dexterity, intelligence, wisdom, charisma, resistances, immunities, effects)

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

#functions:
def display_current_map():
	global xdist
	global ydist
	print(layout[ydist][xdist])

def connect(x,y,loop):
	xstart = x
	ystart = y
	while loop >=1:	
		try:
			place = random.randint(1,4)
			if place == 1:
				y-=1
				if layout[x][y] == "-":
					layout[x][y] = "C"
			if place == 2:
				x-=1
				if layout[x][y] == "-":
					layout[x][y] = "C"
			if place == 3:
				x+=1
				if layout[x][y] == "-":
					layout[x][y] = "C"
					
			else:
				y+=1
				if layout[x][y] == "-":
					layout[x][y] = "C"
			loop-=1
		except:
			print("restart")
			x = xstart
			y = ystart


def map_generate():
	xstart = 0
	ystart = 0
	layout[random.randint(1,3)][random.randint(1,3)] = '⌂'
	
	for i in range(len(layout)):
		for j in range(len(layout[i])):
			if layout[i][j] == '⌂':
				xstart = i
				ystart = j
	connect(xstart,ystart,10)
	
	


#def store_user_input():

#def output_info():

#def combat():



#variables
layout[4][2] = rooms.pop(-1)
layout[2][2] = rooms.pop(-1)

for i in range(5):
	(y, x) = (random.randint(0,len(layout)-1), random.randint(0,len(layout)-1))
	if (y, x) != (2, 2) and (4, 2):
		layout[y][x] = rooms.pop(1)

for i in range(len(layout)):
    for j in range(len(layout[i])):
        if layout[i][j] == '-':
            layout[i][j] = rooms[0]
        

while 1:
	display_current_map()
	for i in range(len(layout)):
	    print(layout[i])
	ydist = int(input('y'))
	xdist = int(input('x'))
