"""
Merge Intervals

https://www.interviewbit.com/problems/merge-intervals/

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].

Example 2:

Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

Make sure the returned intervals are also sorted.
"""


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
	# @param intervals, a list of Intervals
	# @param new_interval, a Interval
	# @return a list of Interval
	def insert(self, intervals, new_interval):
		ans = []
		for interval in intervals:
			if new_interval.start >= interval.start and new_interval.end <= interval.end:
				return intervals
			elif new_interval.start <= interval.start and new_interval.end >= interval.end:
				continue
			elif interval.start <= new_interval.start <= interval.end:
				new_interval.start = interval.start
			elif interval.start <= new_interval.end <= interval.end:
				new_interval.end = interval.end
			else:
				ans.append(interval)

		ans.append(new_interval)
		ans.sort(key = lambda interval: interval.start)
		return ans
