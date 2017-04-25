"""
Longest Arithmetic Progression

https://www.interviewbit.com/problems/longest-arithmetic-progression/

Find longest Arithmetic Progression in an integer array and return its length. More formally, 
find longest sequence of indeces, 0 < i1 < i2 < ... < ik < ArraySize(0-indexed) such that 
sequence A[i1], A[i2], ...,  A[ik] is an Arithmetic Progression. 
Arithmetic Progression is a sequence in which all the differences between consecutive pairs are the same, 

1) 1, 2, 3(All differences are equal to 1)
2) 7, 7, 7(All differences are equal to 0)
3) 8, 5, 2(Yes difference can be negative too)

Samples
1) Input: 3, 6, 9, 12
Output: 4

2) Input: 9, 4, 7, 2, 10
Output: 3(If we choose elements in positions 1, 2 and 4(0-indexed))

"""

"""
	let f[i][j] stands for the length of Arithmetic Progression end with A[i] with diff of j
"""


from collections import defaultdict

class Solution(object):
	# @param A : tuple of integers
	# @return an integer
	def solve(self, A):
		n = len(A)
		if n == 0:
			return 0

		f = [defaultdict(int) for _ in xrange(n)]

		ans = 1
		for i in xrange(1, n):
			for j in xrange(i):
				d = A[i]-A[j]
				num = f[j].get(d, 1) + 1
				f[i][d] = max(f[i][d], num)
			ans = max(ans, max(f[i].values()))

		return ans
