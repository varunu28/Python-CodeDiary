def dot_prod(a,b):
	c = []
	for i in range(len(a)):
		c.append(a[i]*b[i])
	return c

a = [1,2,3]
b = [4,5,6]
print(dot_prod(a,b))