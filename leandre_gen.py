import random
letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

little_letter = "abcdefghijklmnopqrstuvwxyz"

nombre = "0123456789"

sysboles = "!§/?%µ$£^@&"

carac = letter + nombre + sysboles + little_letter
carac_sys = letter + nombre + little_letter


print("#########################")
print("####Léandre générator####")
print("#########################")

enter = int(input("enter un le nombres de caracteres que vous voulez dans votre mot de passe (8, 12, 16) :"))

if enter == 8:
    password = "".join(random.sample(carac, enter))
    print ("votre mot de passe est :","---", password,"---")

elif enter ==12:
    password1 = "".join(random.sample(carac, enter))
    print("votre mot de passe est :","---",password1,"---")

elif enter == 16:
    password2 = "".join(random.sample(carac, enter))
    print("votre mot de passe est :", "---", password2,"---" )

else :
    enter != 8, 12, 16
    print("!!!!error!!!!!")