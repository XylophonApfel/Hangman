# main
from repo_txt import *
from management import *
from tui import *
import os

def main():
    # Lesen und Speichern der Wörter datei in repo_txt
    liste_woerte = open_file()
    # Wort per zufall auswählen in management
    wort = wort_erzeugen(liste_woerte)
    # Leerzeichen entfernen
    wort = wort.strip()
    # Eingabe Anzahl der Spieler in management
    anzahl_Spieler = menge_Spieler()
    # Zuordnung der Namen in management
    Liste_Namen = eingabe_Spieler(anzahl_Spieler)

    # Erste Anzeige zum Starten des Spieles in tui
    os.system("cls")
    laenge_wort(wort)

    # Notwendige Variabeln für die Darstellung
    Erraten = []
    buchstabe_fehler = []
    Richtig = ""
    zaehler = 0

    # Beginn von Abfrag
    while zaehler < 6 and Richtig != "Richtig":
        for Name in Liste_Namen:
            print(f"\n{Name} ist Dran!\n")
            Buchstabe = buchstaben_raten()
            Erraten, Richtig, zaehler, buchstabe_fehler = wort_darstellen(wort, Buchstabe, Erraten, Richtig, zaehler, buchstabe_fehler)
            spiel_gewonnen(Richtig, Name, wort)
            spiel_verloren(zaehler, wort)

            if Richtig == "Richtig" or zaehler == 6:
                break


if __name__ == "__main__":
    main()