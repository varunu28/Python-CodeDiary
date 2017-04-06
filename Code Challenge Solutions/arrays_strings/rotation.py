class Rotation(object):

    def is_substring(self, s1, s2):
        # TODO: Implement me
        if (s1 is None or s2 is None) or ((s1 == "" and s2 != "") or (s2 == "" and s1 != "")):
        	return False
        elif len(s1) != len(s2):
        	return False
        else:
        	return sorted(list(s1)) == sorted(list(s2))	

    def is_rotation(self, s1, s2):
        # TODO: Implement me
        # Call is_substring only once
        return self.is_substring(s1, s2)

# %load test_rotation.py
from nose.tools import assert_equal


class TestRotation(object):

    def test_rotation(self):
        rotation = Rotation()
        assert_equal(rotation.is_rotation('o', 'oo'), False)
        assert_equal(rotation.is_rotation(None, 'foo'), False)
        assert_equal(rotation.is_rotation('', 'foo'), False)
        assert_equal(rotation.is_rotation('', ''), True)
        assert_equal(rotation.is_rotation('foobarbaz', 'barbazfoo'), True)
        print('Success: test_rotation')


def main():
    test = TestRotation()
    test.test_rotation()


if __name__ == '__main__':
    main()