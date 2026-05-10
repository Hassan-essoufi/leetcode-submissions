class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        curr = 0
        nums= sorted(nums)        
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] > curr:
                curr = nums[i+1] - nums[i]
        return curr