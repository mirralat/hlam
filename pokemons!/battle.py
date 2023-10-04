import time

from pokemons import *
import random


class Battle:
    def attack(self, attacker, pokemon):
        PhysicalAttack.attack(pokemon)
        print(f'{attacker.name} attacks {pokemon.name}! Pokemons hp {pokemon.hp}!')

    def special_attack(self, attacker, pokemon):
        SpecialAttack.attack(pokemon)
        print(f'{attacker.name} attacks by special attack {pokemon.name}!  Pokemons hp {pokemon.hp}!')

    def status(self, pokemon1, pokemon2):
        hp1 = Status.status(pokemon1)
        hp2 = Status.status(pokemon2)
        print(f'{pokemon1.name} is {hp1}, {pokemon2.name} is {hp2}')

    def upgrade(self, pokemon):
        Upgrade.upgrade(pokemon)
        print(f'{pokemon.name} has an upgrade!')


b = Battle()
battle_list = [b.attack, b.special_attack]
dragonite = Dragonite('Dragonite', 300, 30, 20)
mismagius = Mismagius('Mismagius', 250, 60, 50)

flag = 1
first_player_count = 0
second_player_count = 0

while True:
    if dragonite.hp <= 0 or mismagius.hp <= 0:
        break

    if first_player_count >= 20:
        b.upgrade(dragonite)
        first_player_count = 0
    if second_player_count >= 20:
        b.upgrade(mismagius)
        second_player_count = 0

    if flag == 1:
        attack = random.choice(battle_list)
        if attack == b.attack:
            b.attack(dragonite, mismagius)
            first_player_count += random.randint(1, 10)
            flag = 2

        if attack == b.special_attack:
            b.attack(dragonite, mismagius)
            first_player_count += random.randint(1, 10)
            flag = 2

    if flag == 2:
        attack = random.choice(battle_list)
        if attack == b.attack:
            b.attack(mismagius, dragonite)
            second_player_count += random.randint(1, 10)
            flag = 1
        if attack == b.special_attack:
            b.attack(mismagius, dragonite)
            second_player_count += random.randint(1, 10)
            flag = 1

    b.status(dragonite, mismagius)
    time.sleep(1)

if mismagius.hp <= 0:
    print('Dragonite won!')

if dragonite.hp <= 0:
    print('Misamagius won!')
