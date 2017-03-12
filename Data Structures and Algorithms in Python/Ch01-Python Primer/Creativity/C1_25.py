def rem_punctuation(s):
	ans = ''
	for let in s:
		if ord(let.lower()) in range(97,122) or let == ' ':
			ans += let
	return ans

print(rem_punctuation("Let's try, Mike."))