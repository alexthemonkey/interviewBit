"""
Best Time To Buy And Sell Stocks

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. 

You may complete at most 2 transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

"""
	f[i] stands for the max profit of one transaction in A[i], A[i+1], ...., A[n-1]
	g[i] stands for the max profit of one transaction in A[0]. A[1], ....., A[i]
	
	so maxProfit = max{g[i+1]+A[i] | 0 <= i < n-1 }
	and be careful of the boundary.
"""


class Solution(object):
	# @param A : tuple of integers
	# @return an integer
	def maxProfit(self, A):
		n = len(A)
		if n == 0:
			return 0

		f = [0] * n
		max_value = A[n-1]
		for i in xrange(n-2, -1, -1):
			f[i] = max(f[i+1], max_value-A[i])
			max_value = max(max_value, A[i])

		g = [0] * n
		min_value = A[0]
		for i in xrange(1, n):
			g[i] = max(g[i-1], A[i]-min_value)
			min_value = min(min_value, A[i])

		ans = f[0]
		for i in xrange(1, n):
			ans = max(ans, g[i-1]+f[i])
		return ans
