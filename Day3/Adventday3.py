import sys
import re

def validTriangle(sideList):
	sideList = [int(i) for i in sideList] #convert the list to int so that we can sort it correctly
	sideList.sort()

	if (sideList[0] + sideList[1]) > sideList[2]:
		possible = 1
	else:
		possible = 0
	return possible

#Variable declaration
possibleTriangles = 0

f = open(sys.argv[1], 'r')

for line in f:
	sides = re.split(" +", line.strip()) #using a regex to deal with irregular spacing
	possibleTriangles += validTriangle(sides)

print("The number of possible triangles is:" + str(possibleTriangles))

# Part 2: Vertical reading of the lines
# We will have 3 triangle lists, and a counter (from 0-2). When the counter hits maxcount, calculate the possibility for each triangle, and reset the counter

#Variable declaration
COUNTER_MAX = 2 #constant
possibleTriangles = 0
countTri = 0
triangle1 = [None]*3
triangle2 = [None]*3
triangle3 = [None]*3

f = open(sys.argv[1], 'r')

for line in f:
	if countTri > COUNTER_MAX:
		print(triangle1)
		possibleTriangles += validTriangle(triangle1)
		possibleTriangles += validTriangle(triangle2)
		possibleTriangles += validTriangle(triangle3)

		sides = re.split(" +", line.strip()) #using a regex to deal with irregular spacing

		triangle1[0] = sides[0]
		triangle2[0] = sides[1]
		triangle3[0] = sides[2]
		countTri = 1
	else:
		sides = re.split(" +", line.strip()) #using a regex to deal with irregular spacing

		triangle1[countTri] = sides[0]
		triangle2[countTri] = sides[1]
		triangle3[countTri] = sides[2]
		countTri += 1
#We want to capture the last triangle. This is not super neat, and would need to be worked on to be included in the for loop
print(triangle1)
possibleTriangles += validTriangle(triangle1)
possibleTriangles += validTriangle(triangle2)
possibleTriangles += validTriangle(triangle3)
print("The number of possible triangles in part 2 is:" + str(possibleTriangles))