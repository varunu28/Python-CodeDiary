# Recurisve Solution. (SLOW)
def rec_coin(target,coins):
	min_coins = target
	if target in coins:
		return 1
	else:
		for i in [c for c in coins if c <= target]:
			num_coins = 1 + rec_coin(target-i, coins)
			if num_coins < min_coins:
				min_coins = num_coins
	return min_coins

# Dynamic Programming
def rec_coin_dynam(target,coins,known_results):
	min_coins = target
	if target in coins:
		known_results[target] = 1
		return 1
	elif known_results[target] > 0:
		return known_results[target]
	else:
		for i in [c for c in coins if c <= target]:
			num_coins = 1 + rec_coin_dynam(target-i,coins,known_results)
			if num_coins < min_coins:
				min_coins = num_coins
				known_results[target] = min_coins
	return min_coins

"""
RUN THIS CELL TO TEST YOUR FUNCTION.
NOTE: NON-DYNAMIC FUNCTIONS WILL TAKE A LONG TIME TO TEST. IF YOU BELIEVE YOU HAVE A SOLUTION 
      GO CHECK THE SOLUTION NOTEBOOK INSTEAD OF RUNNING THIS!
"""

from nose.tools import assert_equal

class TestCoins(object):
    
    def check(self,solution):
        coins = [1,5,10,25]
        assert_equal(solution(45,coins),3)
        assert_equal(solution(23,coins),5)
        assert_equal(solution(74,coins),8)
        print('Passed all tests.')
# Run Test

test = TestCoins()
test.check(rec_coin_dynam)