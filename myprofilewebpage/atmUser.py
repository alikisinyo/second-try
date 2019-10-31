from atm import ATMCard

aliCard = ATMCard(1000)
lucyCard = ATMCard(10000)
letinaCard = ATMCard(100)
# print(type(aliCard))
# print(aliCard.name)
# print(aliCard.color)
print("lucy's balance is ", lucyCard.balance)
print("letina has deposited ", letinaCard.deposit(100))