class Solution(object):

    def two_sum(self, nums=None, target=None):
        if nums is None or target is None:
            raise TypeError('nums or target cannot be None')
        if not nums:
            raise ValueError('nums cannot be empty')
        cache = {}
        for index, num in enumerate(nums):
            cache_target = target - num
            if num in cache:
                return [cache[num], index]
            else:
                cache[cache_target] = index
        return None

from nose.tools import assert_equal, assert_raises


class TestTwoSum(object):

    def test_two_sum(self):
        solution = Solution()
        assert_raises(TypeError, solution.two_sum, None, None)
        assert_raises(ValueError, solution.two_sum, [], 0)
        target = 7
        nums = [1, 3, 2, -7, 5]
        expected = [2, 4]
        assert_equal(solution.two_sum(nums, target), expected)
        print('Success: test_two_sum')


def main():
    test = TestTwoSum()
    test.test_two_sum()


if __name__ == '__main__':
    main()