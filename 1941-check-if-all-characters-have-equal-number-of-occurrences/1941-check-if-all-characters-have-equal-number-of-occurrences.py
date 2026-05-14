from collections import Counter
class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p = Counter(s)
        for i in range(1,len(s)):
            if p[s[i]] != p[s[0]]:
                return False
        return True
