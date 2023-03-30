# THE ACCOMPANYING PROGRAM IS PROVIDED UNDER THE TERMS OF THIS ECLIPSE
# PUBLIC LICENSE ("AGREEMENT"). ANY USE, REPRODUCTION OR DISTRIBUTION
# OF THE PROGRAM CONSTITUTES RECIPIENT'S ACCEPTANCE OF THIS AGGREMENT.

#imports
import math, random, room_Database, engine
rooms = ['cabins', 'kitchen', 'pool', 'fitness center', 'casino', 'smoking area', 'shopping center', 'the bridge']
xdist = 0
ydist = 0
layout = [['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-']]
layout[3][3] = 'shopping center'
layout[5][3] = 'the bridge'

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

class Map:
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
	globa ydist
	print(map[ydist][xdist]


#def store_user_input():

#def output_info():

#def combat():


#variables

while 1:
	display_current_map():
	ydist = int(input('y'))
	xdist = int(input('x'))
