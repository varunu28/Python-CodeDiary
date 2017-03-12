# Print ['a','b'...'z'] without typing it using list comprehension

def all_small_alpha():
	return [chr(97+x) for x in range(26)]

print(all_small_alpha())