# M10.2-Bestanden - Oefening 2 - file 07
with open('voornamen.txt') as bestand:
    voornamen = bestand.readlines()
    for naam in voornamen[::-1]:
        print(naam, end='')

