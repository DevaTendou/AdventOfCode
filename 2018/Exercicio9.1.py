players = 476
lastMarble = 71657
board = [0]
boardLength = 1
currentMarble, currentMarblePos, guessMarble = 0, 0, 0
currentPlayer = 1
scores = [0 for x in range(players)]

while(currentMarble != lastMarble):
	currentMarble += 1
	if currentMarble % 23 != 0 or currentMarble == 0:
		boardLength += 1
		guessMarble = currentMarblePos + 2
		if boardLength <= guessMarble:
			currentMarblePos = 1
		else:
			currentMarblePos = guessMarble
		board.insert(currentMarblePos, currentMarble)
		
	else:
		print("CurrentMarble ->", currentMarble)
		currentMarblePos = (currentMarblePos - 7) % boardLength
		boardLength -= 1
		scores[currentPlayer-1] += currentMarble + board.pop(currentMarblePos)
		
	currentPlayer = (currentPlayer % players) + 1
	
print("#Answer# > ", max(scores))
	
		
