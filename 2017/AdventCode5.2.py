file = open("C:\\Users\\devatendou\\Desktop\\AdventCode2017\\AdventCode5.txt", 'r')

#Converts all the elements in the file into a list of ints
array = [int(x) for x in file.read().split('\n')]

steps, index = 0, 0
while True:
    steps += 1
    temp = index + array[index]
    if temp < 0 or temp >= len(array):
        print(steps)
        break
    else:
        temp2 = array[index]
        if temp2 >= 3:  array[index] -= 1
        else:           array[index] += 1
        index += temp2

file.close()
