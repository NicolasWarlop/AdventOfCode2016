from collections import Counter

INPUTVAL  = 1358  #From the puzzle's instructions
ENDNODE = (31,39) #Where we want to end up

def isWall(x,y):
	#Odd number of bits = wall
	val = bin(x*x + 3*x + 2*x*y + y + y *y + INPUTVAL)[2:]
	return Counter(val)['1'] % 2 == 1

def getNeighbours(x,y):
	#Returns the list of neighbours that can be reached from our current node:
	#Cannot go into wall, cannot go to negative number
	adj = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
	retAdj = []

	for i in range(len(adj)):
		if not (isWall(adj[i][0],adj[i][1]) or adj[i][0] < 0  or adj[i][1] < 0):
			retAdj.append(adj[i])
	return retAdj

def minPath(startnode,endnode):
	#Returns the min number of steps
	#Will use BFS alg to compute min path
	#Algorithm based off the logic given in the following lecture:
	#https://www.youtube.com/watch?v=s-CYnVz-uh4&ab_channel=MITOpenCourseWare

	#variable declaration
	level = {startnode:0}
	i = 1
	frontier = [startnode]

	while frontier:
		nextNodes =[]

		for u in frontier:
			for v in getNeighbours(u[0],u[1]):
				if ENDNODE == v:
					#We have found our destination
					print("We have reached node ", ENDNODE, "in ", i, " steps")
					del frontier
					break
				if v not in level:
					#Avoid jumping back and forth from one node to the other
					level[v] = i
					nextNodes.append(v)
		frontier = nextNodes
		i += 1

def minPathSteps(startnode,maxsteps):
	#Same alg as above, but with max steps (for part 2)

	#variable declaration
	level = {startnode:0}
	i = 1
	frontier = [startnode]

	for i in range(maxsteps):
		nextNodes =[]

		for u in frontier:
			for v in getNeighbours(u[0],u[1]):
				if v not in level:
					#Avoid jumping back and forth from one node to the other
					level[v] = i
					nextNodes.append(v)
		frontier = nextNodes
		i += 1
	return len(level)

#Part 1
minPath((1,1),ENDNODE)
#Part 2
print("We can visit ",minPathSteps((1,1),50), " nodes in 50 steps")