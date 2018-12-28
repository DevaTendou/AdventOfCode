startA, factorA = 634, 16807
startB, factorB = 301, 48271

def mod(x, factor):
    return (x*factor) % 2147483647

judgeCount = 0
newA = startA
newB = startB
for i in range(40_000_000):
    newA = mod(newA, factorA)
    newB = mod(newB, factorB)
    if (newA & 0xFFFF) == (newB & 0xFFFF):
        judgeCount += 1
        print("Iteration:", i)

print(judgeCount)
