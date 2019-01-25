import os
menu=print("Bienvenue dans le menu des retardataires")
choix=input("Si vous voulez choisir le programme mathématique Tapez 1 :\n Si vous voulez choisir le programme géométrie Tapez 2 :\n Si vous voulez choisir le programme liste Tapez 3 :\n Si vous voulez choisir le programme fichiers Taper 4 :\n choix >>>>>>>")
choix= str(choix)

if str(choix) == '1':
    os.system("mathematiques.py 1")

if str(choix) == '2' :
    os.system("geometrie.py 1")

if str(choix) == '3' :
    os.system("listes.py 1")

if str(choix) == '4' :
    os.system("fichiers.py 1")
