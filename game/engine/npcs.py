import random

class Npc:
    def __init__(self, type, name, description, damage, defense, health, taken_damage, dead):
        self.name = name
        self.type = type
        self.description = description
        self.damage = damage
        self.defense = defense
        self.health = health
        self.taken_damage = taken_damage
        self.dead = dead
        dead = False
    
    def take_damage(self, health, taken_damage, dead):
        health = health-taken_damage
        if health == 0:
            dead = True

  

class Random(Npc):
    actions = []

    def __init__(self, actions):
        self.actions = actions
    
    def take_action(self, actions):
        action = actions[random.randint(0,len(actions))-1]

class SearchTree(Npc):
