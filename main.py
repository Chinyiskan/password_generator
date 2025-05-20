import random
import string

# Lista de símbolos seguros y variados
simbolos = list(string.ascii_letters + string.digits + "-/.*@#!&%$+?^()<>;ñÑ")


# Menú de opciones
print("¿De que largo quieres tu contraseña?: ")
print("1) Corta / poco segura 🥱")
print("2) Mediana / moderadamente segura 🥸")
print("3) Larga / muy segura 🔒")
print("4) Personalizada: 🤯")

# Validar entrada
try:
    opcion = int(input("Escoge una opción (1-4): "))
except ValueError:
    print("❌ Debes ingresar un número.")
    exit()

# Validar rango
if opcion not in [1,2,3,4]:
    print("❌ Opción no válida.")
    exit()

# Definir longitud
if opcion == 1:
    cantidad = 7

elif opcion == 2:
    cantidad = 11

elif opcion == 3:
    cantidad = 20

else:
    try:
        cantidad = int(input("¿Qué tan larga quieres la contraseña?: "))
        if cantidad <= 0:
            print("❌ El número debe ser mayor a cero.")
            exit()
    except ValueError:
        print("❌ Debes ingresar un número válido.")
        exit()

# Generador contraseña
#comprensión de listas
password = ''.join(random.choice(simbolos) for _ in range(cantidad))

print("Tu contraseña es 🤩: ", password)