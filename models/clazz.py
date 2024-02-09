import random

class Clazz:
    name: str = None
    level: int = 1
    subclass_choice_level: int = None
    subclasses: [str] = []
    subclass: str = None

    def __init__(self, name, sc_level, sc_list):
        self.name = name
        self.subclass_choice_level = sc_level
        self.subclasses = sc_list
        if self.subclass_choice_level == 1: self.choose_subclass()

    def __str__(self):
        if self.subclass:
            return f"Level {self.level} {self.name} - {self.subclass}"
        return f"Level {self.level} {self.name}"

    def choose_subclass(self):
        self.subclass = random.choice(self.subclasses)

    def level_up(self):
        self.level += 1
        if self.level == self.subclass_choice_level: self.choose_subclass()

    def to_json(self):
        return {self.name: f"{self.level} - {self.subclass}"}


barbarian = Clazz("Barbarian", 3, ["Berserker", "Wild Heart", "Wild Magic"])
bard = Clazz("Bard", 3, ["College of Lore", "College of Valour", "College of Swords"])
cleric = Clazz("Cleric", 1, ["Life Domain", "Light Domain", "Trickery Domain", "Knowledge Domain", "Nature Domain", "Tempest Domain", "War Domain"])
druid = Clazz("Druid", 2, ["Circle of the Moon", "Circle of the Land", "Circle of the Spores"])
fighter = Clazz("Fighter", 3, ["Battle Master", "Eldritch Knight", "Champion"])
monk = Clazz("Monk", 3, ["Way of the Open Hand", "Way of Shadow", "Way of the Four Elements"])
paladin = Clazz("Paladin", 1, ["Oath of Devotion", "Oath of the Ancients", "Oath of Vengeance"])
ranger = Clazz("Ranger", 3, ["Beast Master", "Hunter", "Gloom Stalker"])
rogue = Clazz("Rogue", 3, ["Thief", "Arcane Trickster", "Assassin"])
sorcerer = Clazz("Sorcerer", 1, ["Draconic Bloodline", "Wild Magic", "Storm Sorcery"])
warlock = Clazz("Warlock", 1, ["The Fiend", "The Great Old One", "Archfey"])
wizard = Clazz("Wizard", 2, ["Abjuration School", "Conjuration School", "Divination School", "Enchantment School", "Evocation School", "Necromancy School", "Illusion School", "Transmutation School"])

CLASSLIST = [
    barbarian,
    bard,
    cleric,
    druid,
    fighter,
    monk,
    paladin,
    ranger,
    rogue,
    sorcerer,
    warlock,
    wizard]
