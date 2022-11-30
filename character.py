


class Attribute:
    def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    def __repr__(self):
        return f'Attributes are {self.strength}, {self.dexterity}, {self.constitution}, {self.intelligence}, {self.wisdom}, {self.charisma}'

    def increase_strength(self):
        self.strength += 1

    def decrease_strength(self):
        self.strength -= 1

    def increase_dexterity(self):
        self.dexterity += 1

    def decrease_dexterity(self):
        self.dexterity -= 1

    def increase_constitution(self):
        self.constitution += 1

    def decrease_constitution(self):
        self.constitution -= 1

    def increase_intelligence(self):
        self.intelligence += 1

    def decrease_intelligence(self):
        self.intelligence -= 1

    def increase_wisdom(self):
        self.wisdom += 1

    def decrease_wisdom(self):
        self.wisdom -= 1

    def increase_charisma(self):
        self.charisma += 1

    def decrease_charisma(self):
        self.charisma -= 1

class Character:
    def __init__(self, name, player_class, race, level, hit_points):
        self.name = name
        self.player_class = player_class
        self.race = race
        self.level = level
        self.hit_points = hit_points
        # OOP Composition character class HAS attributes
        self.char_attributes = Attribute(strength=9, dexterity=9,constitution=9, intelligence=9, wisdom=9, charisma=9)

    def __repr__(self):
        return f'{self.name} is a level {self.level}, {self.race}, {self.player_class}.'

    def announce(self):
        print(
            f'Hello there my name is {self.name}, and I am a level {self.level} {self.player_class}')

    def level_up(self):
        self.level += 1

    def adjust_hp(self, hp_amount):
        self.hit_points += hp_amount
        print(f'{self.name}\'s hit points are now {self.hit_points}')

class Paladin(Character):
    def __init__(self, name, race, level, hit_points, player_class='Paladin'):
        super().__init__(name, player_class, race, level, hit_points)

character1 = Character('Nordak', 'Paladin', 'Human', 20, 500)
print(character1)

print(character1.char_attributes)

paladin1 = Paladin(name="Jojo", race="High Elf", level=10, hit_points=200)
print(paladin1)