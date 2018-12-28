from functools import reduce as r

path = "./Exercicio5.txt"

message = ""
with open(path) as file:
	message = file.readline()
				
def rreduce(message):
	newMessage = r(lambda x, y: x[:-1]\
					if (len(x) > 0 and x[-1].isupper() and y.islower() and x[-1].lower() == y.lower())\
					else (x[:-1] if len(x) > 0 and x[-1].islower() and y.isupper() and x[-1].lower() == y.lower()\
					else x + y),\
					message)
		
	if len(newMessage) != len(message):
		return rreduce(newMessage)
	else:	
		return message

dict = {}
for i in range(65, 90 + 1):
	c, C = chr(i), chr(i+32)
	newMessage = "".join([l for l in message if l != c and l != C ])
	dict[c] = len(rreduce(newMessage))

print(min(dict.values()))
		

