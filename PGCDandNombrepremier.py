#nombre premier calculator
def nombre_premier():
    nombre = int(input("entrer un nombre entier :"))
    
    for n in range(2, nombre):
        if nombre % n == 0:
            return("Ce nombre n'est pas premier !")
        else:
            return("Ce nombre est premier !")
#PGCD calculator
def PGCD():
    nombre1 = int(input("entrer un nombre entier positifes: "))
    nombre2 = int(input("entrer un deuxieme nombre entier positifes : "))


    if nombre1 > nombre2 :
        x = nombre1
        y= nombre2
    else : 
        x = nombre2
        y = nombre1
    
    while(x%y!=0):
        reste = x%y
        x = y
        y = reste
    return("Le PGCD de " + str(nombre1) + " et " + str(nombre2) + " est égales a " + str(y))

#initialisation programme

print("**calculateur Nombre premier et PGCD **")


print("a = calculateur nombre premier \nb = calculateur PGCD de deux nombres")
c = input("entrer votre choix: ")

if c == "a":
    print(nombre_premier())
elif c =="b":
    print(PGCD())
else:
    print("Mauvaise entrer de l'utilisateur =(")
