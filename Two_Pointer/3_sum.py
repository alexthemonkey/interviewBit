"""
3 Sum

https://www.interviewbit.com/problems/3-sum/

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
Return the sum of the three integers.

Assume that there will only be one solution

Example: 
given array S = {-1 2 1 -4}, 
and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)

"""

class Solution(object):
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def threeSumClosest(self, A, B):
		A = sorted(A)
		n = len(A)

		ans = A[0] + A[1] + A[-1]
		diff = abs(ans-B)

		for i in xrange(n):
			target = B - A[i]
			left, right = i+1, n-1

			while left < right:
				temp_value = A[left] + A[right]
				current_diff = abs(target - temp_value)
				if diff > current_diff:
					diff = current_diff
					ans = temp_value + A[i]

				if diff == 0:
					return ans

				if temp_value < target:
					left += 1
				else:
					right -= 1

		return ans
