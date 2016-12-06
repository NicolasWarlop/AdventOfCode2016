#Calling command: python Adventday6.py AdventDay6Input.txt
import sys
from collections import Counter

# Most common logic taken from http://stackoverflow.com/questions/1518522/python-most-common-element-in-a-list
# Explanation can be found here: https://docs.python.org/3.1/library/collections.html#collections.Counter
def mostCommon(message_list):
    data = Counter(message_list)
    return data.most_common(1)[0][0]

def leastCommon(message_list):
    data = Counter(message_list)
    return data.most_common()[:-2:-1][0][0]

f = open(sys.argv[1], 'r')

message = f.readlines()
#Truncate the newline characters
message = [list(x.replace('\n','')) for x in message]

# Let's write out our transpose code
# We have a 8x546 matrix that we want to transpose (to 546x8)
# for x in 8:
#    #take each of the 546 characters in column x
#	 for y in 546:
#		transposed_row += character at [x,y]
#    transposed_matrix += transposed_row
#    clear transposed row
# We can translate this to a comprehension: 
# for x in range(len(message[0])) # our x values
# for y in message) # our y values
# [y[x]] #element from each column, appended into a list
# [y[x] for y in message for x in range(len(message[0]))]

message_tranpose = [list(y[x] for y in message) for x in range(len(message[0]))]

decoded = ''
for i in range(len(message_tranpose)):
	decoded += mostCommon(message_tranpose[i])
print("Part 1 answer: " + decoded)

#Part 2:
decoded = ''
for i in range(len(message_tranpose)):
	decoded += leastCommon(message_tranpose[i])
print("Part 2 answer: " + decoded)