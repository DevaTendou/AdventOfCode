#Advent of Code 10 part 1

file = open("C:\\Users\\devatendou\Desktop\\AdventCode2017\\AdventCode10.txt", 'r')

#length = [int(i) for i in file.read().split(',')]
#numbers = list(range(256))
numbers = [0, 1, 2, 3, 4]
length = [3, 4, 1, 5]

skip, pos = 0, 0
for l in length:
    if l == len(numbers):
        select = numbers[pos:] + numbers[:(pos+l)%len(numbers)]
        select.reverse()
        numbers = select[pos:] + select[:(pos+l)%len(numbers)]
    elif (pos + l) >= len(numbers):
        select = numbers[pos:] + numbers[:(pos+l)%len(numbers)]
        select.reverse()
        numbers = select[len(numbers)-pos:] + numbers[(pos+l)%len(numbers):pos] + select[:len(numbers)-pos]
    else:
        select = numbers[pos:l]
        select.reverse()
        numbers = numbers[:pos] + select[pos:pos+l] + numbers[pos+l:]
    pos = (skip + l)%len(numbers)
    skip += 1
    print(numbers)


    



file.close()
