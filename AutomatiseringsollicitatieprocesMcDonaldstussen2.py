#Jelle verheul V2 

#laatste update 28-1-2023

geboortejaar = 0 
#Var kan worden gebruikt in latere code niet in een def zit
def geslachtdef():
    while True:
        geslachten = ['man', 'vrouw', 'overig']
        #lijst met acceptable geslachte

        geslacht = input('van welk geslacht bent u? (man, vrouw, overig)\n:')

        if geslacht in geslachten:
        
            return geslacht
            # 't geslacht word opgeslagen in DEF geslachtdef
        #als 
        elif geslacht not in geslachten:
            print('wat u typt in niet acceptabel, probeer nog eens.')
        #als niet dan repeat de def tot goede input
        
def motivatiezindef ():
    motivatiezin = input('schrijf een leuke motivatie zin.\n:')
    return motivatiezin
# de zin wordt opgeslagen in de def door de return functie

def achernaamdef():
    while True:
        achternaam = input('wat is uw achternaam?\n:')
        
        if not achternaam.isalpha():
            #alleen als input in alfabet is gaat verder 
            print('alleen letter graag')
            continue
        else:
            
            return achternaam

def vraaggeboortejaar():

    while True:
        try:
            geboortejaar = int(input("wanneer bent u geboren?\n: "))
            #aleen een int(getal) word aangenomen
            return geboortejaar  

        except ValueError:
            print("wat u typt is niet acceptabel probeer alleen getallen .")  
            continue
        




##lijst = [geslachtdef() , motivatiezindef() , achernaamdef() ]
#lijst=[]
#lijst.append(geslachtdef())
#def's worden opgeslagn in lijst de lijs maar deze kijst krijg ik niet een break tusssen
#dus daarom heb ik apart opgeroepen

f = open("Python/Periode 2/logboekaplicatie.txt", "w")


#f.write(str(lijst))
f.write(str(achernaamdef() + '.\n'))
f.write(str(geslachtdef() + ".\n")) 
#.\n is een break nieuwe regel beginnen
jaartal = vraaggeboortejaar()

leeftijd = 2023 - jaartal  

f.write('u bent of word ' + (str(leeftijd)) + ' ,geboren in ' + (str(jaartal)) + '.\n')

f.write(str(motivatiezindef() + '.\n')) 




f.close()

#print(lijst , 'staan nu in text file')

            
