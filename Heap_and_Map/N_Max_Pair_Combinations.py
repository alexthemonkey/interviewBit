"""
N Max Pair Combinations

https://www.interviewbit.com/problems/n-max-pair-combinations/

Given two arrays A & B of size N each.
Find the maximum n elements from the sum combinations (Ai + Bj) formed from elements in array A and B.

For example if A = [1,2], B = [3,4], then possible pair sums can be 1+3 = 4 , 1+4=5 , 2+3=5 , 2+4=6
and maximum 2 elements are 6, 5

N = 4
a[]={1,4,2,3}
b[]={2,5,1,6}


Maximum 4 elements of combinations sum are
10   (4+6), 
9    (3+9),
9    (4+5),
8    (2+6)
"""

from heapq import heappush, heappop


class Solution(object):
	# @param A : list of integers
	# @param B : list of integers
	# @return a list of integers
	def solve(self, A, B):
		n = len(A)
		A.sort(); A.reverse()
		B.sort(); B.reverse()

		h = []
		finished = False
		for x in A:
			if finished:
				break

			for idx, y in enumerate(B):
				v = x + y
				if len(h) < n:
					heappush(h, v)
				else:
					if h[0] < v:
						heappop(h)
						heappush(h, v)
					else:
						if idx == 0:
							finished = True
						break

		h.sort()
		h.reverse()
		return h
