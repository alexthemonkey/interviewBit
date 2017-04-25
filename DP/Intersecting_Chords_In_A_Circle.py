"""
Intersecting Chords In A Circle

https://www.interviewbit.com/problems/intersecting-chords-in-a-circle/

Given a number N, return number of ways you can draw N chords in a circle with 2*N points such that no 2 chords intersect.
Two ways are different if there exists a chord which is present in one way and not in other.

For example,
N=2
If points are numbered 1 to 4 in clockwise direction, then different ways to draw chords are:
{(1-2), (3-4)} and {(1-4), (2-3)}

So, we return 2.

1 <= N <= 1000
Return answer modulo 109+7

"""

"""
	Let f(N) num of ways of drawing N chords of 2N points.
	
	we have 
		1. f(0) = 1
		2. f(N) = f(0)*f(N-1) + f(1)*f(N-2) + f(2)*f(N-3) ...
		
	It's Catalan number.
	
	so 
	
	F(N) = C(2N, N) / (n+1)
	and based on number theory:
	
	a ^ (p-1) = 1 (mod p) if p is a prime number and a p co-prime
	
	which also means: under mod p, a ^ (-1) = a ^ (p-2)
"""

def power(a, b, MOD):
	if b == 0:
		return 1

	ans = pow(a, b/2, MOD)
	ans *= ans
	ans %= MOD

	if b % 2 == 1:
		ans *= a

	return (ans % MOD)

def fact(n, MOD):
	ans = 1
	for i in xrange(2, n+1):
		ans *= i
		ans %= MOD
	return ans


class Solution(object):
	# @param A : integer
	# @return an integer
	def chordCnt(self, A):
		MOD = 10 ** 9 + 7
		fact_A = fact(A, MOD)
		fact_2A = fact(2*A, MOD)

		down = (fact_A * fact_A) % MOD
		ans = fact_2A * power(down, MOD-2, MOD)
		ans %= MOD

		ans *= power(A+1, MOD-2, MOD)
		ans %= MOD

		return ans
