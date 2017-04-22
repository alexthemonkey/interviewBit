"""
3 Sum Zero
https://www.interviewbit.com/problems/3-sum-zero/

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

"""


class Solution(object):
	# @param A : list of integers
	# @return a list of list of integers
	def threeSum(self, A):
		n = len(A)
		ans = []
		A.sort()

		for i in xrange(n-2):
			left, right = i+1, n-1

			while left < right:
				v = A[i] + A[left] + A[right]
				if v == 0:
					ans.append([A[i], A[left], A[right]])
					left += 1
					right -= 1
				elif v > 0:
					right -= 1
				else:
					left += 1
		if not ans:
			return ans

		ans =sorted(ans)
		realAns = [ans[0]]
		for i in xrange(1, len(ans)):
			if ans[i][0] == ans[i-1][0] and ans[i][1] == ans[i-1][1]:
				continue
			realAns.append(ans[i])

		return realAns
