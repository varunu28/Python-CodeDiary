class Stack(object):

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[-1]

def balance_check(s):
	stk = Stack()
	open_brk = ['(','[','{']
	cls_brk = [')',']','}']
	for word in s:
		if word in open_brk:
			stk.push(word)
		else:
			if stk.isEmpty():
				return False
			else:
				t = stk.pop()
				if word != cls_brk[open_brk.index(t)]:
					return False
	return stk.isEmpty()

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestBalanceCheck(object):
    
    def test(self,sol):
        assert_equal(sol('[](){([[[]]])}('),False)
        assert_equal(sol('[{{{(())}}}]((()))'),True)
        assert_equal(sol('[[[]])]'),False)
        print('ALL TEST CASES PASSED')
        
# Run Tests

t = TestBalanceCheck()
t.test(balance_check)