"""
Woindow String
https://www.interviewbit.com/problems/window-string/


Given a string S and a string T, find the minimum window in S which will contain all the characters in T in linear time complexity.
Note that when the count of a character C in T is N, then the count of C in minimum window in S should be at least N.
"""

from collections import defaultdict


class Solution(object):
	# @param S : string
	# @param T : string
	# @return a string
	def minWindow(self, S, T):
		n = len(S)
		ans = [0, n-1]

		target = defaultdict(int)
		for x in T:
			target[x] += 1

		M = defaultdict(int)

		ansL = n+1
		left, right = 0, 0

		while left < n and right < n:
			M[S[right]] += 1
			if self.good(M, target):
				while S[left] not in T or M[S[left]]-1 >= target[S[left]]:
					M[S[left]] -= 1
					left += 1
				l = right-left
				if l < ansL:
					ansL = l
					ans = [left, right]

				M[S[left]] -= 1
				left += 1
				right += 1
			else:
				right += 1

		if ansL == n+1:
			return ""
		else:
			return S[ans[0]: ans[1]+1]

	def good(self, M, target):
		for key, value in target.iteritems():
			if M[key] < value:
				return False
		return True
