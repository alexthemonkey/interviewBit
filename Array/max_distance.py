"""
Max Distance


Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

If there is no solution possible, return -1.

Example :

A : [3 5 4 2]

Output : 2 
for the pair (3, 4)

"""

"""
	One observation is that:
	if i and j are the answer, then 
		1. A[i] is the min num among A[0], A[1], ... A[i] 
		2. A[j] is the max num among A[j], A[j+1], ... A[n-1]
	
	based on this, we could use 2-pointer to solve this one.
	
	
"""

class Solution(object):
	# @param A : tuple of integers
	# @return an integer
	def maximumGap(self, A):
		n = len(A)
		if n == 0:
			return -1

		lmin = [A[0]] * n
		rmax = [A[n-1]] * n

		for i in xrange(1, n):
			lmin[i] = min(A[i], lmin[i-1])
		for i in xrange(n-2, -1, -1):
			rmax[i] = max(A[i], rmax[i+1])

		left, right = 0, 0
		ans = 0
		while  left <= right < n:
			if lmin[left] <= rmax[right]:
				ans = max(ans, right-left)
				right += 1
			else:
				left += 1

		return ans
