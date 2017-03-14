def get_less_than2(n):
	c = 0
	while n >= 2:
		n = n//2
		c += 1
	return c

print(get_less_than2(18)) 
print(get_less_than2(1))