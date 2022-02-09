"""3. Feladat
A program generáljon 10 darab véletlenszámot [0;50] intervallumon, de csak a 4-gyel oszthatóakat rögzítse egy listában. A végén jelenítse meg a listát a képernyőn, és írja ki azt is, hány elemből áll a lista."""
import random
lista = []
a = 0
while a < 10:
  veletlen = random.randint(0,50)
  a = a + 1
  if veletlen % 4 == 0:
    lista.append(veletlen)

print(f"A lista elemei: {lista}")
print(f"Lista hosszúsága: {len(lista)}")

