# main
from repo_txt import *
from management import *
from tui import *
import os

def main():
    liste_woerte = open_file()
    wort = wort_erzeugen(liste_woerte)
    wort = wort.strip()
    anzahl_Spieler = menge_Spieler()
    Liste_Namen = eingabe_Spieler(anzahl_Spieler)
    os.system("cls")
    laenge_wort(wort)

    Erraten = []
    Richtig = ""
    zaehler = 0

    while zaehler < 6 and Richtig != "Richtig":
        for Name in Liste_Namen:
            print(f"\n{Name} ist Dran!\n")
            Buchstabe = buchstaben_raten()
            Erraten, Richtig, zaehler = wort_darstellen(wort, Buchstabe, Erraten, Richtig, zaehler)
            spiel_gewonnen(Richtig, Name, wort)
            spiel_verloren(zaehler, wort)

            if Richtig == "Richtig" or zaehler == 6:
                break


if __name__ == "__main__":
    main()