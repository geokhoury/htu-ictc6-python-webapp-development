import random
import math

class GameCharacter:

    def __init__(self, name, health, strength, magic):
        
        # Instance attributes
        self.name = name.title()
        self.health = health
        self.max_health = health
        self.strength = strength
        self.magic = magic

    def __str__(self):
        return f"\n** Stats for {self.name} \n\n\t - Health: {int(self.health)} \n\t - Strength: {int(self.strength)} \n\t - Magic: {int(self.magic)} \n"

    # Getters and setters for the attributes
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_health(self, health):
        if health <=0:
            self.health = 0
        elif health > self.max_health:
            self.health = self.max_health
        else:
            self.health = health

    def get_health(self):
        return self.health
    
    def set_strength(self, strength):
        if strength <=0:
            self.strength = 0
        else:
            self.strength = strength

    def get_strength(self):
        return self.strength

    def set_magic(self, magic):
        if magic <=0:
            self.magic = 0
        else:
            self.magic = magic

    def get_magic(self):
        return self.magic

    # Instance Methods
    def attack(self, opponent):
        attack_strength = int((self.health * 0.6 + self.strength * 0.4 + self.magic * 0.2)/12)

        print(f"> {self.name} is attacking {opponent.name}. {(attack_strength)}")
    
        opponent.set_health(opponent.get_health() - (attack_strength))

    def cast_spell_on(self, opponent):
        spells = [(0.2, 0.4, 0.6), (0.4, 0.2, 0.6), (0.6, 0.4, 0.2)]

        spell = random.choice(spells)

        print(f"> {self.name} is trying to cast a spell on {opponent.name}.")

        magic = random.random()

        if magic > 0.7:
            print(f"> Abracadabra... casting the spell.")

            opponent.health -= opponent.health * spell[0]
            opponent.strength -= opponent.strength * spell[1]
            opponent.magic -= opponent.magic * spell[2]

        else:
            print(f"> Casting the spell failed.")
            self.strength -= 4
            self.magic -= 2