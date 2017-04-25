"""
Coin Sum Infinite

https://www.interviewbit.com/problems/coin-sum-infinite/

You are given a set of coins S. In how many ways can you make sum N assuming you have infinite amount of each coin in the set.

Note : Coins in set S will be unique. Expected space complexity of this problem is O(N).

Example :

Input : 
	S = [1, 2, 3] 
	N = 4

Return : 4

Explanation : The 4 possible ways are
{1, 1, 1, 1}
{1, 1, 2}
{2, 2}
{1, 3}	
Note that the answer can overflow. So, give us the answer % 1000007

"""

"""
	let f[i][j] be the num of ways to form 'j' with S[0] S[1] S[2] ... S[i]
	
	so: f[i][j] = f[i-1][j] + f[i-1][j-S[i]] + f[i-1][j-2*S[i]] + ... f[i-1][j-k*S[i]]
	while f[i][j-S[i]] = f[i-1][j-S[i]] + f[i-1][j-2*S[i]] ... + f[i-1][j-k*S[i]]
	
	combining above together:  f[i][j] = f[i-1][j] + f[i][j-S[i]]
	
	so the time complexity is O(len(S)*N)
	
	But the space is also O(len(S)*N) to improve, we can see that f[i][x] only cares about f[i-1][..]
	but has nothing todo with f[i-2].. f[i-3][..]  
	so a rolling array can be applied here to save space.
"""


# no rolling array
class Solution0(object):
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def coinchange2(self, A, B):
		if not A and not B:
			return 1

		if not A:
			return 0

		MOD = 1000007
		n = len(A)
		f = [[0] * (B+1) for _ in xrange(n+1)]

		f[0][0] = 1
		for i in xrange(1, n+1):
			f[i][0] = 1
			for j in xrange(1, B+1):
				f[i][j] = f[i - 1][j]
				if j >= A[i-1]:
					f[i][j] += f[i][j-A[i-1]]
				f[i][j] %= MOD

		return f[n][B]


# rolling version
class Solution(object):
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def coinchange2(self, A, B):
		if not A and not B:
			return 1

		if not A:
			return 0

		MOD = 1000007
		n = len(A)
		f = [0] * (B+1)

		f[0] = 1
		for i in xrange(1, n+1):
			for j in xrange(1, B+1):
				if j >= A[i-1]:
					f[j] += f[j-A[i-1]]
				f[j] %= MOD

		return f[B]