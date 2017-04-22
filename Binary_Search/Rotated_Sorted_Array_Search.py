"""
Rotated Sorted Array Search
https://www.interviewbit.com/problems/rotated-sorted-array-search/

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7  might become 4 5 6 7 0 1 2 ).

You are given a target value to search. If found in the array, return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Input : [4 5 6 7 0 1 2] and target = 4
Output : 0

"""

"""
	Compare A[0] and target B to know which segment the B might be in (only one of those 2 is possible).
	Then, 
		if B in left part and A[mid] < A[0] (which means mid in right part), we decrease right.
		if B in right part, and A[mid] >= A[0] (which means mid in left part), we increase left.
		Other than above, the rest is ordinary b-search
"""


class Solution(object):
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def search(self, A, B):
		n = len(A)
		if n == 0:
			return -1

		target_in_left_part = (B >= A[0])
		target_in_right_part = (not target_in_left_part)

		left, right = 0, n-1
		while left <= right:
			mid = (left+right) / 2

			if target_in_left_part and A[mid] < A[0]:
				right = mid-1; continue

			if target_in_right_part and A[mid] >= A[0]:
				left = mid+1; continue

			if A[mid] == B:
				return mid

			if A[mid] < B:
				left = mid+1
			else:
				right = mid-1

		if left < n and A[left] == B:
			return left
		return -1
