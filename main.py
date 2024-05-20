import random
lenght = int(input("Inserisci la lunghezza della password che desideri:"))
chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""
for i in range(lenght):
    n = random.randint(0, len(chars)-1)
    password = password+chars[n]

print("La tua password è:", password)
