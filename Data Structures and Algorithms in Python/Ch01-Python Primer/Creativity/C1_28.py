def p_norm(v,p=2):
	return sum([x**p for x in v])**0.5

print(p_norm([4,3],3))
print(p_norm([4,3]))