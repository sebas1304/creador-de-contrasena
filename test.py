import random

passlen = input("introduzca longitud de la clave:")
longpass="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password=""
totalpass=""
for i in range(passlen):
    password += random.choice(longpass)
    totalpass = totalpass + password
print(totalpass)