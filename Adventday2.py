#Calling command: python Adventday2.py AdventDay2Input.txt
import sys

def nextKey(currentKeyX,currentKeyY, instruction, arrayLength, keypadLayout):
	factor=[0,0]

	if instruction == 'U':
		factor = [-1,0]
	elif instruction == 'D':
		factor = [1,0]
	elif instruction == 'L':
		factor = [0,-1]
	elif instruction == 'R':
		factor = [0,1]

	tempX = currentKeyX + factor[0]
	tempY = currentKeyY + factor[1]

	#ensure the keys are in bounds. If not, return the original values
	if tempX >= 0 and tempX <= arrayLength - 1 and tempY >= 0 and tempY <= arrayLength - 1:
		if keypadLayout[tempX][tempY] != 'X':
			return [tempX,tempY]
		else:
			return [currentKeyX,currentKeyY]
	else:
		return [currentKeyX,currentKeyY]


keypad = [[1,2,3],[4,5,6],[7,8,9]]
position = [1,1]
passcode = ''

f = open(sys.argv[1], 'r')
for line in f:
	for inst in range(len(line)):
		position = nextKey(position[0],position[1],line[inst],len(keypad[0]),keypad)
	passcode += str(keypad[position[0]][position[1]])

#Return the passcode
print("For part 1, the code is:" + passcode)


# Part 2: implement the Keypad as a 5x5. An additional constraint needs to be added to the nextKey logic: If the character it moves to is ''X'', then return current keys
keypad2 = [['X','X',1,'X','X'],['X',2,3,4,'X'],[5,6,7,8,9],['X','A','B','C','X'],['X','X','D','X','X']]
position = [2,0] #position of the 5 on the keypad
passcode = ''

f = open(sys.argv[1], 'r')
for line in f:
	for inst in range(len(line)):
		position = nextKey(position[0],position[1],line[inst],len(keypad2[0]),keypad2)
	passcode += str(keypad2[position[0]][position[1]])

#Return the passcode
print("For part 2, the code is:" + passcode)