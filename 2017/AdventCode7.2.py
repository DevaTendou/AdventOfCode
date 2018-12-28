#Advent of Code 7.2.

file = open("C:\\Users\\devatendou\\Desktop\\AdventCode2017\\AdventCode7.txt", 'r')

info = ["".join([c for c in line if c not in "()->,\n"]).split() for line in file]

#Cast to int all the weights
#info = [ i[:1]+[int(i[1])]+i[2:] for i in info]


lists = [[i[0]] + [i[2:]] for i in info if len(i) > 2]

#ID and its weights
weightsID = [[i[0]] + [int(i[1])] for i in info]
#print(weightsID)
'''tree = []
for l in lists:
    for i in lists:
        if l[0] in i[1]:
            tree.append(l[0])
            break'''
numbers = []
for l in lists:
    for e in l[1]:
        for w in weightsID:
            if w[0] == e:
                numbers.append(w[1])
                break
        

print(set(numbers))




file.close()
