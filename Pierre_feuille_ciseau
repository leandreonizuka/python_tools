import random
from random import shuffle
def jeux():
    joueur = int()
    ordi = int()
    choix = ["pierre", "feuille", "ciseau"]
    while joueur < 3 and ordi < 3:
        entrer = str(input("entrer votre choix (pierre, feuille, ciseau): "))
        random.shuffle(choix)
        odir_choix = choix[1]
        print("le choix de La machine est : ",odir_choix)
        if entrer == "pierre" and odir_choix == "feuille":
            ordi += 1
            print("+ 1 point pour la machine !")
            print("joueur point = ", joueur,"\nMachine point =", ordi)
        elif entrer == "pierre" and odir_choix == "ciseau":
            joueur += 1
            print("+ 1 point pour le joueur !")
            print("joueur point = ", joueur, "\nMachine point =", ordi)
        elif entrer == "ciseau" and odir_choix == "pierre":
            ordi += 1
            print("+ 1 point pour la machine !")
            print("joueur point = ", joueur, "\nMachine point =", ordi)
        elif entrer == "ciseau" and odir_choix == "feuille":
            joueur += 1
            print("+ 1 point pour le joueur !")
            print("joueur point = ", joueur, "\nMachine point =", ordi)
        elif entrer == "ciseau" and odir_choix == "ciseau":
            print("égalité ! ")
            print("joueur point = ", joueur, "\nMachine point =", ordi)
        elif entrer == "feuille" and odir_choix == "feuille":
            print("égalité ! ")
            print("joueur point = ", joueur, "\nMachine point =", ordi)
        elif  entrer == "feuille" and odir_choix == "ciseau":
            ordi += 1
            print("+ 1 point pour la machine !")
            print("joueur point = ", joueur, "\nMachine point =", ordi)
        elif entrer == "feuille" and odir_choix == "pierre":
            joueur += 1
            print("+ 1 point pour le joueur !")
            print("joueur point = ", joueur, "\nMachine point =", ordi)
        elif entrer == "pierre" and odir_choix == "pierre":
            print("égalité ! ")
            print("joueur point = ", joueur, "\nMachine point =", ordi)
        else :
            print("[...] mauvaise entré de l'utilisateur =( ")
    #score
    if joueur > ordi:
        print("[+] joueur WIN ! GG ")
        print("joueur point = ", joueur, "\nMachine point =", ordi)
        print("""\
              (っ▀¯▀)つ      
        """)

    else:
        print("[X] Machine WIN !")
        print("joueur point = ", joueur, "\nMachine point =", ordi)
        print("""\
            ᕦ(ò_óˇ)ᕤ
        """)


#initialisation programmes
print("[*]Bienvenue dans le jeu Pierre / Feuille / Ciseau.\n[!] les regles sont les suivantes : le premier en trois points gagne.")
restart = True
while(restart):
    c = str(input("[!]Si vous voulez commencer à jouer contre la Machine entré 'start' : "))

    if c == "start":
        print("[~] chargement ... ")
        print(jeux())
        restart = False
    else:
        print("[X] mauvaise entré de l'utilisateur !")
