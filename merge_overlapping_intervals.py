"""
Merge Overlapping Intervals

https://www.interviewbit.com/problems/merge-overlapping-intervals/

Given a collection of intervals, merge all overlapping intervals.

For example:

Given [1,3],[2,6],[8,10],[15,18],

return [1,6],[8,10],[15,18].

Make sure the returned intervals are sorted.

"""

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
	# @param intervals, a list of Intervals
	# @return a list of Interval
	def merge(self, intervals):
		n = len(intervals)
		if n <= 1:
			return intervals

		intervals.sort(key=lambda intv: intv.start)
		ans = []

		ans.append(intervals[0])
		for i in xrange(1, n):
			last_interval = ans[-1]
			new_interval = intervals[i]

			if new_interval.start > last_interval.end:
				ans.append(new_interval)
			elif new_interval.end <= last_interval.end:
				continue
			else:
				last_interval.end = new_interval.end

		return ans