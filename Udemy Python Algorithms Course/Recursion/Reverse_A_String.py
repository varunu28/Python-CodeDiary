def reverse(s):
	if len(s) == 0:
		return s
	else:
		return s[-1] + reverse(s[:len(s)-1])

'''
RUN THIS CELL TO TEST YOUR FUNCTION AGAINST SOME TEST CASES
'''

from nose.tools import assert_equal

class TestReverse(object):
    
    def test_rev(self,solution):
        assert_equal(solution('hello'),'olleh')
        assert_equal(solution('hello world'),'dlrow olleh')
        assert_equal(solution('123456789'),'987654321')
        
        print('PASSED ALL TEST CASES!')
        
# Run Tests
test = TestReverse()
test.test_rev(reverse)