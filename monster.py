from unit import Unit


class Monster(Unit):
    def calculate_max_health(self):
        return int(self.constitution * 8 + self.strength / 3)

    def calculate_damage(self):
        return int(self.strength * 2 + self.constitution / 5)

    def calculate_defense(self):
        return int(self.constitution * 1.2 + self.strength / 5)
