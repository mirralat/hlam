from base import *


class Dragonite(Pokemon):
    def __init__(self, name, hp, defense,  special_defense):
        super().__init__(hp,  defense,  special_defense)
        self.name = name


class Mismagius(Pokemon):
    def __init__(self, name, hp, defense, special_defense):
        super().__init__(hp, defense, special_defense)
        self.name = name
