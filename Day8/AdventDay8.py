#Calling command: python Adventday8.py AdventDay8Input.txt
import sys
import re

def generateKeypad(width, height):
	#Generate and widthxheight keypad
	return [ ['.' for i in range(width)] for j in range(height) ]

def rect(A,B, keypad):
	#Turn on AxB pixels in the top left of the keypad
	for x in range(B):
		for y in range(A):
			keypad[x][y] = '#'
	return keypad

def rotateRow(rowNum, pixels, keypad):
	#Rotate right by pixels amount
	temprow = keypad[rowNum][:]
	
	for i in range(len(keypad[rowNum])):
		keypad[rowNum][(i + pixels) % len(keypad[rowNum])] = temprow[i]
	return keypad

def rotateColumn(colnumNum, pixels, keypad):
	tempCol = [i[colnumNum] for i in keypad]
	for i in range(len(tempCol)):
		keypad[(i + pixels) % len(tempCol)][colnumNum] = tempCol[i]
	return keypad

keypad = generateKeypad(50,6)
linecount = 0

f = open('AdventDay8Input.txt', 'r')
for line in f:
	linecount += 1
	if 'rect' in line:
		#parse out the x,y values
		retInts = re.search(r"(\d+)x(\d+)", line).groups()
		keypad = rect(int(retInts[0]),int(retInts[1]),keypad)
	elif 'rotate row' in line:
		retInts = re.search(r"(\d+)\s+by\s+(\d+)", line).groups()
		keypad = rotateRow(int(retInts[0]),int(retInts[1]),keypad)
	elif 'rotate column' in line:
		retInts = re.search(r"(\d+)\s+by\s+(\d+)", line).groups()
		keypad = rotateColumn(int(retInts[0]),int(retInts[1]),keypad)

counter = 0
for i in range(50):
	for j in range(6):
		if keypad[j][i] == '#':
			counter += 1
print("Part 1: ", counter)

#Part 2
for i in range(len(keypad)):
	print(keypad[i])