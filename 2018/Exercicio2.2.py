from Levenshtein import distance

path = "./Exercicio2.txt"

strings = []

with open(path) as file:
	for line in file:
		strings += [line]

for i, string in enumerate(strings):
	for str in strings[i:]:
		if distance(string, str) is 1:
			print(string, str)
			break