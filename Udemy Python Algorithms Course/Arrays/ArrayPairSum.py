# O(n**2) order solution
def pair_sum1(arr, k):
	ans_arr = []
	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			if arr[i] + arr[j] == k:
				if sorted([arr[i], arr[j]]) not in ans_arr:
					ans_arr.append([arr[i], arr[j]])
	return len(ans_arr)

# O(n) order solution
def pair_sum(arr, k):
	seen = set()
	output = set()

	for num in arr:
		target = k - num
		if target not in seen:
			seen.add(num)
		else:
			output.add((min(num,target), max(num,target)))
	return len(output)

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestPair(object):
    
    def test(self,sol):
        assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
        assert_equal(sol([1,2,3,1],3),1)
        assert_equal(sol([1,3,2,2],4),2)
        print('ALL TEST CASES PASSED')
        
#Run tests
t = TestPair()
t.test(pair_sum)
