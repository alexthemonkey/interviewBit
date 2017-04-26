"""
Edit Distance
https://www.interviewbit.com/problems/edit-distance/


Given two words A and B, find the minimum number of steps required to convert A to B. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example : 
edit distance between
"Anshuman" and "Antihuman" is 2.

Operation 1: Replace s with t.
Operation 2: Insert i.


"""


class Solution(object):
	# @param A : string
	# @param B : string
	# @return an integer
	def minDistance(self, A, B):
		m = len(A)
		n = len(B)

		if m * n == 0:
			return max(m, n)
		inf = m + n

		f = [[inf] * (n + 1) for _ in xrange(m + 1)]
		for x in xrange(m + 1):
			f[x][0] = x
		for x in xrange(n + 1):
			f[0][x] = x

		for i in xrange(1, m + 1):
			for j in xrange(1, n + 1):
				if A[i - 1] == B[j - 1]:
					f[i][j] = f[i - 1][j - 1]
				else:
					f[i][j] = min(f[i][j - 1], f[i - 1][j], f[i - 1][j - 1]) + 1

		return f[m][n]
