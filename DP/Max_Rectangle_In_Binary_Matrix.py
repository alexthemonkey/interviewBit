"""
Max Rectangle In Binary Matrix

https://www.interviewbit.com/problems/max-rectangle-in-binary-matrix/


Given a 2D binary matrix filled with 0s and 1s, find the largest rectangle containing all ones and return its area.

Bonus if you can solve it in O(n^2) or less.

Example :

A : [  1 1 1
       0 1 1
       1 0 0 
    ]

Output : 4 

As the max area rectangle is created by the 2x2 rectangle created by (0,1), (0,2), (1,1) and (1,2)

"""

class Solution(object):
	# @param A : list of list of integers
	# @return an integer
	def maximalRectangle(self, A):
		n = len(A)
		if n == 0:
			return 0
		m = len(A[0])

		for i in xrange(1, n):
			for j in xrange(m):
				if A[i][j] == 1:
					A[i][j] += A[i-1][j]

		ans = 0
		for i in xrange(n):
			ans = max(ans, self.largestRectangleArea(A[i]))

		return ans

	def largestRectangleArea(self, A):
		A.append(0)  # make things easier so we don't need to handle the boundary
		stack = []
		ans = 0

		for i in xrange(len(A)):
			while len(stack) and A[stack[-1]] >= A[i]:
				h = A[stack.pop()]
				l_pos = stack[-1] if len(stack) else -1
				r_pos = i
				ans = max(ans, h * (r_pos-l_pos-1))
			stack.append(i)

		return ans