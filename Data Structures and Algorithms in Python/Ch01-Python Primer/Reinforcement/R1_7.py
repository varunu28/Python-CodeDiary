def odd_sq_sum(n):
	return sum([x**2 for x in range(n) if x%2 == 1])

print(odd_sq_sum(5)) # Returns 10