# Reverse a list

def rev_list(l):
	rev_l = list()
	for i in range(len(l)-1,-1,-1):
		rev_l.append(l[i])
	return rev_l

print(rev_list([2,321,3,43,5,776,9]))
