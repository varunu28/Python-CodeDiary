def is_even(n):
	return int(str(n)[-1]) in [0,2,4,6,8]

print(is_even(4)) # Returns True
print(is_even(3)) # Returns False