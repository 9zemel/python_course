import random

amountBullets = input("Сколько зарядить? ")
aob = int(amountBullets)
baraban = [0,0,0,0,0,0]

for i in range(aob):
    baraban[i] = 1

howMuch = input("Сколько раз крутить? ")
hm = int(howMuch)
for i in range(hm):
    random.shuffle(baraban)
    if baraban[0] == 1:
        print("Выстрел!\a")
    else:
        print("щелк")

