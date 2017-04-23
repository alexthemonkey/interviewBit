# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
	# @param root : root node of tree
	# @param k : integer
	# @return an integer
	def kthsmallest(self, root, k):
		self.get_sum(root)
		return self._kth(root, k)


	def get_sum(self, root):
		if not root:
			return

		root.sum = 1
		if root.left:
			self.get_sum(root.left)
			root.sum += root.left.sum

		if root.right:
			self.get_sum(root.right)
			root.sum += root.right.sum


	def _kth(self, root, k):

		left_sum = root.left.sum if root.left else 0
		if k <= left_sum:
			return self._kth(root.left, k)

		if k == left_sum + 1:
			return root.val

		return self._kth(root.right, k-1-left_sum)


