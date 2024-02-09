import json
import random
import os
from typing import Dict
from models.clazz import Clazz, CLASSLIST
from models.race import RACELIST

BACKGROUNDLIST = ["Acolyte",
                  "Charlatan",
                  "Criminal",
                  "Entertainer",
                  "Folk Hero",
                  "Guild Artisan",
                  "Noble",
                  "Outlander",
                  "Sage",
                  "Soldier",
                  "Urchin"
]

class Tav:
    name: str = None
    character_level: int = 1
    classes: Dict[str, Clazz] = {}
    race: str = None
    background: str = None
    history: Dict = {}
    id: int = None

    def __init__(self, name="Tav", level = 1, race = None, background = None):
        self.name = name
        self.character_level = level
        clazz = random.choice(CLASSLIST)
        self.classes.update({clazz.name: clazz})
        self.race = race if race else random.choice(RACELIST)
        self.background = background if background else random.choice(BACKGROUNDLIST)
        self.history.update({"Name": self.name})
        self.history.update({"Race": f"{self.race}"})
        self.history.update({"Background": self.background})
        self.history.update({self.character_level: clazz.to_json()})
        self.id = id(self)

    def __str__(self):
        return (f"{self.name}, a level {self.character_level} {self.race} {self.background}:\n"
                f'{os.linesep.join(f"{clazz}" for name, clazz in self.classes.items())}'
        )

    def weighted_class_choice(self):
        N = len(CLASSLIST)
        n = len(self.classes)
        class_weights = [None]*N
        for clazz in CLASSLIST:
            index = CLASSLIST.index(clazz)
            if clazz.name in self.classes.keys():
                class_weights[index] = 60/n
            else:
                class_weights[index] = 40/(N-n)
        return random.choices(population=CLASSLIST, weights=class_weights, k=1)[0]

    def level_up(self):
        if self.character_level == 12:
            print("this is max level you silly goose")
            return
        self.character_level += 1
        # print(f"DING Level {self.character_level}")
        clazz = self.weighted_class_choice()
        if clazz.name not in self.classes.keys():
            self.classes.update({clazz.name: clazz})
            # print(f"You gained a new class: {clazz.name}!")
            # if clazz.subclass:
            #     print(f"Subclass: {clazz.subclass}")
            self.history.update({self.character_level: clazz.to_json()})
        else:
            existing_class = self.classes[clazz.name]
            existing_class.level_up()
            self.classes.update({clazz.name: existing_class})
            # print(f"You leveled up your {clazz.name} class level! {clazz.name} Level {existing_class.level}")
            # if existing_class.level == existing_class.subclass_choice_level:
                # print(f"Subclass: {existing_class.subclass}")
            self.history.update({self.character_level: existing_class.to_json()})
        if self.character_level == 12:
            self.history.update({"Number of classes": len(self.classes)})


    def to_json(self):
            return json.dumps(self.history)
    