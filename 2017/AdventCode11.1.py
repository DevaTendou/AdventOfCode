#Advent of Code 11 part 1

file = open("C:\\Users\\devatendou\\Desktop\\AdventCode2017\\AdventCode11.txt", 'r')

directions = file.read().split(',')

n , nw, ne, s, sw, se = 0, 0, 0, 0, 0, 0

for d in directions:
    if      d == 'n':   n += 1
    elif    d == 'nw':  nw += 1
    elif    d == 'ne':  ne += 1
    elif    d == 'sw':  sw += 1
    elif    d == 's':   s += 1
    elif    d == 'se':  se += 1

def getDistance(n , nw, ne, s, sw, se):
    n = abs(n - s)
    ne = abs(ne - sw)
    nw = abs(nw - se)

    steps = n + abs(ne - nw)
    if ne > nw: return steps + nw
    else:       return steps + ne

steps = getDistance(n , nw, ne, s, sw, se)

print(steps)

file.close()
