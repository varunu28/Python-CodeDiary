def count_vowel(s):
	c = 0
	for let in s:
		if let in ['a','e','i','o','u']:
			c += 1
	return c

s = 'abcdefghi'
print(count_vowel(s.lower())) # Returns 3