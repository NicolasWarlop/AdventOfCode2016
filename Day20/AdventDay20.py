import re

MAXIP = 4294967295
blacklist = []

def getFirstIP(blacklist):
	#Find the lowest upper bound that is not overlapped
	minIP = 0
	blacklist.sort()
	for elem in blacklist:
		if minIP >= elem[0] and minIP <= elem[1]:
			minIP = elem[1] + 1
	return minIP

def getIPCount(blacklist):
	#Part 2: validate whether or not an IP is within bounds, We have to test IPs from 0 - MAXIP
	total = 0
	ip = 0
	found = False

	while ip <= MAXIP:
		for elem in blacklist:
			if ip >= elem[0] and ip <= elem[1]:
				#We found an IP which is between bounds
				#set IP to upper bound, since we can't take any of the other ones.
				ip = elem[1] + 1
				found = True
		#if we make it here, we found a valid IP
		if not found:
			total += 1
			ip += 1
		found = False
	return total

f = open('AdventDay20Input.txt', 'r')
for line in f:
	#get the upper and lower bounds
	lower, upper = re.search(r"(\d+)-(\d+)", line).groups()
	blacklist.append((int(lower),int(upper)))

print("Part 1:",getFirstIP(blacklist))
print("Part 2:", getIPCount(blacklist))