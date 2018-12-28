path = "./Exercicio2.txt"

strings = []
repeats = [ 0 for x in range(26)]

with open(path) as file:
	for line in file:
		strings += ["".join(sorted(line))]
		
for string in strings:
	counterLst = []
	for s in set(string):
		count = string.count(s)
		if count > 1:
			counterLst += [count]
	if len(counterLst):
		for i in set(counterLst):
			repeats[i] += 1
			
print([x for x in repeats if x != 0])
			
			
			