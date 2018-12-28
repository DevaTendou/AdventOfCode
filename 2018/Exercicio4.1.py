import re
import time
import datetime
import operator

path = "./Exercicio4.txt"
instructions = []
minutes = [i for i in range(60)]

with open(path) as file:
	for i, line in enumerate(file):
		if line[-1] == "\n":
			line = line[:-1]
		split = re.split('\[|\] ', line)[1:]
		instructions.append(split)

instructions = sorted(instructions, key=lambda x: x[0])
instructions = [ [re.split(':', i[0])[1]] + i[1:] for i in instructions]

guard, time = None, None
sleepT = {}
falls, wakes = 0, 0
for i in instructions:
	instruction = i[1]
	time = int(i[0])
	if "#" in instruction:
		guard = int(re.split('#| ', instruction)[2])
		falls, wakes = 0, 0
		if(guard in sleepT):
			sleepT[guard] += wakes - falls
		else:
			sleepT[guard] = 0
	elif "falls" in instruction:
		falls = time
	else:
		wakes = time

chosenGuard = max(sleepT.items(), key=lambda x: x[1])[0]



		

