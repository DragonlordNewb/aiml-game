import random
class Enemy:
    def __init__(self, type, name, description, damage, max_health, current_health, taken_damage, range, miss_chance,armor=0.0):
        self.name = name
        self.type = type
        self.description = description
        self.damage = damage
        self.max_health = max_health
        self.current_health = current_health
        self.taken_damage = taken_damage
        self.range=range
        #miss chance is a whole number between 0-100. For example, a 33% miss chance will be 33
        self.miss_chance=miss_chance
        #defense should always be a decimal value, less than
        self.armor = armor

    
    #damage is going to be a positive number
    #blugeoning should be a decimal, never more than 1
    #armor and bludgeoning are both percentage values. Armor reduces the damage the entity takes, bludgeoning reduces said damage decrease.
    #If the bludgeoning value is greater than the armor, then 100% of damage is taken, no more
    #When bludgeoning and armor are in play, the math works as the following:
    #100% (the damage multiplier, represented by the int 1) is subtracted by the armor percentage, and then the bludgeoning percentage is
    #added back to the multiplier. Example: Armor: 0.4 (40%). Bludgeoning: 0.2 (20%). 100%-40%=60%. 60%+20%=80%. 80% of damage is taken
    def take_damage(self, damage, bludgeon=0.0):
        ran_num=random.randint(1,100)
        if (ran_num>=self.miss_chance):
            if (bludgeon > 0.0): 
                if bludgeon < self.armor:
                    self.current_health -= abs((1-self.armor + bludgeon) * damage)
                elif bludgeon >= self.armor:
                    self.current_health -= abs(damage)
            else:
                self.current_health -= abs(damage * (1-self.armor))
        else:
            print("missed")
    def get_range(self):
        return self.range

    def set_range(self,changed_range):
        self.range -= changed_range

    def give_description(self, description):
        print(description)

    def give_info(self):
        print(f"Name:        {self.name.title()}")
        print(f"Type:        {self.type.title()}")
        print(f"Description: {self.description}")
        print(f"Damage:      {int(self.damage)}")
        print(f"Max health:  {int(self.max_health)}")
        print(f"Current Health:   {float(self.current_health)}")
