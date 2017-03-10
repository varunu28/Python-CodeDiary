# List comprehension to produce [1, 2, 4, 8, 16, 32, 64, 128, 256]

def list_comp():
	return [2**x for x in range(9)]

print(list_comp()) 