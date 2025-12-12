# main
from repo_txt import *
from management import *
from tui import *
import os

def main():
    liste_woerte = open_file()
    wort = wort_erzeugen(liste_woerte)
    anzahl_Spieler = menge_Spieler()
    Liste_Namen = eingabe_Spieler(anzahl_Spieler)

    os.system("cls")
    print(wort)
    wort = wort.strip()
    print("Errate folgendes Wort:  ")
    laenge = len(wort)
    print("_" * laenge + "\n")

    while True:
        for Name in Liste_Namen:
            print(f"\n{Name} ist Dran!\n")
            Buchstabe = buchstaben_raten()
            speicher = wort_darstellen(wort, Buchstabe, speicher)



if __name__ == "__main__":
    main()