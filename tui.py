#tui

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


def wort_darstellen(wort):
    print("Errate folgendes Wort:  ")
    laenge = len(wort)
    print("_" * laenge)
	
    print("Welchen Buchstaben möchtest du?")


