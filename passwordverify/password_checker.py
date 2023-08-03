import re
import string
from termcolor import *
import pyfiglet

#introduction des fonctions
#logeur check
def longeur(mot):
    compteur = 0
    for i in mot :
        compteur += 1
    return compteur
#Maj check
def Majcheck(mot):
    compteurMaj = False
    for i in mot :
        if i.isupper():
            compteurMaj = True
    return compteurMaj

#spécial carac
def carac(mot):
    compteur = True
    string_check = re.compile('[@_ù!#$%^&*()<>?/\|}{~:]')
    if (string_check.search(mot) == None):
        compteur = False
    return compteur

#wordlists analyse :
def wordlist(mot):
    compteur = False
    fichier = open("wordlist.txt", "r", encoding="utf-8", errors="ignore")
    contenu = [ligne.rstrip() for ligne in fichier.readlines()]
    fichier.close()

    if mot in contenu:
        compteur = True
    return compteur


#programmes initialisation
ascii_banner = pyfiglet.figlet_format("PasswordVerrify")
cprint(ascii_banner, "magenta")
cprint("[*]", "blue", end="")
print(" Cet outil va déterminer si vous avez un mot de passe sécurisé.")
boucle = True
while(boucle):
    cprint("[*]", "blue", end="")
    c = input(" Entrez un mot de passe, l'outil va vérifier s'il est sécurisé : ")
    # wordlist check
    cprint("[*]", "blue", end="")
    print(" Wordlists analyse...")
    if wordlist(c) == True:
        cprint("[!]", "red", end="")
        print("ATTENTION ce mot de passe est très connu des h4 ckerM4nsh4ckerm4 ns, il est conseillé de ne pas l'utiliser !")

    else:
        cprint("[+]", "green", end="")
        print(" le mot de passe n'est pas dans une liste connu des h4ckerM4ns !")

    #longueur du mot de passe
    if longeur(c) < 9:
        cprint("[!]", "red", end="")
        print(" votre mot de passe est trop court, augmenter sa longueur pour optimiser sa sécurité !")

    else:
        cprint("[+]", "green", end="")
        print(" votre mot de passe est long")

    # assez long mais pas de majuscules
    if Majcheck(c) == False:
        cprint("[!]", "red", end="")
        print(" il manque une majuscule pour optimiser la sécurité du mot de passe.")

    else:
        cprint("[+]", "green", end="")
        print(" le mot de passe comporte une ou plusieur majuscules.")

    # carac spécial check
    if carac(c) == False:
        cprint("[!]", "red", end="")
        print(" le mot de passe ne comporte pas de caractères spéciaux, ajouter sans un pour optimiser sa sécurité.\n")

    else:
        cprint("[+]", "green", end="")
        print(" le mot de passe comporte un ou plusieurs caractères spéciaux.\n")

    next = input("[-] Voulez-vous entrer un autre mot de passe ?(y,n):",)
    print("\n")
    if next == "y":
        boucle = True
    else :
        print("Bye !)")
        break

