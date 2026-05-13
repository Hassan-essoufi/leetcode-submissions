from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = Counter(nums)
        for i in range(len(nums)):
            if  h[nums[i]]> len(nums)//2:
                maj = nums[i]
        return maj