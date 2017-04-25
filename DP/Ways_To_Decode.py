"""
Ways To Decode

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

"""


class Solution(object):
	# @param A : string
	# @return an integer
	def numDecodings(self, A):
		A = '@' + A
		n = len(A)
		ans = [0] * n
		ans[0] = 1

		if '1' <= A[1]:
			ans[1] = 1

		for i in xrange(2, n):
			if A[i] == '0':
				if A[i-1]  in ('1', '2'):
					ans[i] = ans[i-2]
				else:
					return 0
			else:
				if A[i-1] == '0':
					ans[i] = ans[i-1]
				else:
					if 1 <= int(A[i-1]+A[i]) <= 26:
						ans[i] = ans[i-2]
					ans[i] += ans[i-1]

		return ans[n-1]
