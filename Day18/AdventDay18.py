from collections import Counter

INPUTVAL = '...^^^^^..^...^...^^^^^^...^.^^^.^.^.^^.^^^.....^.^^^...^^^^^^.....^.^^...^^^^^...^.^^^.^^......^^^^'
SAFE = '.'
TRAP = '^'

def determineTile(prevRow,index):
	if index - 1 < 0:
		L = SAFE
	else:
		L = prevRow[index - 1]
	if index + 1 >= len(prevRow):
		R = SAFE
	else:
		R = prevRow[index + 1]

	# I drew out the boolean states described in the puzzle, which gave me ~L*~C*R + ~L*C*R + L*~C*~R + L*C*~R
	# After doing some simplification, we end up with (L * ~R + R * ~L) Which leads us to...
	if L != R:
		return TRAP
	else:
		return SAFE

def getSafeSquares(inputval,totalNumRows):
	#Gets the total number of safe squares
	safeSquares = Counter(inputval)[SAFE]
	prevRow = inputval
	currRow = ''

	for i in range(totalNumRows-1):
		for j in range(len(prevRow)):
			currRow += determineTile(prevRow,j)
		safeSquares += Counter(currRow)[SAFE]
		prevRow = currRow
		currRow = ''
	return safeSquares

print('Part 1: ', getSafeSquares(INPUTVAL,40))

print('Part 2: ', getSafeSquares(INPUTVAL,400000))