from unit import Unit


class Character(Unit):
    def calculate_max_health(self):
        return int(self.constitution * 10 + self.strength / 2)

    def calculate_damage(self):
        return int(self.strength * 1.5 + self.dexterity / 4)

    def calculate_defense(self):
        return int(self.constitution * 1.5 + self.dexterity / 3)
