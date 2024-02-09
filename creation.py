from models.character import Tav

char = Tav("Bill")
print(char)
while char.character_level < 12:
    char.level_up()
