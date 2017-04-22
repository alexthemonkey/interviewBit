"""
Longest Substring Without Repeat

https://www.interviewbit.com/problems/longest-substring-without-repeat/


Given a string, 
find the length of the longest substring without repeating characters.

Example:

The longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.

For "bbbbb" the longest substring is "b", with the length of 1.
"""


class Solution(object):
	# @param A : string
	# @return an integer
	def lengthOfLongestSubstring(self, A):
		if not A:
			return 0

		left, right = 0, 1
		cnt = {A[0]: 1}
		ans = 1

		while right < len(A):
			# no duplicates, go on => right += 1
			if cnt.get(A[right], 0) == 0:
				ans = max(right-left+1, ans)
				cnt[A[right]] = 1
				right += 1
			else:
				# have duplicates, let right stay and wait for the left to increase
				cnt[A[left]] -= 1
				left += 1

		return ans
