import random


class Pokemon:
    def __init__(self, hp, defense, special_defense):
        self.hp = hp
        self.defense = defense
        self.special_defense = special_defense


class PhysicalAttack(Pokemon):
    def __init__(self, damage, hp, defense,  special_defense):
        super().__init__(hp,  defense, special_defense)
        self.damage = damage

    def attack(self):
        if self.defense > 50:
            self.damage = random.randint(10, 30)
            self.hp -= self.damage
        else:
            self.damage = random.randint(40, 50)
            self.hp -= self.damage


class Status(Pokemon):
    def __init__(self, status, hp,  defense,  special_defense):
        super().__init__(hp,  defense,  special_defense)
        self.status = status

    def status(self):
        return self.hp


class SpecialAttack(Pokemon):
    def __init__(self, damage, hp, defense,  special_defense):
        super().__init__(hp,  defense,  special_defense)
        self.damage = damage

    def attack(self):
        if self.special_defense > 50:
            self.damage = random.randint(25, 30)
            self.hp -= self.damage
        else:
            self.damage = random.randint(70, 80)
            self.hp -= self.damage


class Upgrade(Pokemon):
    def __init__(self, hp, defense, special_defense):
        super().__init__(hp, defense, special_defense)

    def upgrade(self):
        self.hp += 100

