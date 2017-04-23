"""
Symmetric Binary Tree
https://www.interviewbit.com/problems/symmetric-binary-tree/


Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).


But the following is not:
    1
   / \
  2   2
   \   \
   3    3
"""


class Solution(object):

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

	def isSymmetric(self, A):
		if not A:
			return 1

		self.mirror(A.left)
		if self.isSameTree(A.left, A.right):
			return 1

		return 0

	def mirror(self, node):
		if not node:
			return

		node.left, node.right = node.right, node.left
		self.mirror(node.left)
		self.mirror(node.right)
