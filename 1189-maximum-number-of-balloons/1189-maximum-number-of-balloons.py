from collections import Counter
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        counts = Counter(text)
        p = { 'b': 1, 'a': 1, 'n': 1, 'l': 2, 'o': 2}
        k = []
        for c in p:
            if c not in text:
                return 0
            k.append(counts[c]//p[c])
        return min(k)