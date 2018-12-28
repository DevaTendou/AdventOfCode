#Advent of Code 12 part 1

file = open("C:\\users\\devatendou\\Desktop\\AdventCode2017\\AdventCode12.txt", 'r')

connects = [["".join(c for c in line.strip() if c not in "<->,")] for line in file]
connects = [[int(c) for c in con[0].split()] for con in connects]
seen = [0]
index = 0
def func(lista, conns, index):
    temp = lista
    t = len(temp)
    for i in range(index, len(lista)):
        temp += conns[lista[i]][1:]
        temp = list(set(temp))
    index += len(temp) - t
    if len(temp) == t :     return temp
    else:                   return func(temp, conns, index)

print(func(seen, connects, index))
    
    


    
    
    
    
    



file.close()
