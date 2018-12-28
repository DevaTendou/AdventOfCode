#Advent of Code 7.1
from functools import reduce as red
file = open("c:\\users\\devatendou\\Desktop\\AdventCode2017\\AdventCode7.txt", 'r')

lista = ["".join([c for c in line if c not in "0123456789->,()"]).split() for line in file]
temp = [l[1:] for l in lista if len(l) > 1]
lista = [l[0] for l in lista]
seen = []

for l in lista:
    for t in temp:
        if l in t:
            seen.append(lista.index(l))
            break

numbers = [i for i in range(len(lista))]

print(lista[list(set(numbers) - set(seen))[0]])

file.close()
