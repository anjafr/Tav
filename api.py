from models.character import Tav

bill = Tav("Bill")

while bill.character_level < 12:
    bill.level_up()

print(bill.to_json())
