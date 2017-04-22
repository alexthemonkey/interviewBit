"""
Anagrams

https://www.interviewbit.com/problems/anagrams/

Given an array of strings, return all groups of strings that are anagrams. Represent a group by a list of integers representing the index in the original list. Look at the sample case for clarification.

Anagram :  a word, phrase, or name formed by rearranging the letters of another, 
such as 'spar' formed from 'rasp'

Input : cat dog god tca
Output : [[1, 4], [2, 3]]

cat and tca are anagrams which correspond to index 1 and 4. 
dog and god are another set of anagrams which correspond to index 2 and 3.
The indices are 1 based ( the first element has index 1 instead of index 0).
"""

"""
	Observation:
		if str1 and str2 are anagrams,
		then if we sort letters in str1 and letters in str2
		after sorting, they should be the same
"""

from collections import defaultdict


class Solution(object):
	# @param A : tuple of strings
	# @return a list of list of integers
	def anagrams(self, A):
		list_pos_of = defaultdict(list)
		for idx, value in enumerate(A):
			key = "".join(sorted(list(value)))
			list_pos_of[key].append(idx+1)

		ans = list_pos_of.values()
		ans.sort()
		return ans