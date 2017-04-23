"""
Max Depth Of Binary Tree

https://www.interviewbit.com/problems/max-depth-of-binary-tree/

Given a binary tree, find its maximum depth.

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
	def maxDepth(self, A):
		if not A:
			return 0

		l = self.maxDepth(A.left)
		r = self.maxDepth(A.right)
		return 1 + max(l, r)
