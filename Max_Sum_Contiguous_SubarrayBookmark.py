"""
Max Sum Contiguous Sub array

https://www.interviewbit.com/problems/max-sum-contiguous-subarray/


Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example:

Given the array [-2,1,-3,4,-1,2,1,-5,4],

the contiguous subarray [4,-1,2,1] has the largest sum = 6.

For this problem, return the maximum sum.

"""


class Solution(object):
	# @param A : tuple of integers
	# @return an integer
	def maxSubArray(self, A):
		preMax = A[0]
		ans = A[0]

		for i in xrange(1, len(A)):
			preMax = max(A[i], A[i]+preMax)
			ans = max(ans, preMax)

		return ans
