"""
Add One To Number

https://www.interviewbit.com/problems/add-one-to-number/


Given a non-negative number represented as an array of digits,

add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

Example:

If the vector has [1, 2, 3]

the returned vector should be [1, 2, 4]

as 123 + 1 = 124.

"""


class Solution(object):
	# @param A : list of integers
	# @return a list of integers

	def plusOne(self, A):
		if not A:
			return [1]

		added = 1
		n = len(A)

		for i in xrange(n-1, -1, -1):
			v = A[i] + added
			A[i] = v % 10
			added = v / 10

		if added > 0:
			A = [added] + A
			return A
		else:
			for i in xrange(n):
				if A[i] != 0:
					break
			return A[i:]
