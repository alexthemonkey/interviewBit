"""
Length Of Longest Subsequence
https://www.interviewbit.com/problems/length-of-longest-subsequence/

Given an array of integers, find the length of longest subsequence which is first increasing then decreasing.

For the given array [1 11 2 10 4 5 2 1]

Longest subsequence is [1 2 10 4 2 1]

Return value 6
"""


class Solution(object):
	# @param A : tuple of integers
	# @return an integer
	def longestSubsequenceLength(self, A):
		n = len(A)
		if n == 0:
			return 0

		max_len_inr = [1] * n
		for i in xrange(1, n):
			for j in xrange(i):
				if A[j] < A[i]:
					max_len_inr[i] = max(max_len_inr[i], max_len_inr[j] + 1)

		max_len_inr_right = [1] * n
		for i in xrange(n - 2, -1, -1):
			for j in xrange(n - 1, i, -1):
				if A[j] < A[i]:
					max_len_inr_right[i] = max(max_len_inr_right[i], 1 + max_len_inr_right[j])

		ans = 1
		for i in xrange(n):
			ans = max(ans, max_len_inr[i] + max_len_inr_right[i] - 1)

		return ans
