import re
path = "./Exercicio3.txt"
areas = []  #[x0, y0, x1, y1]
interPoints = 0

interArea = [[' ' for i in range(1000)] for j in range(1000)]

def addToArea(tuple):
	x, y = tuple
	interArea[y][x] = "#"
			
def isInterseption(x1i, y1i, x1f, y1f, x2i, y2i, x2f, y2f):	
	if x1f < x2i or x1i > x2f: 
		return False
	elif y1f < y2i or y1i > y2f: 
		return False
	else: 
		return True
	

with open(path) as file:
	for i, line in enumerate(file):
		if line[-1] == "\n":
			line = line[:-1] 
		str = line.split('@ ')[1]
		split = re.split(',|: |x', str)
		x0, y0, x1, y1 = int(split[0]), int(split[1]), int(split[2]), int(split[3])
		areas.append([x0, y0, x0 + x1 - 1, y0 + y1 - 1])

		
for i, a1 in enumerate(areas):
	x1i, y1i, x1f, y1f = a1[0], a1[1], a1[2], a1[3]
	set1 = [(x, y) for x in range(x1i, x1f + 1) for y in range(y1i, y1f + 1)]
	for a2 in areas[i + 1:]:
		x2i, y2i, x2f, y2f = a2[0], a2[1], a2[2], a2[3]
		
		if not isInterseption(x1i, y1i, x1f, y1f, x2i, y2i, x2f, y2f):
			continue
		
		set2 = [(x, y) for x in range(x2i, x2f + 1) for y in range(y2i, y2f + 1)]

		interSet = set(set1).intersection(set2)	
		for tuple in interSet:
			addToArea(tuple)
		
		
for area in interArea:
	interPoints += area.count("#")

print(interPoints)

with open("./map.txt", "w") as file:
	for i in interArea:
		file.write("".join(i))
