import random

simbolos = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","w","x","y","z","-","/",".",";","*","@","#","!","&","%","$","+","?","^","A","B","C","D","E",'F',"G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","W","X","Y","Z","(",")","<",">","1","2","3","4","5","6","7","8","9","0"]

print("¿De que largo quieres tu contraseña?: ")
print("1) Corta / poco segura 🥱")
print("2) Mediana / moderadamente segura 🥸")
print("3) Larga / muy segura 🔒")
print("4) Personalizada: 🤯")

largo = int(input("Escoje una opción: "))

password = []

if largo == 1:
    cantidad = 7

elif largo == 2:
    cantidad = 11

elif largo == 3:
    cantidad = 20

elif largo == 4:
    cantidad = int(input("Que tan larga quieres la contraseña? (digita el número): "))

else:
    print("Lo sentimos opción no válida 😣")
    exit()

#comprensión de listas
password = ''.join(random.choice(simbolos) for _ in range(cantidad))

print("Tu contraseña es 🤩: ", password)