"""
Magician And Chocolates

https://www.interviewbit.com/problems/magician-and-chocolates/

Given N bags, each bag contains Ai chocolates. There is a kid and a magician. In one unit of time, kid chooses a random bag i, eats Ai chocolates, then the magician fills the ith bag with floor(Ai/2) chocolates.

Given Ai for 1 <= i <= N, find the maximum number of chocolates kid can eat in K units of time.

For example,


K = 3
N = 2
A = 6 5

Return: 14

Note: Return your answer modulo 10^9+7

"""

from heapq import heappush, heappop, heapify


class Solution(object):
	# @param A : integer
	# @param B : list of integers
	# @return an integer
	def nchoc(self, A, B):
		B = [-v for v in B]
		heapify(B)
		MOD = 10 ** 9 + 7
		ans = 0
		for _ in xrange(A):
			if len(B):
				v = heappop(B)
			else:
				break

			ans -= v
			ans %= MOD

			v = (-v) / 2
			if v > 0:
				heappush(B, -v)
		return ans
