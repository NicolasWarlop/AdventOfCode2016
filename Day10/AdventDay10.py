import re

class Bot:

    def __init__(self, name):
        self.name = name
        self.tokens = []

    def token(self, token):
        self.tokens.append(token)

    def lowToken(self):
        return min(self.tokens)

    def highToken(self):
        return max(self.tokens)

class Instruction:
	"""docstring for ClassName"""
	def __init__(self, lowBot, lowType, highBot, highType):
		self.lowBot = lowBot
		self.lowType = lowType
		self.highBot = highBot
		self.highType = highType
		

valueTracking= {}
instructionTracking = {}
outputVals = {}

f = open('AdventDay10Input.txt', 'r')

for lines in f:
	if lines.startswith('value'):
		botdata = re.search(r"value\s(\d+)\sgoes\sto\sbot\s(\d+)",lines).groups()
		if int(botdata[1]) in valueTracking:
			valueTracking[int(botdata[1])].token(int(botdata[0]))
		else:
			valueTracking[int(botdata[1])] = Bot(botdata[1])
			valueTracking[int(botdata[1])].token(int(botdata[0]))
	elif lines.startswith('bot'):
		botdata = re.search(r"bot\s(\d+)\sgives\slow\sto\s(\w+)\s(\d+)\sand\shigh\sto\s(\w+)\s(\d+)",lines).groups()
		instructionTracking[int(botdata[0])] = Instruction(int(botdata[2]), botdata[1], int(botdata[4]), botdata[3])

while len(valueTracking)>0:
	for val in instructionTracking:
		#For each instruction, validate whether or not the bot instructed has 2 chips. if not, then  skip
		# is the bot in the list?
		if val in valueTracking:
			#does the bot have 2 microchips?
			if len(valueTracking[val].tokens) == 2:
				if valueTracking[val].lowToken()== 17 and valueTracking[val].highToken() == 61:
					print("Bot:",valueTracking[val].name, " microchips: ",valueTracking[val].tokens[0],valueTracking[val].tokens[1])

				#Execute the instr:
				#give the low val
				if instructionTracking[val].lowType == 'bot':
					if int(instructionTracking[val].lowBot) in valueTracking:
						valueTracking[instructionTracking[val].lowBot].token(int(valueTracking[val].lowToken()))
					else:
						valueTracking[int(instructionTracking[val].lowBot)] = Bot(instructionTracking[val].lowBot)
						valueTracking[instructionTracking[val].lowBot].token(int(valueTracking[val].lowToken()))
				else:
					#add the value to the output
					outputVals[int(instructionTracking[val].lowBot)] = Bot(instructionTracking[val].lowBot)
					outputVals[instructionTracking[val].lowBot].token(int(valueTracking[val].lowToken()))
				#give the high val
				if instructionTracking[val].highType == 'bot':
					if int(instructionTracking[val].highBot) in valueTracking:
						valueTracking[instructionTracking[val].highBot].token(int(valueTracking[val].highToken()))
					else:
						valueTracking[int(instructionTracking[val].highBot)] = Bot(instructionTracking[val].highBot)
						valueTracking[instructionTracking[val].highBot].token(int(valueTracking[val].highToken()))
				else:
					#add the value to the output
					outputVals[int(instructionTracking[val].highBot)] = Bot(instructionTracking[val].highBot)
					outputVals[instructionTracking[val].highBot].token(int(valueTracking[val].highToken()))
				#We're done with this bot. We can delete him
				del valueTracking[val]


val = outputVals[0].tokens[0] * outputVals[1].tokens[0] * outputVals[2].tokens[0]
print("Part 2: ",val)
f.close()