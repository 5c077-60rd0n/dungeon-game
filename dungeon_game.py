class Character:
    def __init__(self, name, player_class, race, level):
        self.name = name
        self.player_class = player_class
        self.race = race
        self.level = level

    def __repr__(self):
        return f'{self.name} is a level {self.level}, {self.race}, {self.player_class}.'




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


character1 = Character('Nordak', 'Paladin', 'Human', 20)
print(character1)

attribute1 = Attribute(15, 10, 12, 14, 8, 10)
print(attribute1)
attribute1.increase_charisma()
print(attribute1)