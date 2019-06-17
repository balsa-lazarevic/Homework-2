import random

lista_brojeva = [4, 5, 2, 8, 9, 1, 10, 3, 7, 6]

random.shuffle(lista_brojeva)

parovi = []

for index, val in enumerate(lista_brojeva):
    if not index % 2:
        parovi.append([val, lista_brojeva[index + 1]])

print(parovi)