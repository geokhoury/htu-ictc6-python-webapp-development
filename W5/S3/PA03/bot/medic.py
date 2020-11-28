from game_character import GameCharacter

import random

class Medic(GameCharacter):

    def __init__(self, name, health, heal, magic):

        super().__init__(name, health, heal, magic)

        print(f"Your medic {self.name}, to the rescue!")

    def heal(self, character):
        heal_value = (random.randrange(self.strength - 10 , self.strength + 10)/10)
        print(f"> {self.name} is healing {character.name}. {(heal_value)}")

        if character.get_health() + heal_value > character.max_health:
            character.set_health(100)
        else:
            character.set_health(character.get_health() + heal_value)

        return heal_value
    
    def attack(self, character):
        self.heal(character)
