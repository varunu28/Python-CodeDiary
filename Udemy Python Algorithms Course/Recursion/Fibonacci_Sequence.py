# Recursive Solution
def fib_rec(n):
	if n == 0 or n == 1:
		return n
	else:
		return fib_rec(n-1) + fib_rec(n-2)


# Instantiate Cache information for Dynamic Programming Solution
n = 10
cache = [None] * (n + 1)
def fib_dyn(n):
	if n == 0 or n == 1:
		return n
	if cache[n] != None:
		return cache[n]
	cache[n] = fib_dyn(n-1) + fib_dyn(n-2)
	return cache[n]


# Iterative Solution
def fib_iter(n):
	a, b = 0, 1 
	while n > 0:
		a, b = b, a+b
		n -= 1
	return a


"""
UNCOMMENT THE CODE AT THE BOTTOM OF THIS CELL TO SELECT WHICH SOLUTIONS TO TEST.
THEN RUN THE CELL.
"""

from nose.tools import assert_equal

class TestFib(object):
    
    def test(self,solution):
        assert_equal(solution(10),55)
        assert_equal(solution(1),1)
        assert_equal(solution(23),28657)
        print('Passed all tests.')
# UNCOMMENT FOR CORRESPONDING FUNCTION
t = TestFib()

#t.test(fib_rec)
t.test(fib_dyn) # Note, will need to reset cache size for each test!
#t.test(fib_iter)