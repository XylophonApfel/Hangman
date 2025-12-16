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


def wort_darstellen(wort, Buchstabe, Erraten, Richtig, zaehler):
    os.system("cls")
    
    if Buchstabe != wort:
        if Buchstabe.lower() not in wort and Buchstabe.upper() not in wort:
            zaehler += 1
            hangman_zeichen(zaehler)

    if not Erraten:
        Erraten = ["_"] * len(wort)

    if Buchstabe.lower() == wort.lower():
        Richtig = "Richtig"
        return Erraten, Richtig, zaehler

    else:
        for idx, letter in enumerate(wort):
            if Buchstabe.lower() == letter.lower():
                Erraten[idx] = letter.lower()

        if "_" not in Erraten:
            Richtig = "Richtig"
            return Erraten, Richtig, zaehler

    print("".join(Erraten))

    return Erraten, Richtig, zaehler