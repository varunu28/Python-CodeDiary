class ReverseString(object):

    def reverse(self, chars):
        # TODO: Implement me
        if chars is None or len(chars) == 0:
        	return chars
        else:
        	size = len(chars)
	        for i in range(size // 2):
	            chars[i], chars[size - 1 - i] = \
	                chars[size - 1 - i], chars[i]
	        return chars

# %load test_reverse_string.py
from nose.tools import assert_equal


class TestReverse(object):

    def test_reverse(self, func):
        assert_equal(func(None), None)
        assert_equal(func(['']), [''])
        assert_equal(func(
            ['f', 'o', 'o', ' ', 'b', 'a', 'r']),
            ['r', 'a', 'b', ' ', 'o', 'o', 'f'])
        print('Success: test_reverse')

    def test_reverse_inplace(self, func):
        target_list = ['f', 'o', 'o', ' ', 'b', 'a', 'r']
        func(target_list)
        assert_equal(target_list, ['r', 'a', 'b', ' ', 'o', 'o', 'f'])
        print('Success: test_reverse_inplace')


def main():
    test = TestReverse()
    reverse_string = ReverseString()
    test.test_reverse(reverse_string.reverse)
    test.test_reverse_inplace(reverse_string.reverse)


if __name__ == '__main__':
    main()