path = "./Exercicio1.txt"
sum = 0
done = False
numbers, seen = [], []

with open(path) as file:
	for line in file:
		numbers += [int(line)]
	
while not done:
	for i in numbers:
		sum += i
		if sum not in seen:
			seen += [sum]
		else:
			done = True
			break
	
print(sum)