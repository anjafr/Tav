import random
from models.clazz import CLASSLIST
from models.race import RACELIST

BACKGROUNDLIST = [
    "Acolyte",
    "Charlatan",
    "Criminal",
    "Entertainer",
    "Folk Hero",
    "Guild Artisan",
    "Noble",
    "Outlander",
    "Sage",
    "Soldier",
    "Urchin",
]


class Tav:
    def __init__(self, name="Tav", num_max_classes=12):
        self.name = name
        self.character_level = 1
        self.num_max_classes = num_max_classes
        self.race = random.choice(RACELIST)
        self.background = random.choice(BACKGROUNDLIST)
        self.history = []
        self.classes = {}
        self.level_up_class()

    @property
    def __dict__(self):
        return {"name": self.name, "race": f"{self.race}", "background": self.background, "progression": self.history}

    def present_classes(self):
        return list(self.classes.values())

    def available_classes(self):
        if self.num_max_classes > len(self.classes):
            return CLASSLIST
        else:
            return self.present_classes()

    def at_max_number_of_different_classes(self):
        return len(self.present_classes()) == self.num_max_classes

    def weighted_class_choice(self):
        if self.at_max_number_of_different_classes():
            return random.choice(self.present_classes())
        return self.weigthed_new_or_existing_clazz()

    def weigthed_new_or_existing_clazz(self):
        N = len(self.available_classes())
        n = len(self.classes)
        class_weights = [None] * N
        for clazz in self.available_classes():
            index = self.available_classes().index(clazz)
            if clazz.name in self.classes.keys():
                class_weights[index] = 60 / n
            else:
                class_weights[index] = 40 / (N - n)
        return random.choices(population=self.available_classes(), weights=class_weights, k=1)[0]

    def level_up_class(self):
        clazz = self.weighted_class_choice()
        if clazz.name not in self.classes.keys():
            self.classes[clazz.name] = clazz()

        self.classes[clazz.name].level_up()
        self.history.append(self.classes[clazz.name].__dict__)

    def level_up(self):
        if self.character_level == 12:
            print("this is max level you silly goose")
            return

        self.character_level += 1
        self.level_up_class()
        