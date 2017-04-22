"""
Diffk ii

https://www.interviewbit.com/problems/4-sum/


Given an array A of integers and another non negative integer k, 
find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

"""

from collections import defaultdict


class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def diffPossible(self, A, B):
		cnt = defaultdict(int)
		for x in A:
			cnt[x] += 1

		for x in A:
			target = B + x
			if x != target and cnt.get(target, 0) > 0:
				return 1
			if x == target and cnt.get(target, 0) > 1:
				return 1

		return 0
