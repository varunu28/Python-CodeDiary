class CompressString(object):

    def compress(self, string):
        # TODO: Implement me
        if string is None or string == "":
        	return string
        else:
        	comp_string = ''
        	c = 1 
        	for i in range(len(string)-1):
        		if string[i] == string[i+1]:
        			c += 1
        		else:
        			comp_string += string[i]
        			if c > 1:
        				comp_string += str(c)
        				c = 1
        	comp_string += string[-1]
        	if c > 1:
        		comp_string += str(c)

        	if len(comp_string) < len(string):
        		return comp_string
        	else:
        		return string

# %load test_compress.py
from nose.tools import assert_equal


class TestCompress(object):

    def test_compress(self, func):
        assert_equal(func(None), None)
        assert_equal(func(''), '')
        assert_equal(func('AABBCC'), 'AABBCC')
        assert_equal(func('AAABCCDDDDE'), 'A3BC2D4E')
        assert_equal(func('BAAACCDDDD'), 'BA3C2D4')
        assert_equal(func('AAABAACCDDDD'), 'A3BA2C2D4')
        print('Success: test_compress')


def main():
    test = TestCompress()
    compress_string = CompressString()
    test.test_compress(compress_string.compress)


if __name__ == '__main__':
    main()