import sys
import re



#Variable declaration
sectorIDRe = re.compile('[0-9]+')
encryptedRe = re.compile('^[^0-9]*')
checksumRe = re.compile('\[[a-z]*\]')
charList = list()
sectorIDSum = 0
decodedStr=''


def shiftFunc(character, sectorID):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'

	if character == '-':
		return ' '
	else:
		return alphabet[(alphabet.index(character) + sectorID) % 26]



#Part2: We want to add the lines that are not dummy to a list, and parse through these
nonDecoy = list()

f = open(sys.argv[1], 'r')

for line in f:
	#let's split the encrypted name, the sector id and the checksum
	encryptedStr = encryptedRe.search(line).group().replace('-','') #encrypted string
	sectorID = int(sectorIDRe.search(line).group()) #Sector ID
	checksum = checksumRe.search(line).group() #Checksum with []
	checksum = checksum[1:len(checksum)-1] #Remove the square brackets
	
	#ok, let's get counting
	for i in range(len(encryptedStr)):
		charCount =encryptedStr.count(encryptedStr[i])

		if [encryptedStr[i],charCount] not in charList:
			charList.append([encryptedStr[i],charCount])
	
	#We want to sort the list by 2 criteria: () the count of occurences of a character, and (2) alphabetical order
	charList = sorted(charList, key=lambda x: (-x[1], x[0])) #Useful reference: https://wiki.python.org/moin/HowTo/Sorting

	#Create our checksum
	calcChecksum = charList[0][0] + charList[1][0] + charList[2][0] + charList[3][0] + charList[4][0]
	
	if calcChecksum == checksum:
		sectorIDSum += sectorID
		nonDecoy.append(line) #for Part 2

	charList[:] = [] #Clear the list for the next iteration

print("The sum of the sector IDs for part 1 is:" + str(sectorIDSum) )


for loc in range(len(nonDecoy)):
	#let's split the encrypted name, the sector id and the checksum
	encryptedStr = encryptedRe.search(nonDecoy[loc]).group() #encrypted string
	sectorID = int(sectorIDRe.search(nonDecoy[loc]).group()) #Sector ID

	#We can shift through the list using a modulo (26 shifts = back to the starting point)
	for a in range(len(encryptedStr)):
		decodedStr += shiftFunc(encryptedStr[a], sectorID)

	print(decodedStr,sectorID)
	decodedStr=''
	