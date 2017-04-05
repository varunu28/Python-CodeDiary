class Permutations(object):

    def is_permutation(self, str1, str2):
        # TODO: Implement me
        if (str1 == '' or str2 == '') or (str1 is None or str2 is None):
        	return False
        elif sorted(list(str1)) == sorted(list(str2)):
        	return True
        return False


# %load test_permutation_solution.py
from nose.tools import assert_equal


class TestPermutation(object):

    def test_permutation(self, func):
        assert_equal(func(None, 'foo'), False)
        assert_equal(func('', 'foo'), False)
        assert_equal(func('Nib', 'bin'), False)
        assert_equal(func('act', 'cat'), True)
        assert_equal(func('a ct', 'ca t'), True)
        print('Success: test_permutation')


def main():
    test = TestPermutation()
    permutations = Permutations()
    test.test_permutation(permutations.is_permutation)
    try:
        permutations_alt = PermutationsAlt()
        test.test_permutation(permutations_alt.is_permutation)
    except NameError:
        # Alternate solutions are only defined
        # in the solutions file
        pass


if __name__ == '__main__':
    main()