"""
Min Jumps Array

https://www.interviewbit.com/problems/min-jumps-array/

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example :
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

If it is not possible to reach the end index, return -1.

"""


"""
Let ans[i] = k stands for:
	the max pos we can get within i steps.
	
then we has ans[i], we can check the first ans[j] which is >= n-1
and this j will be the answer.

The key problem here is to get ans[].

by the definition of ans[], we can use some block update techniques.


if you want, you can use 2 int instead of ans[] to store the value.
and do a short-circuit return. But then, the code may not very clear
and hard to understand.
"""


class Solution(object):
	# @param A : list of integers
	# @return an integer
	def jump(self, A):
		n = len(A)
		if n == 1:
			return 0

		ans = [-1] * n
		ans[0] = 0
		step = 0

		temp_right_most_pos = 0

		for i in xrange(n):
			if i > ans[step] and i > temp_right_most_pos:
				return -1

			temp_right_most_pos = max(temp_right_most_pos, i+A[i])
			# hit the boundary of last step
			# then, we entering new step
			if i == ans[step]:
				step += 1
				ans[step] = max(ans[step-1], temp_right_most_pos)

		for i in xrange(n):
			if ans[i] >= n-1:
				return i
