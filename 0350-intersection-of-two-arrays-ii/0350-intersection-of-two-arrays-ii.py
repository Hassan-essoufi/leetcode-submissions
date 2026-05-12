from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s = []
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        for x in nums1:
            if x in nums2 and x not in s:
                    s = s + [x]*min(count1[x], count2[x])

        return s

            