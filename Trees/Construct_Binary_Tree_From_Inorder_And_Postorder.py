"""
Construct Binary Tree From Inorder And Postorder

https://www.interviewbit.com/problems/construct-binary-tree-from-inorder-and-postorder/

Given inorder and postorder traversal of a tree, construct the binary tree.

"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
	# @param inorder : list of integers denoting inorder traversal
	# @param postorder : list of integers denoting postorder traversal
	# @return the root node in the tree
	def buildTree(self, inorder, postorder):
		self.inorder = inorder
		self.postorder = postorder

		self.prepare()
		n = len(inorder)
		m = len(postorder)

		return self.solve(0, n-1, 0, m-1)


	def prepare(self):
		self.pos_of = {}
		for idx, value in enumerate(self.inorder):
			self.pos_of[value] = idx

	def solve(self, a, b, c, d):
		if a > b or c > d:
			return None

		root = TreeNode(self.postorder[d])
		pos = self.pos_of[self.postorder[d]]

		root.left = self.solve(a, pos-1, c, pos+c-1-a)
		root.right = self.solve(pos+1, b, pos+c-a, d-1)

		return root
