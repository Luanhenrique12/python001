import random
cesta=["Carro","Moto","Avião","Barco"]

print("Você foi premiado com:",random.choice(cesta))
cesta.pop(0)
print(cesta)