from __future__ import unicode_literals
"""
Painters Partition Problem

You have to paint N boards of length {A0, A1, A2, A3, ... ,AN-1}. 
There are K painters available and 
you are also given how much time a painter takes to paint 1 unit of board. 
You have to get this job done as soon as possible under the constraints that 
any painter will only paint contiguous sections of board.

2 painters cannot share a board to paint. That is to say, a board
cannot be painted partially by one painter, and partially by another.

A painter will only paint contiguous boards. Which means a
configuration where painter 1 paints board 1 and 3 but not 2 is
invalid.

Return the ans % 10000003

Input :
K : Number of painters
T : Time taken by painter to paint 1 unit of board
L : A List which will represent length of each board

Output:
     return minimum time to paint all boards % 10000003
     
Input : 
  K : 2
  T : 5
  L : [1, 10]
  
Output : 50

"""

"""
Observation:
	1. We are targeting at minimizing the maximum value, a typical binary search. And
	2. if x is the answer, x+1 will also be a available answer. => we can apply b-search
"""


class Solution(object):
	# @param K : integer
	# @param T : integer
	# @param L : list of integers
	# @return an integer
	def paint(self, K, T, L):
		left, right = max(L), sum(L)
		MOD = 10000003

		while left <= right:
			mid = (left + right) / 2
			if self.solvable(L, K, mid):
				right = mid-1
			else:
				left = mid+1

		return ((left * T) % MOD)


	def solvable(self, L, K, maxV):
		cap = 0
		cnt = 1
		for v in L:
			if cap + v <= maxV:
				cap += v
			else:
				cnt += 1
				cap = v

			if cnt > K:
				return False
		return True


