# Produce a range 8,6,4,2,0,-2,-4,-6,-8

def produce_range():
	r = []
	for i in range(8,-10,-2):
		r.append(i)
	return r

print(produce_range())