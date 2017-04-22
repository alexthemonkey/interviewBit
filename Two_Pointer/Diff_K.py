"""
Diff K

https://www.interviewbit.com/problems/diffk/
Given an array A of sorted integers and another non negative integer k, 
find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

"""


class Solution(object):
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def diffPossible(self, A, B):
		n = len(A)
		if n < 2:
			return 0

		left, right = 0, 1
		while right < n:
			v = A[right] - A[left]
			if v == B:
				return 1

			if v > B:
				left += 1
				if left >= right:
					right = 1 + left
			else:
				right += 1
		return 0