#Advent of Code 6.1

file = open("C:\\Users\\devatendou\\Desktop\\AdventCode2017\\AdventCode6.txt", 'r')

numbers = file.readline().split()
numbers = [int(x) for x in numbers]
seen = [str(numbers)]

def findGreat(lista):
    great = max(numbers)
    index = 0
    for n in numbers:
        if n == great:
            return index
        index += 1

def newList(lista):       
    newIndex = findGreat(lista)
    num = lista[newIndex]
    lista[newIndex] = 0
    index = newIndex
    while num:
        index = (index + 1)%len(lista)
        lista[index] += 1
        num -= 1
    return lista

count, final, distance = 0, 0, 0
while True:
    numbers = newList(numbers)
    count += 1
    for s in seen:
        if str(numbers) == s:
            distance = count - seen.index(s)
            final = 1
            break
    if final == 1: break
    seen.append(str(numbers))
    
print("The same redistribution has been seen at the ",count,"th cycle")
print("There are ",distance, " cycles in infinite loop")

file.close()


