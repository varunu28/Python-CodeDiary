# Changes the actual array after string based indexing is followed

def change_num_param(l, fact):
	for i in range(len(l)):
		l[i] *= fact

l = [1,2,3,4]
print(l)
change_num_param(l, 4)
print(l)
