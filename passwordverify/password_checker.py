import re
import string
import termcolor
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
print(ascii_banner)
termcolor.cprint("[*] Cette outil va déterminer si vous avez un mot de passe sécurisé.", "green")
boucle = True
while(boucle):
    c = input("[+] Entrez un mot de passe l'outil va vérifier si il est sécurisé : ")
    # wordlist check
    print("[~] Wordlists analyse... ")
    if wordlist(c) == True:
        print("[!] ATTENTION ce mot de passe est dans une liste de mot de passe qui a fuité donc trés connu des h4ckerM4n")

    #mot de passe pas assez long
    elif longeur(c) < 9 :
        print("[✓]  votre mot de passe n'est pas dans un liste de mot de passe qui a fuité !")
        print("ok pour longueur !")
        boucle = False

    #Maj dans mot de passe
    elif Majcheck(c) == False:
        print("[✓]  votre mot de passe n'est pas dans un liste de mot de passe qui a fuité !")
        print("ok pour maj ! ")

    #special carac dans mot de passe
    elif carac(c) == False:
        print("[✓]  votre mot de passe n'est pas dans un liste de mot de passe qui a fuité !")
        print("ok pour carac ! ")
    #Good password!
    elif wordlist(c) == False and longeur(c) > 9 and Majcheck(c) == True and carac(c) == True:
        print("ok pour bon mot de passe")
    #mauvaise entré de l'utilisateur
    else :
        print("")
