"""
Distinct Subsequences

https://www.interviewbit.com/problems/distinct-subsequences/

Given two sequences S, T, count number of unique ways in sequence S, 
to form a subsequence that is identical to the sequence T.

Example :
 S = "rabbbit" T = "rabbit" 

Return 3. And the formations as follows:

S1= "ra_bbit" 
S2= "rab_bit" 
S3="rabb_it"

"_" marks the removed character.

"""


class Solution(object):
	# @param S : string
	# @param T : string
	# @return an integer
	def numDistinct(self, S, T):
		n, m = len(S), len(T)
		if n < m:
			return 0

		f = [[0] * (m + 1) for _ in xrange(n + 1)]
		for i in xrange(n + 1):
			f[i][0] = 1

		for i in xrange(1, n + 1):
			for j in xrange(1, min(i + 1, m + 1)):
				if S[i - 1] == T[j - 1]:
					f[i][j] = f[i - 1][j - 1] + f[i - 1][j]
				else:
					f[i][j] = f[i - 1][j]

		return f[n][m]