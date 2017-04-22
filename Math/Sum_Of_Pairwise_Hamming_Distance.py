"""
Sum Of Pairwise Hamming Distance

https://www.interviewbit.com/problems/sum-of-pairwise-hamming-distance/

Hamming distance between two non-negative integers is defined as the number of positions at which the corresponding bits are different.

For example,

HammingDistance(2, 7) = 2, as only the first and the third bit differs in the binary representation of 2 (010) and 7 (111).

Given an array of N non-negative integers, find the sum of hamming distances of all pairs of integers in the array.
Return the answer modulo 1000000007.

Example

Let f(x, y) be the hamming distance defined above.

A=[2, 4, 6]

We return,
f(2, 2) + f(2, 4) + f(2, 6) + 
f(4, 2) + f(4, 4) + f(4, 6) +
f(6, 2) + f(6, 4) + f(6, 6) = 

0 + 2 + 1
2 + 0 + 1
1 + 1 + 0 = 8
"""


class Solution(object):
	# @param A : tuple of integers
	# @return an integer
	def hammingDistance(self, A):
		MOD = 10 ** 9 + 7
		N = len(A)
		num_of_one = [0] * 33

		for x in A:
			for i in xrange(33):
				if x == 0:
					break
				num_of_one[i] += (x%2)
				x /= 2

		ans = 0
		for i in xrange(33):
			num_1 = num_of_one[i]
			num_0 = N - num_1

			ans += 2 * num_0 * num_1
			ans %= MOD
		return ans
