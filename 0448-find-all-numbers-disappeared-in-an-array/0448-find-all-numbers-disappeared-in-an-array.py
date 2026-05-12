class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set(nums)
        miss = []
        for x in range(1,len(nums)+1):
            if x not in s:
                miss.append(x)
        return miss