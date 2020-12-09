pip install colorama


#ESSAI 2 :


from colorama import init
init()
from colorama import Fore, Back, Style

# fonction : 

import random

def motAtrouver(mot_1,mot_joueur):
    for i in range (1,7):
        mot_joueur[i-1] = input("trouve une lettre :  ")
    return mot_joueur

def mot_vrai(mot_1,mot_joueur):
    for i in range (1,7):
        if mot_joueur[i-1] == mot_1 :
            print("you win")
        if mot_joueur[i-1] != mot_1 :
            print("you loose")
    return 

def lettre_bonne(mot_1, mot_joueur):
    for i in range (1,7):
        if mot_joueur[0] == mot_1[0]:
            print(Back.RED + mot_joueur[0], end=" ")
        if mot_joueur[1] == mot_1[1]:
            print(Back.RED + mot_joueur[1], end=" ")
        if mot_joueur[2] == mot_1[2]:
            print(Back.RED + mot_joueur[2], end=" ")
        if mot_joueur[3] == mot_1[3]:
            print(Back.RED + mot_joueur[3], end=" ")
        if mot_joueur[4] == mot_1[4]:
            print(Back.RED + mot_joueur[4], end=" ")
        if mot_joueur[5] == mot_1[5]:
            print(Back.RED + mot_joueur[5], end=" ")
    return lettre_bonne

def lettre_pas_presente(mot_1, mot_joueur):
    for i in range (1,7):
        if mot_joueur[0] != mot_1[0]:
            print(Back.BLUE + mot_joueur[0], end=" ")
        if mot_joueur[1] != mot_1[1]:
            print(Back.BLUE + mot_joueur[1], end=" ")
        if mot_joueur[2] != mot_1[2]:
            print(Back.BLUE + mot_joueur[2], end=" ")
        if mot_joueur[3] != mot_1[3]:
            print(Back.BLUE + mot_joueur[3], end=" ")
        if mot_joueur[4] != mot_1[4]:
            print(Back.BLUE + mot_joueur[4], end=" ")
        if mot_joueur[5] != mot_1[5]:
            print(Back.BLUE + mot_joueur[5], end=" ")
    return lettre_pas_presente

# tableaux : 

mot_1 =['c','a','s','t','o','r']
mot_2 =['c','i','n','e','m','a']
mot_3 =['c','y','p','r','e','s']
mot_4 =['c','i','t','r','o','n']

mot_joueur=[' ',' ',' ',' ',' ',' ']

motAtrouver(mot_1,mot_joueur)
mot_vrai(mot_1,mot_joueur)
lettre_bonne(mot_1,mot_joueur)
lettre_pas_presente(mot_1,mot_joueur)

print(motAtrouver)


input()