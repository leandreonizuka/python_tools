import re
import string
import termcolor
import pyfiglet
#Fonction
def password_verificateur():
    c = str(input("Entrer un mot de passe : "))
    compteurlonguer = int()
    compteurcarac = False
    compteurmaj = int()
    string_check = re.compile('[@_ù!#$%^&*()<>?/\|}{~:]')
    wordlist = False

    #boucles
    for i in c:
        compteurlonguer += 1
        if i.isupper():
            compteurmaj += 1
        else:
            compteurmaj += 0

    #compteur longueur check
    if compteurlonguer >= 9:
        termcolor.cprint("[✓] Ce mot de passe est long","blue")
    else:
        termcolor.cprint("[X] Ce mot de passe est trop court ","red")

    #compteur caratéres spéciaux check
    if (string_check.search(c) == None):
        termcolor.cprint("[X] aucun caracteres spéciales détecter !","red")
    else:
        compteurcarac = True
        termcolor.cprint("[✓] Ce mot de passe comporte des caracteres spéciaux","blue")

    #maj check
    if compteurmaj < 1:
        termcolor.cprint("[X] Ce mot de passe ne comptient pas de majuscule ", "red")
    else:
        termcolor.cprint("[✓] Ce mot de passe comptient une ou des majuscules ", "blue")

    #wordlist check
    print("[~] Rockyou wordlist analyse ...")
    fichier = open("wordlist.txt", "r", encoding="utf-8", errors="ignore")
    contenu = [ligne.rstrip() for ligne in fichier.readlines()]
    fichier.close()

    if c in contenu:
        wordlist = True
    else :
        print("[✓] Ce mot de passe n'est pas dans une liste de mot de passe connue des hackers")
        wordlist = False

    #verdicte du programme
    if compteurmaj > 0 and compteurcarac == True and compteurlonguer >= 9:
        print("[*] Ce mot de passe est fort !!")
    elif compteurmaj > 0 and compteurcarac == True and compteurlonguer < 9:
        print("[~] CE mot de passe est trop petit ")
    elif compteurmaj == 0 and compteurcarac == True and compteurlonguer >= 9:
        print("[~] Ce mot de passe est pas mal mais il manque une majuscule !")
    elif wordlist == True :
        print("[X] Ce mot de passe est dans une liste de mot de passe trés connu des hackers ! Attention ")
        hacked = pyfiglet.figlet_format("cracked")
        print(hacked)
    elif compteurmaj > 0 and compteurcarac == False and compteurlonguer >= 9:
        print("[~] Le mot de passe est pas mal mais il manque un ou plusieur caractéres spéciales ! ")
    else:
        print("[X] le Mot de passe est faible ! =(")


#Programmes initialisation
ascii_banner = pyfiglet.figlet_format("PasswordVerrify")
print(ascii_banner)
termcolor.cprint("[*] Cette outil va déterminer si vous avez un mot de passe sécurisé.", "green")
boucles = True
while(boucles):
    start = str(input("[*] Entré 'y' Pour commencer la vérification : "))

    if start == "y":
        boucles = False
        password_verificateur()
    else:
        termcolor.cprint("[X] Mauvaise entré de l'utilisateur !", "red")
        boucles = True
