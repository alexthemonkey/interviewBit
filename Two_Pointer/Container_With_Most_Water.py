"""
Container With Most Water

https://www.interviewbit.com/problems/container-with-most-water/

Given n non-negative integers a1, a2, ..., an,
where each represents a point at coordinate (i, ai).
'n' vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).

Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Your program should return an integer which corresponds to the maximum area of water that can be contained 
( Yes, we know maximum area instead of maximum volume sounds weird. But this is 2D plane we are working with for simplicity ).


"""

"""

	lets see A[0], A[1], ..., A[n-1]
	if A[0] > A[n-1]:
		then all possible containers related to A[n-1] will less the the container (A[0] A[n-1])
		because:
			container (A[0], A[n-1]) =>  (n-1-0) * min(A[0], A[n-1]) = (n-1) * A[n-1]
			container (A[x], A[n-1]) =>  (x-0) * min(A[x], A[n-1])
				we know that: x < n-1 and min(A[x], A[n-1]) <= A[n-1]
				so container  (A[x], A[n-1]) < (n-1) * A[n-1] = container (A[0], A[n-1])
		
		so we know: if A[0] > A[n-1], we don't need to consider any other (A[x], A[n-1])
		which means A[n-1] will be useless after the first calculation
		which means the problem scale comes from (0, n-1) down to (0, n-2)
	
	if A[0] < A[n-1]:
		same, (0, n-1) comes down to (1, n-1)

	either case, we can scale problem down by 1 each time.
"""

class Solution(object):
	# @param A : list of integers
	# @return an integer
	def maxArea(self, A):
		n = len(A)
		ans = 0

		left, right = 0, n-1
		while left < right:
			ans = max(ans, (right-left)*min(A[left], A[right]))
			if A[left] > A[right]:
				right -= 1
			else:
				left += 1

		return ans