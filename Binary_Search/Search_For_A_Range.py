"""
Search For A Range
https://www.interviewbit.com/problems/search-for-a-range/

Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithms runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example:

Given [5, 7, 7, 8, 8, 10]

and target value 8,

return [3, 4].
"""


class Solution(object):
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
	def lower_bound(self, aList, start, end, target):
		left, right = start, end

		while left <= right:
			mid = (left + right) / 2
			if aList[mid] >= target:
				right = mid - 1
			else:
				left = mid + 1
		return left

	def upper_bound(self, aList, start, end, target):
		left, right = start, end

		while left <= right:
			mid = (left + right) / 2
			if aList[mid] > target:
				right = mid - 1
			else:
				left = mid + 1
		return left

	def searchRange(self, A, B):
		n = len(A)
		if n == 0:
			return [-1, -1]

		left = self.lower_bound(A, 0, n-1, B)
		if left >= n or A[left] != B:
			return [-1, -1]

		right = self.upper_bound(A, 0, n-1, B)
		if right == 0 or A[right-1] != B:
			return [-1, -1]

		return [left, right-1]
