import time


class Pokemon:
    # construindo os objetos pokemon
    def __init__(self, name, types, attack, defense, move1, move2):
        self.name = name
        self.types = types
        self.attack = attack
        self.defense = defense
        self.hp = self.defense * 10
        self.move1 = move1
        self.move2 = move2

    def fight(self, pokemon2):
        # imprimindo informações da batalha
        print(f'A wild {pokemon2.name} appear')
        time.sleep(.05)
        print(f'Go {self.name}')
        time.sleep(1)
        print()
        print('---- POKEMON BATTLE ----')
        print(f'Pokemon {self.name}')
        print(f'HP {self.hp}')
        print()
        print('VS')
        print()
        print(f'Pokemon {pokemon2.name}')
        print(f'HP {pokemon2.hp}')
        print()

        version = ['Fire', 'Water', 'Grass']
        for i, k in enumerate(version):
            if self.types == k:
                # São do mesmo tipo
                if pokemon2.types == k:
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts not very effective...'

                # pokemon2 é forte
                if pokemon2.types == version[(i + 1) % 3]:
                    pokemon2.attack += 5
                    pokemon2.defense += 5
                    self.attack -= 2
                    self.defense -= 2
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts super effective!'

                # pokemon2 é fraco
                if pokemon2.types == version[(i + 2) % 3]:
                    self.attack += 5
                    self.defense += 5
                    pokemon2.attack -= 2
                    pokemon2.defense -= 2
                    string_1_attack = '\nIts super effective!'
                    string_2_attack = '\nIts not very effective...'
        # loop da batalha
        while self.hp > 0 and pokemon2.hp > 0:
            atk = int(input(f'Pick a move 1 {self.move1} / 2 {self.move2}: '))
            if atk < 1 or atk > 2:
                return 'Try again'
            elif atk == 1:
                print(f'{self.name} used {self.move1}')
                time.sleep(1)
                pokemon2.hp -= self.attack
                print(string_1_attack)
            elif atk == 2:
                print(f'{self.name} used {self.move2}')
                time.sleep(1)
                pokemon2.defense -= 2
                print(f'{pokemon2} loses defense')

            time.sleep(1)
            print(f"\n{self.name}\t\tHLTH\t{self.hp}")
            print(f"{pokemon2.name}\t\tHLTH\t{pokemon2.hp}\n")
            time.sleep(.5)

            if pokemon2.hp <= 0:
                print(f'{pokemon2.name} fainted...')
                break
            else:
                print(f'{pokemon2.name} used {pokemon2.move1}')
                self.hp -= pokemon2.attack
                print(string_2_attack)

            time.sleep(1)
            print(f"\n{self.name}\t\tHLTH\t{self.hp}")
            print(f"{pokemon2.name}\t\tHLTH\t{pokemon2.hp}\n")
            time.sleep(.5)

            if self.hp <= 0:
                print(f'{self.name} is fainted...')
                break

    def heal(self):
        print(f'{self.name} drink a potion and healed 25 HP')
        self.hp += 25


if __name__ == '__main__':

    charmander = Pokemon('Charmander', 'Fire', 8, 4, 'scratch', 'growl')
    squirtle = Pokemon('Squirtle', 'Water', 7, 5, 'Water Pump', 'growl')

    squirtle.fight(charmander)
