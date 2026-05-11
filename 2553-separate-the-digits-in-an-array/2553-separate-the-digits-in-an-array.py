class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def numbers(n):
            if n < 10:
                return [n]
            l = []
            while n > 9:
                  l.append(n%10)
                  n = n//10
            l.append(n)
            return reversed(l)
        p = []
        for num in nums:
            p += numbers(num)
        return p
