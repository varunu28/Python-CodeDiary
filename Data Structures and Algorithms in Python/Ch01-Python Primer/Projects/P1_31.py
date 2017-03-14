def return_change(cost,money_given,valid_change):
	valid_change = sorted(valid_change, reverse=True)
	change = money_given - cost
	change_den = dict()
	for num in valid_change:
		change_den[str(num)] = change//num
		change = change%num
	return change_den

cost = 42
money_given = 54
valid_change = [1,2,5,10]
print(return_change(cost,money_given,valid_change))


