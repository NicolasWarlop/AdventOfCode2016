import re
def cpy(value,register):
	try:
		registers[register] = int(value)
	except ValueError:
		#if we can't convert to int, we are copying to another register
		registers[register] = registers[value]

def inc(register):
	#increment the register by 1
	registers[register] += 1

def dec(register):
	#decrement the register by 1
	registers[register] -= 1

def jnz(value,register):
	#Jump to instr index if register value is not 0
	try:
		register = int(register)
		if register != 0:
			return int(value)
		else:
			return 1
	except ValueError:
		#if we can't convert to int, we are copying to another register
		if int(registers[register]) != 0:
			return int(value)
		else:
			return 1

#All registers are initialized to 0
registers = {
    'a': 0,
    'b': 0,
    'c': 1, #part 2, initialize c as 1
    'd': 0
}

index = 0
f = open('AdventDay12Input.txt', 'r')
instructions = f.readlines()

while index < len(instructions):
	if instructions[index].startswith('cpy'):
		value,register = re.search(r"cpy\s(\w+)\s(\w+)",instructions[index]).groups()
		cpy(value,register)
		index += 1
	elif  instructions[index].startswith('inc'):
		register = re.search(r"inc\s(\w+)",instructions[index]).group(1)
		inc(register)
		index += 1
	elif  instructions[index].startswith('dec'):
		register = re.search(r"dec\s(\w+)",instructions[index]).group(1)
		dec(register)
		index += 1
	elif  instructions[index].startswith('jnz'):
		register,value = re.search(r"jnz\s(\w+)\s(-*\d+)",instructions[index]).groups()
		index += jnz(value,register)
print("Register a value: ",registers['a'])
f.close()