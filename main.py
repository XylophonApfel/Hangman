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
    Erraten = []
    Richtig = ""
    zaehler = 0

    while Richtig != "Richtig":
        for Name in Liste_Namen:
            print(f"\n{Name} ist Dran!\n")
            Buchstabe = buchstaben_raten()
            Erraten, Richtig, zaehler = wort_darstellen(wort, Buchstabe, Erraten, Richtig, zaehler)
            if Richtig == "Richtig":
                print(f"Herzlichen Glückwunsch {Name}, du hast das Wort '{wort}' erraten!")
                break
    
    print("Fertig")



if __name__ == "__main__":
    main()