class Solution(object):

    def find_diff(self, str1, str2):
        if str1 is None or str2 is None:
            raise TypeError('str1 or str2 cannot be None')
        seen = {}
        for char in str1:
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1
        for char in str2:
            try:
                seen[char] -= 1
            except KeyError:
                return char
            if seen[char] < 0:
                return char
        return None

# %load test_str_diff.py
from nose.tools import assert_equal, assert_raises


class TestFindDiff(object):

    def test_find_diff(self):
        solution = Solution()
        assert_raises(TypeError, solution.find_diff, None)
        assert_equal(solution.find_diff('abcd', 'abcde'), 'e')
        assert_equal(solution.find_diff('aaabbcdd', 'abdbacade'), 'e')
        print('Success: test_find_diff')


def main():
    test = TestFindDiff()
    test.test_find_diff()


if __name__ == '__main__':
    main()