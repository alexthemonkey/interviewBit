"""
Longest Common Prefix

https://www.interviewbit.com/problems/longest-common-prefix/


Write a function to find the longest common prefix string amongst an array of strings.

Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.

As an example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".

Given the array of strings, you need to find the longest S which is the prefix of ALL the strings in the array.

Example:

Given the array as:

[

  "abcdefgh",

  "aefghijk",

  "abcefgh"
]
The answer would be "a"
"""

class Solution(object):
	# @param A : list of strings
	# @return a strings
	def longestCommonPrefix(self, A):
		if not A:
			return ""

		ans = A[0]
		for x in A[1:]:
			ans = self.getCommonPreFixPosition(ans, x)
			if not ans:
				return ans

		return ans

	def getCommonPreFixPosition(self, x, y):
		n = len(x)
		m = len(y)
		if n > m:
			x, y = y, x
			n, m = m, n

		for i in xrange(n):
			if x[i] != y[i]:
				return x[:i]
		return x
