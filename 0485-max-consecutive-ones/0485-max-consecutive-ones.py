class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        streaks = []
        streak = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                streak += 1
                streaks.append(streak)
            else:
                streak = 0
        return max(streaks) if streaks else 0