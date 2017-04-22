"""
Count And Say

https://www.interviewbit.com/problems/count-and-say/

The count-and-say sequence is the sequence of integers beginning as follows:

1, 11, 21, 1211, 111221, ...
1 is read off as one 1 or 11.
11 is read off as two 1s or 21.

21 is read off as one 2, then one 1 or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

Example:

if n = 2,
the sequence is 11.
"""


class Solution(object):
	# @param A : integer
	# @return a strings
	def countAndSay(self, A):
		last = "1"
		for i in xrange(1, A):
			last = self.count(last)

		return last

	def count(self, s):
		ans = ""
		v = s[0]
		cnt = 1
		for i in xrange(1, len(s)):
			if s[i] == s[i - 1]:
				cnt += 1
			else:
				ans += str(cnt) + v
				v = s[i]
				cnt = 1

		ans += str(cnt) + v
		return ans
