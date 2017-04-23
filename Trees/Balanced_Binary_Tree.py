"""
Balanced Binary Tree

https://www.interviewbit.com/problems/balanced-binary-tree/

Given a binary tree, determine if it is height-balanced.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem

"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
	# @param A : root node of tree
	# @return an integer
	def isBalanced(self, A):
		if not A:
			return 1

		def dfs_get_max_length(node):
			l = 1
			if node.left:
				dfs_get_max_length(node.left)
				l = max(l, 1+node.left.length)

			if node.right:
				dfs_get_max_length(node.right)
				l = max(l, 1+node.right.length)

			node.length = l

		dfs_get_max_length(A)
		return self._is_balanced(A)


	def _is_balanced(self, A):
		if not A:
			return 1

		left = 0 if not A.left else A.left.length
		right = 0 if not A.right else A.right.length

		if abs(left-right) > 1:
			return 0

		return 1 \
			if self._is_balanced(A.left) and self._is_balanced(A.right) \
			else 0


"""
Version 2:
	Actually, the get_max_length process and is_balanced process can be done at the same time.
"""

class Solution2(object):

	def _is_balanced(self, node):
		if not node:
			return 0, True

		l, left_ok = self._is_balanced(node.left)
		r, right_ok = self._is_balanced(node.right)
		l += 1; r += 1

		if abs(l-r) <= 1 and left_ok and right_ok:
			return max(l, r), True
		else:
			return max(l, r), False

	def isBalanced(self, A):
		if not A:
			return 1

		_, balanced = self._is_balanced(A)
		return 1 if balanced else 0
