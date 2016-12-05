#Calling command: python Adventday5.py
import sys
import hashlib

secretKey = 'ffykfhsq' #given input
counter = 0
password = ''

PASSWORD_LEN = 8

while True:
	currKey = secretKey + str(counter)
	m = hashlib.md5(currKey.encode('utf-8')).hexdigest() #This gets the hexadecimal output of based off the given currKey input

	if(m[:5] == '00000'):
		password = password + m[5]
		if len(password) == PASSWORD_LEN:
			break
		counter += 1
	else:
		counter += 1
print("The password is:" + password)

#Part 2
password2 = ['X','X','X','X','X','X','X','X']
counter = 0

while True:
	currKey = secretKey + str(counter)
	m = hashlib.md5(currKey.encode('utf-8')).hexdigest() #This gets the hexadecimal output of based off the given currKey input

	if(m[:5] == '00000'):
		if 0 <= int(m[5],16) <= 7:
			if password2[int(m[5])] == 'X':
				password2[int(m[5])] = m[6]
				print(password2)
				if 'X' not in password2:
					break
		counter += 1
	else:
		counter += 1
print("The password in part 2 is:" + ''.join(password2))