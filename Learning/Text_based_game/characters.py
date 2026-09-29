import random
from random import randint
from names import list_names
import os
import time
os.system('cls')


def print_linebreak(self):
    print()
    print('-'*50)
    print()


class Actor:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health

    def __repr__(self):
        return f'<Actor: {self.name}, Level:{self.level}'

    # This is what determines how much damage you do.
    def get_attack_power(self):
        return randint(1, 20) * self.level

    # Checks to see if you are alive.
    def is_alive(self):
        return self.health > 0

    def health(self):
        return self.health * self.level

    def attacks(self, other):
        raise NotImplementedError()

    # This is for player XP


class Player(Actor):
    def __init__(self, name, level, health):
        super().__init__(name, level, health)
        self.xp = 0  # Sets the players xp to 0 at the beginning of the game.
        # This is the amount of XP required to get to the next level.
        self.xp_to_next_level = 100

    # This is how you gain XP
    def gain_xp(self, amount):
        self.xp += amount
        print(f'{self.name} gained {amount} XP! Total XP: {self.xp}')
        while self.xp >= self.xp_to_next_level:
            self.xp -= self.xp_to_next_level
            self.level_up()
            # increases the amount of xp needed for the next level
            self.xp_to_next_level = int(self.xp_to_next_level * 1.5)

    # Option to heal yourself just gives you 10 hp.
    def heal(self):
        self.health = self.health + 10

    # Attacking
    def attacks(self, enemy):
        power = self.get_attack_power()

        print('{} attacks the {}'.format(self.name, enemy.kind))
        time.sleep(1.5)
        print('{} did {} attack damage'.format(self.name, power))
        time.sleep(1.5)
        enemy.health -= power

    def level_up(self):
        self.level += 1

        print('{} leveled up! You are now level {}'.format(self.name, self.level))

    # This is the stats for the player.
    def stats(self):
        print('{} has {} hp, is level {}, and has {}/{} XP'.format(self.name,
              self.health, self.level, self.xp, self.xp_to_next_level) + '\n')
# Enemies Class


class Enemy(Actor):
    def __init__(self, kind, level, health, name=None):
        if name is None:
            name = random.choice(list_names)
        super().__init__(name, level, health)
        self.kind = kind

    # This is for enemy attacks.
    def attacks(self, player):
        print('\n{} the {} attacks {}'.format(
            self.name, self.kind, player.name))
        time.sleep(1.5)

        e_power = self.get_attack_power()

        print('{} attacks you with {} attack damage'.format(self.name, e_power))
        time.sleep(1.5)

        player.health -= e_power

    # These are the stats for the enemy.
    def stats(self):
        print(f'{self.name} the {self.kind} has {self.health} hp, and is level {self.level}'.format(
            self.name, self.kind, self.health, self.level))

# Ogre enemy


class Ogre(Enemy):
    def __init__(self, health, level, size, name):
        super().__init__('Ogre', level, health, name)
        self.size = size

    def get_attack_power(self):
        return randint(1, 50) * (self.size * self.level)

# Goblin Enemy


class Goblin(Enemy):
    def __init__(self, level, health, name, weapon):
        super().__init__('Goblin', level, health, name)
        self.weapon = weapon

    def get_attack_power(self):
        return randint(1, 25) * (self.weapon * self.level)
# Imp Enemy


class Imp(Enemy):
    def __init__(self, level, health, name):
        super().__init__('Imp', level, health, name)

    def get_attack_power(self):
        return super().get_attack_power() / 4


 # The players name, start level and start health.
if __name__ == '__main__':
    player = Player(name='Luffy', level=1, health=100)
