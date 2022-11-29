class Character:

    def __init__(self, name, player_class, race, level):
        self.name = name
        self.player_class = player_class
        self.race = race
        self.level = level

    def __repr__(self):
        return f'{self.name} is a level {self.level}, {self.race}, {self.player_class}.'


character1 = Character('Nordak', 'Paladin', 'Human', 20)
print(character1)


class Attribute:
    def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    def __repr__(self):
        return f'Attributes are {self.strength}, {self.dexterity}, {self.constitution}, {self.wisdom}, {self.charisma}'
