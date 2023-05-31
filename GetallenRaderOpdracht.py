#dit is de eindopdracht medium

naam1 = str(input('Speler 1 kies een naam\n'))
#naam1 word gewezen aan speler 1 
naam2 = str(input('Speler 2 kies een naam\n'))
#naam2 word toegewezen naar speler 2
maxpoging = int(input('Kies hoeveel pogingen\n'))
#onthoud max pogingen
getal = int(input(f' {naam1} kies een getal tussen 1 en 100\n'))
# Persoon 1  kan getal kiezen word opgeslaagd in Getal




#while getal != antwoord:
 
poging = 0
#poging word naar 0 gezet
antwoord = 0 
while poging < maxpoging and antwoord != getal:
    #als poging is kleinde max loopen and andwoord is niet gelijk aan andwoord. 
    antwoord = int(input(f' {naam2} raad het getal van speler\n'))
    # Persoon 2 raad het getal word opgeslagen in raadgetal

    if getal == antwoord: 
        print ('Goed bezig dikke duim 👍')
        # als getal is gelijk aan anwwoord dan is t goed
        #break

    elif getal < antwoord: 
        #< 
        print ('Je getal is hoger dan verwacht ' f'{naam2}')
            #elif is zelfde als is else 
    else: 
        print ('Je getal is lager dan verwacht ' f'{naam2}')
        
        
        
    #print pogingen 
    poging += 1 
    print("conditie is : ",poging<maxpoging)


if poging == maxpoging:
    print('Je hebt teveel kansen gehad')
       #poging evenveel als max word je kans verkeken

