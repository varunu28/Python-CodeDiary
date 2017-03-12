def all_unique(l):
	return len(l) == len(set(l))

print(all_unique([1,2,3,4])) # Returns True
print(all_unique([1,2,3,4,4])) # Returns False
