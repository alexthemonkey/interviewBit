"""
Sub Matrices With Sum Zero


Given a 2D matrix, find the number non-empty sub matrices, 
such that the sum of the elements inside the sub matrix is equal to 0. 

(note: elements might be negative).
"""

"""
	Let sum[i][j] be the sum of A[0][0] + A[0][1] + ... + A[0][j]
	                           +A[1][0] + A[1][1] + ... + A[1][j]
	                           + ...
	                           +A[i][0] + A[i][1] + ... + A[i][j]
	                           
	then we iterate over each stripe (rows of i, i+1, i+2, ..., j)
	and for each stripe, we count how many sub-matrix sums 0
	
	to sum zero sum in each stripe, we have one observation:
	
	if g[i] + g[i+1] + g[i+2] + ... g[k] = 0
	then:
	we know sum(g[0]..g[k]) is equal to sum(g[0]..g[i-1])
	
	so we maintain a dict of sum and num of zero matrix ends with col pos K in the stripe
	will equal to the num of matrix sums the same previously in the stripe.

"""

from collections import defaultdict


class Solution(object):
	# @param A : tuple of integers
	# @return an integer
	def solve(self, A):
		n = len(A)
		if n == 0:
			return 0

		m = len(A[0])
		_sum = [[0]*(m+1) for _ in xrange(n+1)]
		for i in xrange(1, n+1):
			for j in xrange(1, m+1):
				_sum[i][j] = _sum[i-1][j] + _sum[i][j-1] - _sum[i-1][j-1] + A[i-1][j-1]

		ans = 0
		for i in xrange(1, n+1):
			for j in xrange(i, n+1):
				cnt = defaultdict(int)
				cnt[0] = 1
				for c in xrange(1, m+1):
					s = _sum[j][c] - _sum[i-1][c]
					ans += cnt[s]
					cnt[s] += 1

		return ans
