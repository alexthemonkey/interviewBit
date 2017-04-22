"""
Counting Triangles

https://www.interviewbit.com/problems/counting-triangles/

You are given an array of N non-negative integers, A0, A1, ..., AN-1.
Considering each array element Ai as the edge length of some line segment, 
count the number of triangles which you can form using these array values.

Notes:

You can use any value only once while forming each triangle. 
Order of choosing the edge lengths doesnt matter. 
Any triangle formed should have a positive area.

Return answer modulo 10**9 + 7.

"""

"""
	If the edges are sorted. when outer loop goes from start to end,
	and in each loop, we already have the shortest edge (a) of a triangle,
	the other 2 edges b and c should satisfy:
		abs(b-c) < a
		
	2 pointer:
		outer loop => A[i]
		we trying to find A[right] - A[left] < A[i]
		
		right initialized to be left + 1
		for every possible left:
			keep let right increase until A[right] - A[left] >= A[i]
			
			then, any pos in the range (left, right) will form a triangle together with 
			A[i] and A[left]
"""

class Solution(object):
	# @param A : list of integers
	# @return an integer
	def nTriang(self, A):
		n = len(A)
		if n < 3:
			return 0

		A.sort()
		MOD = 10 ** 9 + 7
		ans = 0
		for i in xrange(n-2):
			right = i+2
			for left in xrange(i+1, n-1):
				right = left + 1 if left >= right else right
				while right < n and A[right]-A[left] < A[i]:
					right += 1
				ans += right - left - 1
				ans %= MOD

		return ans
