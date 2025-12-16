#management
import random
import os 
from tui import *

def menge_Spieler():
    os.system("cls")
    print("------------------------------------------")
    print("          Willkommen bei Hangman!")
    print("------------------------------------------\n")
    print("Hangman kann mit 2-5 Speilern gespielt werden!")
    while True:
        try:
            anzahl = int(input("Mit wie vielen Spieler möchtet ihr Spielen: "))
            if anzahl <=5 and anzahl >= 2:
                break
            else:
                os.system("cls")
                print("Bitte geben sie eine zahl zwischen 2-5 ein!")
        except ValueError:
            os.system("cls")
            print("Bitte geben Sie eine zahl ein!")
    return anzahl

def eingabe_Spieler(anzahl_Spieler):
    Spieler_Name = []
    os.system("cls")
    print(f"Sie spielen mit {anzahl_Spieler}!")
    for i in range(1, anzahl_Spieler+1):
        while True:
            try:
                Name = str(input(f"Bitte geben Sie den Namen für Spieler {i} ein: "))
                if Name.isalpha():
                    Spieler_Name.append(Name)
                    break
                else:
                    print("Es sind nur Buchstaben erlaubt!")
            except ValueError:
                print("Es sind nur Buchstaben erlaubt!")
    
    return Spieler_Name

def wort_erzeugen(liste_woerter):
    wort = random.choice(liste_woerter)

    return wort

def buchstaben_raten():
    while True:
        try:
            Buchstabe = str(input("\nWelchen Buchstaben oder Wort möchtetst du raten: "))
            if Buchstabe.isalpha():
                break
            else:
                print("Bitte gebe nur Buchstaben ein!")
        except ValueError:
            print("Bitte gebe nur Buchtsaben ein!")
    
    return Buchstabe

def spiel_gewonnen(richtig, Name, wort):
    if richtig == "Richtig":
        os.system("cls")
        print(f"Herzlichen Glückwunsch {Name}, du hast das Wort '{wort}' erraten!")

def spiel_verloren(zaehler, wort):
    if zaehler == 6:
        os.system("cls")
        hangman_zeichen(zaehler)
        print(f"\nDu hast leider verloren :( \nDas Wort war {wort}")