import numpy as n
dim = 13    #Matrix's size
Matrix = n.zeros((dim,dim), dtype=n.int)
initX, initY = dim//2, dim//2

Matrix[initY][initX] = 1


def search(y, x):
    value = Matrix[y+1][x+1]+Matrix[y-1][x-1]+Matrix[y+1][x-1]+Matrix[y-1][x]+\
            Matrix[y-1][x+1]+Matrix[y][x+1]+Matrix[y+1][x]+Matrix[y][x-1]
    return value


index = 9 #Range of numbers to be calculated (Warning: may be needed to change 'dim')
step = 1
switch = 1
x, y = initX, initY
while index:
    for i in range(step):
        x += switch
        Matrix[y][x] = search(y, x)
    switch *= -1
    for i in range(step):
        y += switch
        Matrix[y][x] = search(y, x)
    step += 1
    index -= 1

mat = Matrix.tolist()

for y in range(dim):
    strFormat = len(mat[y]) * '|{:^9}|'
    formattedList = strFormat.format(*mat[y])
    print(formattedList)
    
        

