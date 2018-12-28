#Advent of Code 1.1

file = open("c:\\users\\devatendou\\Desktop\\AdventCode2017\\AdventCode1.txt", 'rb')

numbers = [[int(chr(char)) for char in line] for line in file]
numbers = numbers[0]

counter = 0
for n in range(-1, len(numbers) - 1):
    if numbers[n] == numbers[n+1]:
        counter += numbers[n]

print(counter)
file.close()
