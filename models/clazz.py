import random

class BG3Class:
    name: str = None
    level: int = 0
    subclass_choice_level: int = 1
    subclasses: [str] = []
    subclass: str = None

    def choose_subclass(self):
        self.subclass = random.choice(self.subclasses)

    def level_up(self):
        self.level += 1
        if self.level == self.subclass_choice_level:
            self.choose_subclass()

    @property
    def __dict__(self):
        return {"name": self.name, "level": self.level, "subclass": self.subclass}


class Barbarian(BG3Class):
    name = "Barbarian"
    subclass_choice_level = 3
    subclasses = ["Berserker", "Wild Heart", "Wild Magic"]


class Bard(BG3Class):
    name = "Bard"
    subclass_choice_level = 3
    subclasses = ["College of Lore", "College of Valour", "College of Swords"]


class Cleric(BG3Class):
    name = "Cleric"
    subclasses = [
        "Life Domain",
        "Light Domain",
        "Trickery Domain",
        "Knowledge Domain",
        "Nature Domain",
        "Tempest Domain",
        "War Domain",
    ]


class Druid(BG3Class):
    name = "Druid"
    subclass_choice_level = 2
    subclasses = ["Circle of the Moon", "Circle of the Land", "Circle of the Spores"]


class Fighter(BG3Class):
    name = "Fighter"
    subclass_choice_level = 3
    subclasses = ["Battle Master", "Eldritch Knight", "Champion"]


class Monk(BG3Class):
    name = "Monk"
    subclass_choice_level = 3
    subclasses = ["Way of the Open Hand", "Way of Shadow", "Way of the Four Elements"]


class Paladin(BG3Class):
    name = "Paladin"
    subclasses = ["Oath of Devotion", "Oath of the Ancients", "Oath of Vengeance"]


class Ranger(BG3Class):
    name = "Ranger"
    subclass_choice_level = 3
    subclasses = ["Beast Master", "Hunter", "Gloom Stalker"]


class Rogue(BG3Class):
    name = "Rogue"
    subclass_choice_level = 3
    subclasses = ["Thief", "Arcane Trickster", "Assassin"]


class Sorcerer(BG3Class):
    name = "Sorcerer"
    subclasses = ["Draconic Bloodline", "Wild Magic", "Storm Sorcery"]


class Warlock(BG3Class):
    name = "Warlock"
    subclasses = ["The Fiend", "The Great Old One", "Archfey"]


class Wizard(BG3Class):
    name = "Wizard"
    subclass_choice_level = 2
    subclasses = [
        "Abjuration School",
        "Conjuration School",
        "Divination School",
        "Enchantment School",
        "Evocation School",
        "Necromancy School",
        "Illusion School",
        "Transmutation School",
    ]


CLASSLIST = [Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard]
