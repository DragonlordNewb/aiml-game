class Enemy:
    def __init__(self, type, name, description, damage, max_health, current_health, taken_damage, dead):
        self.name = name
        self.type = type
        self.description = description
        self.damage = damage
        self.max_health = max_health
        self.current_health = current_health
        self.taken_damage = taken_damage
        self.dead = dead
    
    def take_damage(self, health, taken_damage, dead):
        health = health-taken_damage
        if health <= 0:
            dead = True
        taken_damage = 0
    
    def give_description(self, description):
        print(description)

    def give_info(self, type, name, description, damage, max_health, current_health):
        print(f"Name:        {name.title()}")
        print(f"Type:        {type.title()}")
        print(f"Description: {description}")
        print(f"Damage:      {int(damage)}")
        print(f"Max health:  {int(max_health)}")
        print(f"Health:      {int(current_health)}")
