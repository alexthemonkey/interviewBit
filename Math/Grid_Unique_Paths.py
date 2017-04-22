"""
Grid Unique Paths
https://www.interviewbit.com/problems/grid-unique-paths/


A robot is located at the top-left corner of an A x B grid.
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.


How many possible unique paths are there?

Note: A and B will be such that the resulting answer fits in a 32 bit signed integer.

Example :

Input : A = 2, B = 2
Output : 2

2 possible routes : (0, 0) -> (0, 1) -> (1, 1) 
              OR  : (0, 0) -> (1, 0) -> (1, 1)
See Expected Output

"""

"""
	dp[i][j] stands for how many ways to get to position (i, j). Then,
	 dp[i][j] = dp[i-1][j] (from up) + dp[i][j-1] (from left)
"""


class Solution(object):
	# @param A : integer
	# @param B : integer
	# @return an integer
	def uniquePaths(self, A, B):
		if A * B == 0:
			return 0

		dp = [[1] * B for _ in xrange(A)]
		for i in xrange(1, A):
			for j in xrange(1, B):
				dp[i][j] = dp[i][j-1] + dp[i-1][j]

		return dp[A-1][B-1]