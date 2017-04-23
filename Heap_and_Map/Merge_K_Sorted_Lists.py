"""
Merge K Sorted Lists

https://www.interviewbit.com/problems/merge-k-sorted-lists/


Merge k sorted linked lists and return it as one sorted list.

Example :

1 -> 10 -> 20
4 -> 11 -> 13
3 -> 8 -> 9
will result in

1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20
"""

# Definition for singly-linked list.

from heapq import heapify, heappop, heappush


class ListNode:

	def __init__(self, x):
		self.val = x
		self.next = None

	def __cmp__(self, other):
		return cmp(self.val, other.val)


class Solution(object):
	# @param A : list of linked list
	# @return the head node in the linked list
	def mergeKLists(self, A):
		ans = []
		heapify(A)

		while len(A):
			node = heappop(A)
			ans.append(node)
			node = node.next
			if node:
				heappush(A, node)

		for i in xrange(len(ans)-1):
			ans[i].next = ans[i+1]
		return ans[0]
