# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	# @param A : root node of tree
	# @param B : root node of tree
	# @return an integer
	def isSameTree(self, A, B):
		if not A and not B:
			return 1

		if A and B:
			value_ok = (A.val == B.val)
			if not value_ok:
				return 0

			left_ok = self.isSameTree(A.left, B.left)
			if not left_ok:
				return 0

			right_ok = self.isSameTree(A.right, B.right)
			if not right_ok:
				return 0

			return 1
		return 0
