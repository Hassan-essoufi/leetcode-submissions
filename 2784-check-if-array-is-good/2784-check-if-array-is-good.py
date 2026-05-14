from collections import Counter
class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counts = Counter(nums)
        for i  in range(len(nums)):
            if nums[i] > len(nums)-1:
                return False
            elif nums[i] == len(nums)-1:
                if counts[nums[i]] != 2:
                    return False
            else:
                if counts[nums[i]] != 1:
                    return False
        return True