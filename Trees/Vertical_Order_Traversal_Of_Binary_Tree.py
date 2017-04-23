"""
Vertical Order Traversal Of Binary Tree

Given a binary tree, print a vertical order traversal of it.

Example :
Given binary tree:

      6
    /   \
   3     7
  / \     \
 2   5     9
returns

[
    [2],
    [3],
    [6 5],
    [7],
    [9]
]

"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict


class Solution:
	# @param A : root node of tree
	# @return a list of list of integers
	def verticalOrderTraversal(self, A):

		M = defaultdict(list)

		def dfs_get_pos(node):
			M[node.pos].append([node.height, node.val])

			if node.left:
				node.left.pos = node.pos - 1
				node.left.height = node.height + 1
				dfs_get_pos(node.left)

			if node.right:
				node.right.pos = node.pos + 1
				node.right.height = node.height + 1
				dfs_get_pos(node.right)

		if not A:
			return []

		A.pos = 0
		A.height = 0
		dfs_get_pos(A)

		ans = []
		for key in sorted(M.keys()):
			value_list = [x[1] for x in sorted(M[key], key=lambda y: y[0])]
			ans.append(value_list)
		return ans
