from game_character import GameCharacter

class Warrior(GameCharacter):

    def __init__(self, name, health, attack_max, magic):

        super().__init__(name, health, attack_max, magic)

        print(f"{self.name} is ready to fight! \n")
