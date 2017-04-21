"""
N/3 Repeat Number

https://www.interviewbit.com/problems/n3-repeat-number/


You are given a read only array of n integers. Find out if any integer occurs more than n/3 times in the array in linear time and constant additional space.

If so, return the integer. If not, return -1.

If there are multiple solutions, return any one.

Example :

Input : [1 2 3 1 1]
Output : 1 
1 occurs 3 times which is more than 5/3 times. 
"""


class Solution(object):
	# @param A : tuple of integers
	# @return an integer
	def repeatedNumber(self, A):
		n = len(A)
		if n == 0:
			return -1
		if n <= 2:
			return A[0]

		target_cnt = n / 3

		rangeTuple = (0, 1, 2)
		num = [-1, -1, -1]
		cnt = [0, 0, 0]
		for v in A:
			if v in num:
				for i in rangeTuple:
					if num[i] == v:
						cnt[i] += 1
						break
			else:
				for i in rangeTuple:
					if cnt[i] == 0:
						num[i] = v
						cnt[i] = 1
						break

			base = min(cnt)
			cnt = [c-base for c in cnt]
			for i in rangeTuple:
				if cnt[i] == 0:
					num[i] = -1

		for i in rangeTuple:
			if cnt[i] > 0:
				x = 0
				for v in A:
					if v == num[i]:
						x += 1
				if x > target_cnt:
					return num[i]
		return -1
