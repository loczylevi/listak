'''
2.1 Feladat
Készíts egy programot, amely a felhasználótól kis "a" betűvel kezdődő szavakat kér be és ezeket tárolja. Ha a felhasználó nem "a" betűvel kezdődő szót ad meg, akkor azt hagyja figyelmen kívül és ne tárolja. A bekérés egészen addig folytatódjon, amíg a felhasználó ENTER-t nem üt (nem ad meg újabb nevet a bekérésnél)! A program a bekért neveket írja ki a képernyőre!

A program tájékoztatássa a felhasználót a működéséről, és az elvárt adatokról!

2.2 Feladat
Alakítsd át úgy az előző porgramot, hogy az ne csak kis, hanem a nagy "A" betűvel kezdődő szavakat is elfogadja.
'''
szavak = []
print("A program szavakat kér be mig a felhasználó enter nem üt!\n Minden szavat bele rak a listába ami kis vagy nagy \"a\"-val kezdődik!\n ")
while True:
  bekeres = input("Kérek szavakt, uram!\t")
  if bekeres == "":
    break
  elif bekeres[0] == "a" or bekeres[0] == "A":
    szavak.append(bekeres)
print(f"A lista elemei:{', '.join(szavak)}")
  
