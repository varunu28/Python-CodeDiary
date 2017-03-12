import random

def rand_shuffle(l):
	arr = []
	n = len(l)
	for i in range(n):
		while True:
			temp = random.randint(0,n-1)
			if l[temp] not in arr:
				arr.append(l[temp])
				break
	return arr

print(rand_shuffle([1,4,3,2,53,6]))