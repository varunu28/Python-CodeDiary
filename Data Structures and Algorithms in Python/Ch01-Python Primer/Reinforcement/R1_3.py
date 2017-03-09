def minmax(l):
	min_n, max_n = None, None
	for num in l:
		if min_n is None or num < min_n:
			min_n = num
		if max_n is None or num > max_n:
			max_n = num
	return (min_n,max_n)

print(minmax([2,3,1,24,245,2,-4,1223,6]))