#tui
import os

def hangman_zeichen(zaehler):
    match zaehler:
        case 1:
            print(" ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))	
            print(chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))
        
        case 2:
            print("   ",chr(9744),chr(9744),chr(9744))
            print("  ",chr(9744),chr(9744),chr(9744),chr(9744))
            print(" ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))	
            print(chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))
        
        case 3:
            print("     ",chr(9744))
            print("     ",chr(9744))
            print("     ",chr(9744))
            print("     ",chr(9744))
            print("     ",chr(9744))
            print("     ",chr(9744))
            print("     ",chr(9744))
            print("     ",chr(9744))
            print("     ",chr(9744))
            print("     ",chr(9744))
            print("     ",chr(9744))
            print("     ",chr(9744))	
            print("     ",chr(9744))
            print("   ",chr(9744),chr(9744),chr(9744))
            print("  ",chr(9744),chr(9744),chr(9744),chr(9744))
            print(" ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))	
            print(chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))

        case 4:
            print("     ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))
            print("     ",chr(9744))
            print("     ",chr(9744))
            print("     ",chr(9744))
            print("     ",chr(9744))
            print("     ",chr(9744))
            print("     ",chr(9744))
            print("     ",chr(9744))
            print("     ",chr(9744))
            print("     ",chr(9744))
            print("     ",chr(9744))
            print("     ",chr(9744))	
            print("     ",chr(9744))
            print("   ",chr(9744),chr(9744),chr(9744))
            print("  ",chr(9744),chr(9744),chr(9744),chr(9744))
            print(" ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))	
            print(chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))

        case 5:
            print("     ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))
            print("     ",chr(9744),"       ",chr(9744))
            print("     ",chr(9744),"       ",chr(9744))
            print("     ",chr(9744),"       ",chr(9744))
            print("     ",chr(9744))
            print("     ",chr(9744))
            print("     ",chr(9744))
            print("     ",chr(9744))
            print("     ",chr(9744))
            print("     ",chr(9744))
            print("     ",chr(9744))
            print("     ",chr(9744))	
            print("     ",chr(9744))
            print("   ",chr(9744),chr(9744),chr(9744))
            print("  ",chr(9744),chr(9744),chr(9744),chr(9744))
            print(" ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))	
            print(chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))

        case 6:
            print("     ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))
            print("     ",chr(9744),"       ",chr(9744))
            print("     ",chr(9744),"       ",chr(9744))
            print("     ",chr(9744),"       ",chr(9744))
            print("     ",chr(9744),"     ",chr(9744),chr(9744),chr(9744))
            print("     ",chr(9744),"    ",chr(9744),"   ",chr(9744))
            print("     ",chr(9744),"     ",chr(9744),chr(9744),chr(9744))
            print("     ",chr(9744),"       ",chr(9744))
            print("     ",chr(9744),"   ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))
            print("     ",chr(9744),"       ",chr(9744))
            print("     ",chr(9744),"     ",chr(9744),chr(9744),chr(9744))
            print("     ",chr(9744),"     ",chr(9744)," ",chr(9744))		
            print("     ",chr(9744))
            print("   ",chr(9744),chr(9744),chr(9744))
            print("  ",chr(9744),chr(9744),chr(9744),chr(9744))
            print(" ",chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))	
            print(chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744),chr(9744))


def wort_darstellen(wort, Buchstabe, Speicher):
    os.system("cls")

    wort_klein = ""
    wort_liste = []
    Erraten = []

    for i in wort:
        Erraten.append("_")
        wort_liste.append(i.lower())
        wort_klein += i.lower()

    if Buchstabe == wort:
        print("richtig")
    else:
        for i in wort:
            if Buchstabe.lower() == i or Buchstabe.upper() == i:
                platz = wort.index(i)
                Erraten[platz] = Buchstabe.lower()
                wort_liste[platz] = "-"

            if "_" not in Erraten:
                print("Richtig")
                        

    for i in wort:
        platz = wort.index(i)
        print(Erraten[platz], end='')

    return Erraten

