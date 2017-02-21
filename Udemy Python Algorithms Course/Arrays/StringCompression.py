def compress(s):
	set_s = set(list(s))
	d = dict()
	for letter in set_s:
		d[letter] = s.count(letter)
	ans = ''
	for item in d:
		ans += item + str(d[item])
	return ans

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print('ALL TEST CASES PASSED')

# Run Tests
t = TestCompress()
t.test(compress)