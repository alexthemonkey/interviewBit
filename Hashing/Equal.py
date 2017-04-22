"""
Equal

https://www.interviewbit.com/problems/equal/


Given an array A of integers, find the index of values that satisfy A + B = C + D, 
where A,B,C & D are integers values in the array

1) Return the indices `A1 B1 C1 D1`, so that 
  A[A1] + A[B1] = A[C1] + A[D1]
  A1 < B1, C1 < D1
  A1 < C1, B1 != D1, B1 != C1 
  
2) If there are more than one solutions, 
   then return the tuple of values which are lexicographical smallest. 

"""

from collections import defaultdict


class Solution:
	# @param A : list of integers
	# @return a list of integers
	def equal(self, A):
		n = len(A)
		if n < 4:
			return []

		M = defaultdict(list)
		ans = []
		for i in xrange(n):
			for j in xrange(i+1, n):
				sum_v = A[i] + A[j]
				for v in M[sum_v]:
					if v[0] < i and v[1] != i and v[1] != j:
						if not ans:
							ans = [v[0], v[1], i, j]
						else:
							ans = min(ans, [v[0], v[1], i, j])
						break
				M[sum_v].append((i, j))
		return ans
