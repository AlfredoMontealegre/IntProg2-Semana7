""" Leer una palabra diferente a fin y convertirla
a Mayuscula"""

palabra = input("Dame una palabra: ")
for i in range(10000000000):
    if (palabra.lower() == "fin"):
        print("Adios...")
        break
    else:
        print(f"{palabra.upper()} tiene {len(palabra)} letras")
        palabra = input("Dime una palabra: ")