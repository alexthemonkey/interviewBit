"""
Longest Valid Parentheses
https://www.interviewbit.com/problems/longest-valid-parentheses/

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

"""


"""

	let f[i] stands for, the longest valid parentheses ends with A[i]:
	
	so 
		1. if A[i] == '('   then f[i] = 0
		2. if A[i] == ")" and A[i-1] == '('  then f[i] = 2 + f[i-2]
		3. if A[i] == ")" and A[i-1] == ')'
			then it should be something like ((...... ))
			we compare A[i] with A[i-l[i-1]-1]  to see if they match.
			
			then, if they match, we still need to concatenate with parentheses ends with A[i-l[i-1]-1]
"""


class Solution(object):
	# @param A : string
	# @return an integer
	def longestValidParentheses(self, A):
		n = len(A)
		if n <= 1:
			return 0

		l = [0] * n
		if A[0] == '(' and A[1] == ')':
			l[1] = 2

		for i in xrange(2, n):
			if A[i] == '(':
				continue

			if A[i-1] == '(':
				l[i] = 2 + l[i-2]
			else:
				pos = i - l[i-1] - 1
				if pos >= 0 and A[pos] == '(':
					l[i] = l[i-1] + 2
					if pos - 1 >= 0:
						l[i] += l[pos-1]

		return max(l)
