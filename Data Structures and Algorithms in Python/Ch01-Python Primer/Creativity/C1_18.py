# Generate a sequence [0, 2, 6, 12, 20, 30, 42, 56, 72, 90] by list comprehension

def list_comp1():
	return [x*(x+1) for x in range(10)]

print(list_comp1())

