"""
Sorted Array To Balanced Bst
https://www.interviewbit.com/problems/sorted-array-to-balanced-bst/

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.


"""



# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	# @param A : tuple of integers
	# @return the root node in the tree
	def sortedArrayToBST(self, A):
		return self.solve(A, 0, len(A)-1)

	def solve(self, A, i, j):
		if i > j:
			return None

		mid = (i+j) / 2
		root = TreeNode(A[mid])
		root.left = self.solve(A, i, mid-1)
		root.right = self.solve(A, mid+1, j)
		return root
