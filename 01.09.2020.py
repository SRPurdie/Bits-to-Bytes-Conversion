import time
Beenden = False

while Beenden == False:
    print("\nHerzlich Willkommen beim Bits und Bytes Rechner!")
    print (
    "1 - Eingabe in Bit\n"
    "2 - Eingabe in Byte\n"
    "3 - Eingabe in Kibibyte\n"
    "4 - Eingabe in Mebibyte\n"
    "5 - Eingabe in Gibibyte\n"
    "6 - Eingabe in Tebibyte\n"
    "0 - Beenden\n")
    
    number = int(input("Bitte wählen:\n"))
    
    if number == 0:
        exit("Das Programm wurde erfolgreich abgebrochen")
        
    elif number < 1:
        exit("Bitte eine Zahl zwischen 0 und 6 eingeben")
        
    elif number > 6:
        exit("Bitte eine Zahl zwischen 0 und 6 eingeben")
        
    Liste = ["", "Bits", "Bytes", "Kibibyte", "Mebibyte", "Gibibyte", "Tebibyte"]
    eingabe = int(input("Bitte Anzahl {} eingeben:\n".format(Liste[number])))
    
    print("Ergebnis wird berechnet....\n")
    time.sleep(1)
    
    if number == 1:
        bit = eingabe
    
    elif number == 2:
        bit = eingabe*8
        
    elif number == 3:
        bit = eingabe*8*1024
            
    elif number == 4:
        bit = eingabe*8*1024*1024
    
    elif number == 5:
        bit = eingabe*8*1024*1024*1024
        
    elif number == 6:
        bit = eingabe*8*1024*1024*1024*1024
        
    byte = bit / 8
    Kibibyte = byte / 1024
    Mebibyte = Kibibyte / 1024
    Gibibyte = Mebibyte / 1024
    Tebibyte = Gibibyte / 1024
    
    #Ergebnis
    print("\tBit:\t\t", bit)
    print("\tByte:\t\t", byte)
    print("\tKibibyte:\t\t", Kibibyte)
    print("\tMebibyte:\t\t", Mebibyte)
    print("\tGibibyte:\t\t", Gibibyte)
    print("\tTebibyte:\t\t", Tebibyte)
    
    print("\nLade Programm neu...\n")
    time.sleep(10)
    