import itertools
def swapPosition(x, y, string):
	#Swaps the character at index x with the character at index y
	string = list(string)
	temp1, temp2 = string[x],string[y]
	string[y] = temp1
	string[x] = temp2
	return ''.join(string)

def swapLetter(x, y, string):
	#Swaps the character x with the character y
	string = swapPosition(string.find(x),string.find(y),string)
	return string

def rotate(steps, direction, string):
	#rotate left or right by n steps
	steps = steps % len(string)
	if direction == 'left':
		return string[steps:] + string[:steps]
	elif direction =='right':
		return string[-steps:] + string[:-steps]

def rotateBasedOnPos(letter, string):
	#rotate right by 1 + index of letter. If index greater than 4, add one additional step
	rotateBy = string.find(letter)
	if rotateBy >= 4:
		rotateBy += 1
	rotateBy += 1
	return rotate(rotateBy,'right', string)

def rotateBackBasedOnPos(letter, string):
	#this command negates the rotateBasedOnPos for pt2.
	#Based off the character position initially, we can calulate where it ends up
	# char At | rotate right by | New position: | Inverse Function
	#   0     |        1        |      1        | Rotate right 7
	#   1     |        2        |      3        | Rotate right 6
	#   2     |        3        |      5        | Rotate right 5
	#   3     |        4        |      7        | Rotate right 3  
	#   4     |        6        |      10%8 = 2 | Rotate right 2
	#   5     |        7        |      12%8 = 4 | Rotate right 1
	#   6     |      8%8 =0     |      14%8 = 6 | Rotate right 0 
	#   7     |      9%8 =1     |      16%8 = 0 | Rotate right 7
	lookup = {0:7, 1:7, 2:2, 3:6, 4:1, 5:5, 6:0, 7:4}

	rotateBy = string.find(letter)

	return rotate(lookup[rotateBy],'right', string)

def reverse(x, y, string):
	#reverse the substring defined by x,y (inclusively)
	return string[:x] + string[x:y+1][::-1] + string[y+1:]

def move(x,y, string):
	#move character at position x such that it ends up at index y
	string = list(string)
	charToMove = string.pop(x)
	string = string[:y] + list(charToMove) + string[y:]
	return ''.join(string)

def solvePt1(scrambleString):
	f = open('AdventDay21Input.txt', 'r')

	for lines in f:
		instr = lines.split()
		
		if instr[0] == 'swap':
			if instr[1] == 'position':
				scrambleString = swapPosition(int(instr[2]),int(instr[5]),scrambleString)
			elif instr[1] == 'letter':
				scrambleString = swapLetter(instr[2],instr[5],scrambleString)
		elif instr[0] == 'rotate':
			if instr[1] == 'based':
				scrambleString = rotateBasedOnPos(instr[6],scrambleString)
			else:
				scrambleString = rotate(int(instr[2]),instr[1], scrambleString)
		elif instr[0] == 'reverse':
			scrambleString = reverse(int(instr[2]),int(instr[4]), scrambleString)
		elif instr[0] == 'move':
			scrambleString = move(int(instr[2]),int(instr[5]), scrambleString)

	f.close()
	return scrambleString

def solvePt2(scrambleString):
	f = open('AdventDay21Input.txt', 'r')
	allInstr = f.readlines()
	allInstr = [allInstr[i].strip('\n') for i in range(len(allInstr))][::-1]

	for lines in allInstr:
		instr = lines.split()
		
		if instr[0] == 'swap':
			if instr[1] == 'position':
				#the inverse of a swap is a swap back
				scrambleString = swapPosition(int(instr[5]),int(instr[2]),scrambleString)
			elif instr[1] == 'letter':
				#the inverse of a swap is a swap back
				scrambleString = swapLetter(instr[5],instr[2],scrambleString)
		elif instr[0] == 'rotate':
			if instr[1] == 'based':
				scrambleString = rotateBackBasedOnPos(instr[6],scrambleString)
			else:
				scrambleString = rotate(-int(instr[2]),instr[1], scrambleString)
		elif instr[0] == 'reverse':
			scrambleString = reverse(int(instr[2]),int(instr[4]), scrambleString)
		elif instr[0] == 'move':
			scrambleString = move(int(instr[5]),int(instr[2]), scrambleString)

	f.close()
	return scrambleString

print('part 1:', solvePt1('abcdefgh'))
print('part 2:', solvePt2('fbgdceah'))