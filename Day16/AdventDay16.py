INPUTVAL ='11011110011011101'
DISKLENGTH = 272
DISKLENGTHPT2 = 35651584

def dataFill(initialInput):
	inputCopy = list(''.join(reversed(initialInput)))

	inputCopy = ['x' if x == '1' else 'y' for x in inputCopy]
	inputCopy = ['0' if val == 'x' else '1' for val in inputCopy]
	return initialInput + '0' + ''.join(inputCopy)

def diskFill(initialInput, diskLength):
	retval = initialInput

	while len(retval) < diskLength:
		retval = dataFill(retval)
	return retval[:diskLength]

def calcCheckSum(disk):
	#Calculate the checksum
	i = 0 
	checksum = ''
	while i < len(disk) - 1:
		if disk[i] == disk[i+1]:
			checksum += '1'
		else:
			checksum += '0'
		i += 2
	return checksum

def calcSolution(inputval,diskLength):
	#Fill the disk
	disk = diskFill(inputval,diskLength)

	while len(disk) % 2 != 1:
		disk = calcCheckSum(disk)
	return disk

print("Part 1:", calcSolution(INPUTVAL,DISKLENGTH))
print("Part 2:", calcSolution(INPUTVAL,DISKLENGTHPT2))