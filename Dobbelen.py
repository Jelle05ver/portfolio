#dobbel opdracht // in samenwerking met Tygo van Norel
#laatste update = 30-11-2022

import random
import time
#import random en time om later te kunnen gebruiker


min = 1
max = 6
#zet minnimun en maxinum van dobbelsteen
score = 0
#score op 0 want er is nog nier gegeooid
anwt = (input ("wilt u dobbelen? (ja of nee) \n"))
#vraag om input

while anwt == "ja":

    print ("aan het rollen...")



    steen1 = (random.randint(min,max))
    print (steen1)
#steen 1 word random tussen min (1) en max (6)
    time.sleep (1)
#set time op 1 puur voor de mooi


    steen2 = (random.randint(min,max))
#steen 2 word random tussen min (1) en max (6)
    print (steen2)

    time.sleep (1)
#set time op 1 puur voor de mooi


    if steen1 == 1 :
        steen2 = steen2 * 0
#als steen1, 1 is dan word steen 2 x 0 // steen 2 word 0
    elif steen1 == 6:
        steen2 = steen2 * 2 
#als steen 1, 6 is word steen 2 x 2 gedaan // verdubbeld  

    score = steen1 + steen2 
    print ('je score is' ,score)
#de score word opgeteld
    roll = input("nogmaals rollen?")
    if roll == "ja" :
        ()
    #als ja gezegd word niks gedaan 
    else:
        print ('fijne dag!' ) ,
        break
        #als iets anders is een break // stoppen
