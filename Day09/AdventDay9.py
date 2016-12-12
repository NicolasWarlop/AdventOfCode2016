import re

#Variable declaration
counter=0

f = open('AdventDay9Input.txt', 'r')
encodedString = f.read()
#find the multiples
pattern = re.compile(r"\((\d+)x(\d+)\)")

while pattern.search(encodedString) is not None:
	encPattern = pattern.search(encodedString)
	
	#Start of the string to duplicate
	encSpan = int(encPattern.span()[1])
	stringlist = []
	#length groups()[0] and number of times to multiply groups()[1]
	encGroup = encPattern.groups()
	counter += int(encGroup[0])*int(encGroup[1])
	encodedString = encodedString[encSpan+int(encGroup[0]):]

print("Part 1: ",counter,"Encoded String length: ",len(encodedString))
f.close()
