import hashlib
import re

INPUTVAL  = 'jlmsuwbz'  #From the puzzle's instructions

possibleKeys = {}
confirmedKeys = {}
counter = 0

def keyStretch(hashedKey,hashIter):
	#hashes an already hashed key hashIter number of times
	for i in range(hashIter):
		hashedKey = hashlib.md5(hashedKey.encode('utf-8')).hexdigest()
	return hashedKey

while len(confirmedKeys) < 64:
	#remove any keys that are over 1000 integers away from counter
	possibleKeys = {k:v for k,v in possibleKeys.items() if k + 1000 > counter}
    #calculate the new hash
	currKey = INPUTVAL + str(counter)
	m = hashlib.md5(currKey.encode('utf-8')).hexdigest()
	try:
		keyDetermine = re.search(r"(\w)\1\1", m).group(1)*5
		#See if we have matches
		for key in sorted(possibleKeys.keys()):
			if m.find(possibleKeys[key]) > -1:
				confirmedKeys[key] = possibleKeys[key]	
				if len(confirmedKeys) == 64:
					print("Match found for 64th key. Key at", key)
					break
		possibleKeys[counter] = keyDetermine
	except AttributeError:
		pass
	counter += 1

#Part 2:
possibleKeys.clear()
confirmedKeys.clear()
counter = 0

while len(confirmedKeys) < 64:
	#remove any keys that are over 1000 integers away from counter
	possibleKeys = {k:v for k,v in possibleKeys.items() if k + 1000 > counter}
    #calculate the new hash
	currKey = INPUTVAL + str(counter)
	m = hashlib.md5(currKey.encode('utf-8')).hexdigest()
	m = keyStretch(m, 2016)
	try:
		keyDetermine = re.search(r"(\w)\1\1", m).group(1)*5
		#See if we have matches
		for key in sorted(possibleKeys.keys()):
			if m.find(possibleKeys[key]) > -1:
				confirmedKeys[key] = possibleKeys[key]	
				if len(confirmedKeys) == 64:
					print("Part 2. Match found for 64th key. Key at", key)
					break
		possibleKeys[counter] = keyDetermine
	except AttributeError:
		pass
	counter += 1