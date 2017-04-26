"""
Longest Increasing Subsequence
https://www.interviewbit.com/problems/longest-increasing-subsequence/

Find the longest increasing subsequence of a given array.

In other words, find a subsequence of array in which the subsequences elements are in strictly increasing order, and in which the subsequence is as long as possible. 
This subsequence is not necessarily contiguous, or unique.
In this case, we only care about the length of the longest increasing subsequence.

Example :

Input : [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
Output : 6
The sequence : [0, 2, 6, 9, 13, 15] or [0, 4, 6, 9, 11, 15] or [0, 4, 6, 9, 13, 15]
"""


# O(n*n) solution
class Solution0(object):
	# @param A : tuple of integers
	# @return an integer
	def lis(self, A):
		n = len(A)
		if n == 0:
			return 0

		f = [1] * n
		for i in xrange(1, n):
			for j in xrange(i):
				if A[i] > A[j]:
					f[i] = max(f[i], 1 + f[j])

		return max(f)



# O(nlog(n)) solution

def upper_bound(aList, target, start=None, end=None):
	start = 0 if start is None else start
	end = len(aList)-1 if end is None else end

	left, right = start, end
	while left <= right:
		mid = (left + right) / 2
		if aList[mid] > target:
			right = mid - 1
		else:
			left = mid + 1
	return left

class Solution(object):
	# @param A : tuple of integers
	# @return an integer
	def lis(self, A):
		n = len(A)
		if n == 0:
			return 0

		inf = max(A) + 1
		end_of_length = [inf] * (n+1)
		end_of_length[0] = -1
		end_of_length[1] = A[0]

		for i in xrange(1, n):
			pos = upper_bound(end_of_length, A[i])
			if A[i] > end_of_length[pos-1]:
				end_of_length[pos] = A[i]

		for i in xrange(n, -1, -1):
			if end_of_length[i] != inf:
				return i
