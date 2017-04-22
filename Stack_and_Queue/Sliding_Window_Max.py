"""
Sliding Window Max

https://www.interviewbit.com/problems/sliding-window-max/


A long array A[] is given to you. There is a sliding window of size w which is moving from the very left of the array to the very right. You can only see the w numbers in the window. Each time the sliding window moves rightwards by one position.

Example :

The array is [1 3 -1 -3 5 3 6 7], and w is 3.

Window position	Max
 	 
[1 3 -1] -3 5 3 6 7	  3
1 [3 -1 -3] 5 3 6 7	  3
1 3 [-1 -3 5] 3 6 7	  5
1 3 -1 [-3 5 3] 6 7	  5
1 3 -1 -3 [5 3 6] 7	  6
1 3 -1 -3 5 [3 6 7]	  7


Input: A long array A[], and a window width w
Output: An array B[], B[i] is the maximum value of from A[i] to A[i+w-1]
Requirement: Find a good optimal way to get B[i]
"""


"""
We maintain a de-queue with 3 constraint:
	1. Maximum num of elements in the queue is: B (window size)
	2. Elements in the queue are decreasing
	3. current_index - front_index should less than B (implies rule 1)
	
if above 3 satisfied, then every time, A[queue_front] would be the max value.
"""


class Solution(object):
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
	def slidingMaximum(self, A, B):
		Q = []
		ans = []

		for i in xrange(len(A)):
			# ensure elements in Q are decreasing
			while len(Q) and A[Q[-1]] <= A[i]:
				Q.pop()

			# current_index - front_index should less than B
			# which also implies:
			if len(Q) and Q[0] == i-B:
				Q.pop(0)

			Q.append(i)
			if i >= B-1:
				ans.append(A[Q[0]])

		return ans
