"""2.1 Feladat
Az adott lista (amely a 'Próbáld ki!' gombra kattintva elérhető) elemei közül a program kiírja a "t" és "T" betűkkel kezdődőeket"""

szavak = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']
kereso = [print(f"\"t\"-betüs szó: {szo}") for szo in szavak if szo[0] == "t" or szo[0] == "T"]
