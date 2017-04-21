"""
Pascal Triangle Rows
https://www.interviewbit.com/problems/pascal-triangle-rows/

Given numRows, generate the first numRows of Pascals triangle.

Pascals triangle : To generate A[C] in row R, sum up A[C] and A[C-1] from previous row R - 1.

Example:

Given numRows = 5,

Return

[
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
]
"""


class Solution(object):
	# @param A : integer
	# @return a list of lists of integers
	def generate(self, A):
		if A == 0:
			return []

		ans = [[1]]
		for row_id in xrange(1, A):
			last_row = ans[row_id-1]
			current_row = [1]
			for i in xrange(1, len(last_row)):
				current_row.append(last_row[i-1]+last_row[i])
			current_row.append(1)
			ans.append(current_row)
		return ans