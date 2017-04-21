"""
Max Non Negative Sub Array

https://www.interviewbit.com/problems/max-non-negative-subarray/

Find out the maximum sub-array of non negative numbers from an array.
The sub-array should be continuous. That is, a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array. Sub-array A is greater than sub-array B if sum(A) > sum(B).

Example:

A : [1, 2, 5, -7, 2, 3]
The two sub-arrays are [1, 2, 5] [2, 3].
The answer is [1, 2, 5] as its sum is larger than [2, 3]
NOTE: If there is a tie, then compare with segment's length and return segment which has maximum length
NOTE 2: If there is still a tie, then return the segment with minimum starting index
"""


class Solution(object):
	# @param A : list of integers
	# @return a list of integers
	def maxset(self, A):
		A = A + [-1]

		ansLeft = -1
		ansRight = -1
		ansSum = -1

		left = -1
		segSum = 0

		for i in xrange(len(A)):
			if A[i] >= 0:
				segSum += A[i]
			else:
				if segSum > ansSum or (segSum == ansSum and (i-left > ansRight-ansLeft)):
					ansSum = segSum
					ansLeft = left
					ansRight = i

				segSum = 0
				left = i

		return A[ansLeft+1: ansRight]
