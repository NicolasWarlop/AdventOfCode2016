#Calling command: python Adventday7.py AdventDay7Input.txt
import sys
import re

TLSCounter = 0

f = open(sys.argv[1], 'r')
for line in f:
	#Cannot have a palindrome in between square brackets
	if re.search(r"\[[a-z]*(\w)(\w)\2\1[a-z]*\]", line) is None:
		if re.search(r"(\w)(\w)\2\1", line) is not None: 
			#We have found a palindrome, make sure it's characters differ
			retChars  = re.search(r"(\w)(\w)\2\1", line).groups()
			if retChars[0] != retChars[1]:
				TLSCounter += 1
print("TLS Count part 1: " + str(TLSCounter))
f.close()

#Part 2: 
hyperList = []
SSLCounter = 0
lineCount = 0
counted = False
lineArray = []

f = open(sys.argv[1], 'r')

for line in f:
	lineCount += 1
	ip7addr = line
	
	#split line between hypernet and non-hypernet segments
	hyperList= re.findall(r"\[[a-z]+\]", ip7addr)
	ip7addr = re.sub(r"\[[a-z]+\]",'-',ip7addr)

	for i in range(len(hyperList)):
		for j in range(len(hyperList[i])-2):
			firstChar = hyperList[i][j]
			secondChar = hyperList[i][j+1]
			thirdChar = hyperList[i][j+2]

			if firstChar == thirdChar and firstChar != secondChar:
				#We found an ABA palindrome. See if BAB exists in the string
				if str(secondChar) + str(firstChar) + str(secondChar) in ip7addr and lineCount not in lineArray:
					SSLCounter += 1
					lineArray.append(lineCount)
	hyperList[:] = []
print("SSL Count part 2: " + str(SSLCounter))