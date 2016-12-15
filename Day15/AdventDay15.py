import re

def calcPos(discNo,discNoPos,discInitPos,time):
	#Calculates the disc's position when the ball reaches it
	return (int(discInitPos) + int(discNo) + int(time)) % int(discNoPos)



f = open('AdventDay15Input.txt', 'r')
instructions = []

for instr in f:
	discNo, discNoPos, discInitPos = re.search(r"Disc #(\w+) has (\w+) positions; at time=0, it is at position (\w+).", instr).groups()
	instructions.append((discNo,discNoPos,discInitPos))
f.close()

time = 0

while True:
	for i in range(len(instructions)):
		if calcPos(instructions[i][0],instructions[i][1],instructions[i][2],time) != 0:
			time += 1
			break
	#If we make it here, position is 0 for all discs
	else:
		print("All discs are aligned at t=", time)
		break

#Part 2:
time =0 

instructions.append(('7','11','0'))

while True:
	for i in range(len(instructions)):
		if calcPos(instructions[i][0],instructions[i][1],instructions[i][2],time) != 0:
			time += 1
			break
	#If we make it here, position is 0 for all discs
	else:
		print("All discs are aligned at t=", time)
		break