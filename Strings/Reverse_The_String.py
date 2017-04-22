"""
Add Binary Strings

https://www.interviewbit.com/problems/add-binary-strings/


Given two binary strings, return their sum (also a binary string).

Example:

a = "100"

b = "11"
Return a + b = "111"
"""


class Solution(object):
	# @param A : string
	# @param B : string
	# @return a strings
	def addBinary(self, A, B):
		n = len(A)
		m = len(B)
		if n < m:
			A = "0" * (m - n) + A
		else:
			B = "0" * (n - m) + B

		n = len(A)
		ans = [0] * n
		added = 0
		for i in xrange(n - 1, -1, -1):
			v = int(A[i]) + int(B[i]) + added
			ans[i] = v % 2
			added = v / 2

		if added > 0:
			ans = [added] + ans

		for i in xrange(len(ans)):
			if ans[i] != 0:
				break
		ans = "".join([str(x) for x in ans])
		if i < len(ans):
			return ans[i:]
		else:
			return "0"
