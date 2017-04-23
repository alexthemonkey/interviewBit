"""
Ways To Form Max Heap

https://www.interviewbit.com/problems/ways-to-form-max-heap/


Max Heap is a special kind of complete binary tree in which for every node the value present in that node is greater than the value present in its children nodes. 
If you want to know more about Heaps, please visit this link

So now the problem statement for this question is:

How many distinct Max Heap can be made from n distinct integers

In short, you have to ensure the following properties for the max heap :

Heap has to be a complete binary tree 
( A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible)
Every node is greater than all its children.
"""

f = [-1] * 101
C = [[1] * 101 for _ in xrange(101)]
MOD = 10 ** 9 + 7

def prepareC():
	for i in xrange(2, 101):
		for j in xrange(1, i):
			C[i][j] = (C[i-1][j] + C[i-1][j-1]) % MOD

# using f to save the calculated values  =>  memorized search
# which is common when try to solve DP problem with DFS.
def calculate(n):
	if n <= 1:
		return 1

	if f[n] >= 0:
		return f[n]

	level = 0
	m = n
	while True:
		level_num = (1<<level)
		if m-level_num < 0:
			break
		m -= level_num
		level += 1

	v = (1<<(level-1))
	num = min(m, v)
	num += v-1
	ans = (((C[n-1][num] * calculate(num)) % MOD ) * calculate(n-1-num)) % MOD

	f[n] = ans
	return ans


class Solution(object):
	# @param A : integer
	# @return an integer
	def solve(self, A):
		prepareC()
		return calculate(A)
