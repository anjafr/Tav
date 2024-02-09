import random

class Race:
    name: str = None
    subraces: str = None

    def __init__(self, name, sr_list):
        self.name = name
        self.subrace = random.choice(sr_list)

    def __str__(self):
        return f"{self.subrace}"


dragonborn = Race("Dragonborn", ["Black Dragonborn", "Blue Dragonborn", "Brass Dragonborn", "Bronze Dragonborn", "Copper Dragonborn", "Gold Dragonborn", "Green Dragonborn", "Red Dragonborn", "Silver Dragonborn", "White Dragonborn"])
drow = Race("Drow", ["Lolth-Sworn Drow", "Seldarine Drow"])
dwarf = Race("Dwarf", ["Gold Dwarf", "Shield Dwarf", "Duergar"])
elf = Race("Elf", ["High Elf", "Wood Elf"])
githyanki = Race("Githyanki", ["Githyanki"])
gnome = Race("Gnome", ["Deep Gnome", "Forest Gnome", "Rock Gnome"])
half_elf = Race("Half-Elf", ["High Half-Elf", "Wood Half-Elf", "Drow Half-Elf"])
half_orc = Race("Half-Orc", ["Half-Orc"])
halfling = Race("Halfling", ["Lightfoot Halfling", "Strongheart Halfling"])
human = Race("Human", ["Human"])
tiefling = Race("Tiefling", ["Asmodeus Tiefling", "Mephistopheles Tiefling", "Zariel Tiefling"])


RACELIST = [
    dragonborn,
    drow,
    dwarf,
    githyanki,
    gnome,
    half_elf,
    half_orc,
    halfling,
    human,
    tiefling
    ]
