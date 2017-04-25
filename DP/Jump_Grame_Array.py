"""
Jump Game Array
https://www.interviewbit.com/problems/jump-game-array/


Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return 1 ( true ).

A = [3,2,1,0,4], return 0 ( false ).

Return 0/1 for this problem

"""


class Solution(object):
	# @param A : list of integers
	# @return an integer
	def canJump(self, A):

		right_most_pos = 0
		for i in xrange(len(A)):
			if i <= right_most_pos:
				right_most_pos = max(i+A[i], right_most_pos)
			else:
				return 0

		return 1
