file1 = open("c:\\users\\devatendou\\Desktop\\AdventCode2017\\AdventCode4.1.txt", 'r')
file2 = open("c:\\users\\devatendou\\Desktop\\AdventCode2017\\AdventCode4.1.txt", 'r')

def hasDuplicates(lista):
    index = 0
    temp = lista
    for l in lista:
        for t in temp:
            if l == t:  index += 1
            if index == 2: return True
        index = 0
    return False

def isAnagram(lista):
    for i in range(0, len(lista)):
        for j in range(i+1, len(lista)):
            if sorted(lista[i]) == sorted(lista[j]): return True  
    return False
        
def part1(content):
    lista = []
    valid = 0
    for line in content:
        lista = line.split()
        if hasDuplicates(lista) == False:   valid += 1
    content.close()
    return valid

def part2(content):
    lista = []
    valid = 0
    for line in content:
        lista = line.split()
        if isAnagram(lista) == False:   valid += 1
    content.close()
    return valid

print(part1(file1))
print(part2(file2))





