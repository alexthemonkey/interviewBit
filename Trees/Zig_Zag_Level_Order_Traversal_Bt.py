"""
Zig Zag Level Order Traversal Bt

https://www.interviewbit.com/problems/zigzag-level-order-traversal-bt/

Given a binary tree, return the zigzag level order traversal of its nodes values. 
ie, from left to right, then right to left for the next level and alternate between).


"""


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict


class Solution(object):
	# @param A : root node of tree
	# @return a list of list of integers
	def zigzagLevelOrder(self, A):
		M = defaultdict(list)
		if not A:
			return []

		Q = [A]
		A.level = 0
		while len(Q):
			root = Q.pop(0)
			M[root.level].append(root.val)

			if root.left:
				root.left.level = root.level + 1
				Q.append(root.left)

			if root.right:
				root.right.level = root.level + 1
				Q.append(root.right)

		rev = False
		ans = []
		for key in sorted(M.keys()):
			value_list = M[key]
			if rev:
				value_list = reversed(value_list)
			ans.append(value_list)

			rev = (not rev)

		return ans
