from collections import Counter
class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        lucky = -1
        counts = Counter(arr)
        for x in arr:
            if x == counts[x]:
                lucky = max(x,lucky)
        return lucky
        