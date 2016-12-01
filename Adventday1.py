def getDirection(currentDirection, instruction):
	"""gets the direction we will be moving in, based off the current direction"""

	coordinateMap = ['N','E','S','W']
	currentIndex = coordinateMap.index(currentDirection) #get the current direction's index


	if instruction[0] == 'R':
		currentIndex = (currentIndex + 1) % len(coordinateMap) #modulo used to keep the list circular
	elif instruction[0] == 'L':
		currentIndex = (currentIndex - 1) % len(coordinateMap) #modulo used to keep the list circular

	return coordinateMap[currentIndex]

coordinates = [0,0,'N']
exampleInst= ['R4', 'R3', 'L3', 'L2', 'L1', 'R1', 'L1', 'R2', 'R3', 'L5', 'L5', 'R4', 'L4', 'R2', 'R4', 'L3', 'R3', 'L3', 'R3', 'R4', 'R2', 'L1', 'R2', 'L3', 'L2', 'L1', 'R3', 'R5', 'L1', 'L4', 'R2', 'L4', 'R3', 'R1', 'R2', 'L5', 'R2', 'L189', 'R5', 'L5', 'R52', 'R3', 'L1', 'R4', 'R5', 'R1', 'R4', 'L1', 'L3', 'R2', 'L2', 'L3', 'R4', 'R3', 'L2', 'L5', 'R4', 'R5', 'L2', 'R2', 'L1', 'L3', 'R3', 'L4', 'R4', 'R5', 'L1', 'L1', 'R3', 'L5', 'L2', 'R76', 'R2', 'R2', 'L1', 'L3', 'R189', 'L3', 'L4', 'L1', 'L3', 'R5', 'R4', 'L1', 'R1', 'L1', 'L1', 'R2', 'L4', 'R2', 'L5', 'L5', 'L5', 'R2', 'L4', 'L5', 'R4', 'R4', 'R5', 'L5', 'R3', 'L1', 'L3', 'L1', 'L1', 'L3', 'L4', 'R5', 'L3', 'R5', 'R3', 'R3', 'L5', 'L5', 'R3', 'R4', 'L3', 'R3', 'R1', 'R3', 'R2', 'R2', 'L1', 'R1', 'L3', 'L3', 'L3', 'L1', 'R2', 'L1', 'R4', 'R4', 'L1', 'L1', 'R3', 'R3', 'R4', 'R1', 'L5', 'L2', 'R2', 'R3', 'R2', 'L3', 'R4', 'L5', 'R1', 'R4', 'R5', 'R4', 'L4', 'R1', 'L3', 'R1', 'R3', 'L2', 'L3', 'R1', 'L2', 'R3', 'L3', 'L1', 'L3', 'R4', 'L4', 'L5', 'R3', 'R5', 'R4', 'R1', 'L2', 'R3', 'R5', 'L5', 'L4', 'L1', 'L1']

for x in exampleInst:
	coordinates[2] = getDirection(coordinates[2], x)

	if coordinates[2] == 'N': #positive y
		coordinates[1] += int(x[1:])
	elif coordinates[2] == 'S': #negative y
		coordinates[1] -= int(x[1:])
	elif coordinates[2] == 'E': #positive x
		coordinates[0] += int(x[1:])
	elif coordinates[2] == 'W': #positive x
		coordinates[0] -= int(x[1:])
	print(coordinates[0],coordinates[1],coordinates[2])

#The taxicab geometry is equal to the sum of the absolute value of these coordinates (since our initial coordinate was 0,0)
print("The final distance is: " + str(abs(coordinates[0]) + abs(coordinates[1])))