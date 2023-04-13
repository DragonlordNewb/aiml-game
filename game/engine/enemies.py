class Enemy:
    def __init__(self, type, name, description, damage, max_health, current_health, taken_damage, armor, dead):
        self.name = name
        self.type = type
        self.description = description
        self.damage = damage
        self.max_health = max_health
        self.current_health = current_health
        self.taken_damage = taken_damage
        self.dead = dead
        #defense should always be a decimal value
        self.armor = armor
    
    #damage is going to be a positive number
    #blugeoning should be a decimal, never more than 1
    #armor and bludgeoning are both percentage values. Armor reduces the damage the entity takes, bludgeoning reduces said damage decrease.
    #If the bludgeoning value is greater than the armor, then 100% of damage is taken, no more
    #When bludgeoning and armor are in play, the math works as the following:
    #100% (the damage multiplier, represented by the int 1) is subtracted by the armor percentage, and then the bludgeoning percentage is
    #added back to the multiplier. Example: Armor: 0.4 (40%). Bludgeoning: 0.2 (20%). 100%-40%=60%. 60%+20%=80%. 80% of damage is taken
    def take_damage(self, damage, bludgeon=0.0):
        if (damage < 0): 
            if bludgeon < self.armor:
                self.current_health -= int((1-self.armor + bludgeon) * damage)
            elif bludgeon >= self.armor:
                self.current_health -= damage
        else:
            self.current_health -= damage
    
    def give_description(self, description):
        print(description)

    def give_info(self, type, name, description, damage, max_health, current_health):
        print(f"Name:        {name.title()}")
        print(f"Type:        {type.title()}")
        print(f"Description: {description}")
        print(f"Damage:      {int(damage)}")
        print(f"Max health:  {int(max_health)}")
        print(f"Health:      {int(current_health)}")
