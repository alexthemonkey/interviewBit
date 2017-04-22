"""
2 Sum

https://www.interviewbit.com/problems/2-sum/

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 < index2. Please note that your returned answers (both index1 and index2 ) are not zero-based. 
Put both these numbers in order in an array and return the array from your function ( Looking at the function signature will make things clearer ). Note that, if no pair exists, return empty list.

If multiple solutions exist, output the one where index2 is minimum. If there are multiple solutions with the minimum index2, choose the one with minimum index1 out of them.

"""


class Solution(object):
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
	def twoSum(self, A, B):
		n = len(A)
		if n <= 1:
			return []

		pos = {A[0]: 0}
		for i in xrange(1, n):
			target = B - A[i]
			if pos.get(target, None) is not None:
				return [pos[target]+1, i+1]

			if pos.get(A[i], None) is None:
				pos[A[i]] = i
		return []
