pip install colorama

from colorama import init
init()
from colorama import Fore, Back, Style
print(Fore.RED + 'some red text', end=" ")
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
input()

# fonction : 

def motAtrouver (mot_joueur):
    for i in range (1,7):
        mot_joueur[i-1] = input("trouve une lettre :  ")
    return mot_joueur

# tableaux : 
mot_1=['c','a','s','t','o','r']
mot_2=['c','i','n','e','m','a']
mot_3=['c','y','p','r','e','s']
mot_4=['c','i','t','r','o','n']
mot_5=['','','','','','']
mot_6=['','','','','','']
mot_7=['','','','','','']
mot_8=['','','','','','']
mot_9=['','','','','','']
mot_10=['','','','','','']
mot_joueur=[' ',' ',' ',' ',' ',' ']
mot_joueur = motAtrouver(mot_joueur)
print (motAtrouver)
