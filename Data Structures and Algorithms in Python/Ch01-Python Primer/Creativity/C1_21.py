def read_till_EOF():
	arr = []
	while True:
		inp = input()
		if inp == '':
			break
		else:
			arr.append(inp)
	return arr

arr = read_till_EOF()[::-1]
for line in arr:
	print(line)