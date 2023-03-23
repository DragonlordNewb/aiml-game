# THE ACCOMPANYING PROGRAM IS PROVIDED UNDER THE TERMS OF THIS ECLIPSE
# PUBLIC LICENSE ("AGREEMENT"). ANY USE, REPRODUCTION OR DISTRIBUTION
# OF THE PROGRAM CONSTITUTES RECIPIENT'S ACCEPTANCE OF THIS AGGREMENT.

#imports
import engine, math, random, room_Database


#classes:
class Player:
	def __init__(char, health, experience, inventory, strength, dexterity, resistances, immunities, effects):
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

	def gain_item(char, item):
		self.inv.append(item)
	def gain_res(char, resist):
		self.inv.append(resist)
	def gain_imm(char, immune):
		self.inv.append(immune)
	def gain_effect(char, effect):
		self.inv.append(effect)
		

#usage: Player = Player(health, experience, inventory, strength, dexterity, resistances, immunities, effects)

class Zombie:
	def __init__(zombie, health, attack, effects, loot):
		self.hp = health
		self.atk = attack
		self.eff = effects
		self.loot = loot
		self.loot = []


	def set_loot(zombie, item):
		self.loot.append(item)

class Item:
    def __init__(item, damage, effects):
        self.dmg = damage
        self.eff = effects


class Room:
	def __init__(room, modifiers, effects, loot, zombies, resources):
		self.mod = modifiers
		self.eff = effects
		self.loot = loot
		self.zom = zombies
		self.reso = resources

class Map:
    def __init__(map, xdistance, ydistance, layout):
        self.xdist = xdistance
        self.ydist = ydistance
        self.layout = layout
        self.layout = []
#functions:
def display_current_map():


#def store_user_input():

#def output_info():

#def combat():


#variables:
