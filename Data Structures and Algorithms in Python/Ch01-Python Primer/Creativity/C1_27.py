def factors(n):
	k = 1
	while k*k < n:
		if n%k == 0:
			yield min(k,n//k)
			yield max(k,n//k)
		k += 1
	if k*k == n:
		yield k


facts = factors(100)

print(next(facts)) 

