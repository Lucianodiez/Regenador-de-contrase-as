import random

letras = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("Que tan largo quieres que sea de parfo la palabra "))
contraseña = ""

for i in range(longitud):
    contraseña += random.choice(letras)

print(contraseña)
