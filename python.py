palabra = input("ingresa una palabra \n")
contador = 0
for letra in palabra:
    if letra.lower() == "a" or letra.lower() == "e"or letra.lower() == "i"or letra.lower() == "o" or letra.lower() == "u":
        contador+=1
print(f"la palabra '{palabra}' tiene {contador} vocales")

print("no se que mas")