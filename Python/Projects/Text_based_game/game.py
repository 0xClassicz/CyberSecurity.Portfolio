from characters import Player, Enemy, Ogre, Goblin, Imp
import random
import os
import time
os.system('cls')


class Game:
    def __init__(self, player, enemies):
        self.player = player
        self.enemies = enemies
        self.player.has_healed = False

    def main(self):
        self.print_intro()
        return self.play()

    def print_intro(self):
        print('''
                Welcome to Level Up!
                Ready to fight your way to victory?
                [Press Enter to Continue]
                ''')
        input()
        os.system('cls')

   # This is the break line that you see with the lines.

    def print_linebreak(self):
        print()
        print('-'*50)
        print()

    def play(self):
        # pick enemy first and then only chooses another enemy if you run away or after deafting the old one
        next_enemy = random.choice(self.enemies)

        while True:
            cmd = input(
                f'You see a {next_enemy.kind}. [r]un, [a]ttack, [h]eal, [p]ass, [x]restart? ')
            os.system('cls')

            if cmd.lower() == 'r':
                print(f'{self.player.name} runs away! ')

                if len(self.enemies) > 1:
                    available_enemies = [
                        enemy for enemy in self.enemies
                        if enemy != next_enemy
                    ]
                    next_enemy = random.choice(available_enemies)
                else:
                    print('There are no other enemies to fight! ')

            elif cmd.lower() == 'h':
                if not self.player.has_healed:
                    print(f"{self.player.name} heals themselve's!")
                    self.player.heal()
                    self.player.has_healed = True  # See line 67
                else:
                    print(f"{self.player.name} has already healed!")

            elif cmd.lower() == "a":
                self.player.attacks(next_enemy)

                if not next_enemy.is_alive():
                    # Enemy died
                    self.enemies.remove(next_enemy)
                    # Only after you kill an enemy will you be able to heal again.
                    self.player.has_healed = False

                    print(f'{self.player.name} has slayed the {next_enemy.kind}!')

                    xp_earned = next_enemy.level * 50
                    self.player.gain_xp(xp_earned)

                    if not self.enemies:
                        self.print_linebreak()
                        print('\n You have won! Congratulations.')
                        time.sleep(3)

                        self.print_linebreak()

                        for i in range(3, 0, -1):
                            print(i)
                            time.sleep(1)

                        break

                    next_enemy = random.choice(self.enemies)

                else:
                    next_enemy.attacks(self.player)

            elif cmd.lower() == 'p':
                print('You are still thinking about your next move...')
                if random.randint(1, 11) < 5:
                    next_enemy.attacks(self.player)

            elif cmd.lower() == 'x':
                print('Restarting game.')
                return True

            else:
                print('Please choose a valid option')

            if not self.player.is_alive():
                self.print_linebreak()
                print('OH NO! You lose...')
                self.print_linebreak()
                time.sleep(3)

                for i in range(3, 0, -1):
                    print(i)
                    time.sleep(1)
                break

            # This prints out the player stats after the end of a successful turn.
            print('\n' * 5)
            self.print_linebreak()
            self.player.stats()
            self.print_linebreak()

            # This prints out the enemy stats after the end of a successful turn.
            self.print_linebreak
            for e in self.enemies:
                e.stats()
            self.print_linebreak()

        while True:
            self.print_linebreak()
            restart = input('Would you like to play again? [y/n] ').lower()
            if restart in ('y', 'n'):
                return restart == 'y'
            print('Please enter y or n.')


def create_game():
    player = Player('Luffy', 1, health=50)
    enemies = [
        Ogre(name=None, level=1, health=40, size=1),
        Goblin(name=None, level=1, health=20, weapon=1),
        Imp(name=None, level=1, health=10),
    ]
    return Game(player, enemies)


if __name__ == '__main__':  # this code only runs if this file is being run directly so game.py
    restart = True
    while restart:
        restart = create_game().main()
