"""
Intersection Of Sorted Arrays

https://www.interviewbit.com/problems/intersection-of-sorted-arrays/

Find the intersection of two sorted arrays.
OR in other words,
Given 2 sorted arrays, find all the elements which occur in both the arrays.

Example :

Input : 
    A : [1 2 3 3 4 5 6]
    B : [3 3 5]

Output : [3 3 5]

Input : 
    A : [1 2 3 3 4 5 6]
    B : [3 5]

Output : [3 5]
"""


class Solution(object):
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @return a list of integers
	def intersect(self, A, B):
		n = len(A)
		m = len(B)

		pa, pb = 0, 0
		ans = []
		while pa < n and pb < m:
			if A[pa] == B[pb]:
				ans.append(A[pa])
				pa += 1
				pb += 1
				continue

			if A[pa] < B[pb]:
				pa += 1
			else:
				pb += 1
		return ans
