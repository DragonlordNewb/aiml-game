import random

class Npc:
    def __init__(self, name):
        self.name = name
  

class Random(Npc):
    actions = []

    def __init__(self, actions):
        self.actions = actions
    
    def take_action(self, actions):
        action = actions[random.randint(0,len(actions))-1]

class SearchTree(Npc):
    
