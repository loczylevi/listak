'''
1.1 Feladat
Készíts egy programot, amely a felhasználótól keresztneveket kér be egészen addig, amíg az ENTER-t nem üt (nem ad meg újabb nevet a bekérésnél)! A program a bekért neveket írja ki a képernyőre!
'''
'''
nevek = []
while True:
  bekeres = input("Kérek keresztneveket!\t")
  if bekeres == "":
    break
  else:
    nevek.append(bekeres)
print(f"A lista elemei: {', '.join(nevek)}")
'''
#-----------------------

"""
1.2 Feladat
Fejleszd tovább úgy az előző programot, hogy a 3. név megadása után tájékoztassa a program a felhasználót, hogy már nincs lehetősége újabb adat bevitelére, írja ki az addig megadott neveket, és lépjen ki.
"""
nevek = []
hossz = 0
while hossz < 3:
  bekeres = input("Kérek keresztneveket!\t")
  nevek.append(bekeres)
  hossz = hossz + 1
  if hossz == 3:
    print(f"""Sajnálom már nincs lehetőség újabb nevek megadására!
A lista elemei: {', '.join(nevek)}""")
    break
    

