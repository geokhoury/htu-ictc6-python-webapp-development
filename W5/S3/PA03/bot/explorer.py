from game_character import GameCharacter

class Explorer(GameCharacter):

    def __init__(self, name, health, attack_max, magic):

        super().__init__(name, health, attack_max, magic)

        print(f"Commander '{self.name}' at your service.")