from character import Character
from spell import Fireball, IceLance, LightningBolt


def main():
    mage = Character(
        strength=8,
        dexterity=12,
        constitution=10,
        wisdom=16,
        intelligence=18,
        charisma=14,
        character_class="mage"
    )

    mage.add_spell(Fireball())
    mage.add_spell(IceLance())
    mage.add_spell(LightningBolt())

    print("Персонаж создан")
    print("Класс:", mage.character_class)
    print("Здоровье:", mage.health)
    print("Урон:", mage.damage)
    print("Защита:", mage.defense)
    print("Мана:", mage.mana)

    damage = mage.cast_spell(0)

    print("Маг использовал заклинание")
    print("Урон заклинания:", damage)
    print("Осталось маны:", mage.mana)


if __name__ == "__main__":
    main()
