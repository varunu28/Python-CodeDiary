def find_odd_mul_pair(l):
	first_num = None 
	for num in l:
		if num%2 == 1:
			if first_num is None:
				first_num = num
			elif num != first_num:
				return True
	return False

print(find_odd_mul_pair([2,3,4,6]))

