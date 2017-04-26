"""
Max Sum Without Adjacent Elements

https://www.interviewbit.com/problems/max-sum-without-adjacent-elements/

Given a 2 * N Grid of numbers, choose numbers such that the sum of the numbers
is maximum and no two chosen numbers are adjacent horizontally, vertically or diagonally, and return it.

Example:

Grid:
	1 2 3 4
	2 3 4 5
so we will choose
3 and 5 so sum will be 3 + 5 = 8


Note that you can choose more than 2 numbers

"""

"""

	let f[i] stands the max sum of first i cols if we choose one value from col i
	let g[i] be the max sum of fist i cols of we don't choose any value from col i
	
	so : f[i] = max(A[0][i], A[1][i]) + g[i-1]  # if we choose i, then we can not choose i-1
	     g[i] = max(g[i-1], f[i-1])
"""

class Solution(object):
	# @param A : list of list of integers
	# @return an integer
	def adjacent(self, A):
		n = len(A[0])
		f = [0] * n
		g = [0] * n

		f[0] = max(A[0][0], A[1][0])

		for i in xrange(1, n):
			f[i] = max(A[0][i], A[1][i]) + g[i-1]
			g[i] = max(f[i-1], g[i-1])

		return max(f[n-1], g[n-1])
