# Does not changes the actual array as string based indexing is not followed

def change_num_param(l, fact):
	for num in range(len(l)):
		num *= fact

l = [1,2,3,4]
print(l)
change_num_param(l, 4)
print(l)
