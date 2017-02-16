def isAnagram(s1, s2):
    s1_l = [x.lower() for x in s1 if x != ' ']
    s2_l = [x.lower() for x in s2 if x != ' ']
    return sorted(s1_l) == sorted(s2_l)
    

from nose.tools import assert_equal

class AnagramTest(object):
    
    def test(self,sol):
        assert_equal(sol('go go go','gggooo'),True)
        assert_equal(sol('abc','cba'),True)
        assert_equal(sol('hi man','hi     man'),True)
        assert_equal(sol('aabbcc','aabbc'),False)
        assert_equal(sol('123','1 2'),False)
        print("ALL TEST CASES PASSED")

# Run Tests
t = AnagramTest()
t.test(isAnagram)
