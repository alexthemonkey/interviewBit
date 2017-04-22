"""
Largest Rectangle In Histogram
https://www.interviewbit.com/problems/largest-rectangle-in-histogram/

Given n non-negative integers representing the histograms bar height where the width of each bar is 1, 
find the area of largest rectangle in the histogram.

given height = [2,1,5,6,2,3].
The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10.

"""

"""
	Observation:
		if the final answer is  A[i] A[i+1] A[i+2], ..., A[j]
		then we know 2 things:
			1. the height of this rectangle, let say h, is one of the height in A[i,...,j]
			2. A[i-1] < h and A[j+1] < h. Otherwise we could expend above 
			to be A[i-1] ... A[j] or A[i] ... A[j+1] or even A[i-1] ... A[j+1]
			which are all more than the original answer.
			
	Let's dig deeper: 
		let say for the answer A[i] A[i+1], ..., A[k]=h  ,...,A[j]
		
		let A[k] is the height of the rectangle,
		we can also know that A[i-1] is the first one to the left of position K which is less than h
		and A[j+1] is the first one to the right of K which is less than h
		
		so basically, for a given pos: X
		if we want to use A[x] as the height of rectangle,
		then the left boundary of this rectangle is the nearest pos to the left of X which is less than A[x]
		similar happens to the right boundary of the this rectangle.
		
	So the problem becomes: for every position X, we need to find,
		nearest left or right pos which is less than A[x]
		
		
	There are 2 ways to do it:
"""

# jumping
def get_nearest_less_left_jumping(A):
	n = len(A)
	ans = [-1] * n

	for i in xrange(1, n):
		pos = i-1
		while pos > -1 and A[i] <= A[pos]:
			pos = ans[pos]
		ans[i] = pos

	return ans

def get_nearest_less_right_jumping(A):
	n = len(A)
	ans = [n] * n

	for i in xrange(n-2, -1, -1):
		pos = i+1
		while pos < n and A[i] <= A[pos]:
			pos = ans[pos]
		ans[i] = pos

	return ans


# using a stack  and we keep elements increasing in the stack
def get_nearest_less_left_stack(A):
	n = len(A)
	ans = [-1] * n

	stack = []
	for i in xrange(0, n):
		while len(stack) and A[stack[-1]] >= A[i]:
			stack.pop()

		if not len(stack):
			ans[i] = -1
		else:
			ans[i] = stack[-1]

		stack.append(i)

	return ans

def get_nearest_less_right_stack(A):
	n = len(A)
	ans = [n] * n

	stack = []
	for i in xrange(n-1, -1, -1):
		while len(stack) and A[stack[-1]] >= A[i]:
			stack.pop()

		if not len(stack):
			ans[i] = n
		else:
			ans[i] = stack[-1]

		stack.append(i)

	return ans



class Solution1(object):
	# @param A : list of integers
	# @return an integer
	def largestRectangleArea(self, A):
		n = len(A)
		if n == 0:
			return 0

		left = get_nearest_less_left_jumping(A)
		right = get_nearest_less_right_stack(A)
		ans = 0
		for i in xrange(n):
			l_pos = left[i]
			r_pos = right[i]

			ans = max(ans, (r_pos - l_pos - 1) * A[i])

		return ans



"""
	Above will work and the time complexity is O(n).
	But we need extra space to store 2 lists of :left, right
	 
	For this particular problem, we can save some space:
	
	as we try to get nearest less pos using stack, for every pos X, 
	we could use height A[x] and get nearest left less at the same time.
	
	The only problem is how to get nearest less position to the right.
	
	the Key here is:
	
	at any pos X, before we push X into the stack,
	let say the stack now looks like:
	
	s1, s2, s3, s4
	we know that A[s1] is the nearest less pos to s2.
	A[s2] is the nearest less pos to s3, and so on....
	
	so now, for X, we calculate for those s3, s4 ...
	
	we know for s4, the nearest less left pos is s3
	and the nearest less right pos is X (if A[X]<= A[s4] otherwise we push X and continue)
	so for the rectangle of height A[s4], left bound is s3 and right bound is X
	
	and so on for s3, s2, ... until a si : A[si] < A[X] 
"""


class Solution2(object):
	# @param A : list of integers
	# @return an integer
	def largestRectangleArea(self, A):
		A.append(0)  # make things easier so we don't need to handle the boundary
		stack = []
		ans = 0

		for i in xrange(len(A)):
			while len(stack) and A[stack[-1]] >= A[i]:
				h = A[stack.pop()]
				l_pos = stack[-1] if len(stack) else -1
				r_pos = i
				ans = max(ans, h * (r_pos-l_pos-1))
			stack.append(i)

		return ans
