def odd_sq_sum(n):
	s = 0
	for num in range(n):
		if num%2 == 1:
			s += num**2
	return s

print(odd_sq_sum(5)) # Returns 10