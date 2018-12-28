path = "./Exercicio1.txt"
sum = 0

with open(path) as file:
	for line in file:
		sum += int(line)
		
print(sum)