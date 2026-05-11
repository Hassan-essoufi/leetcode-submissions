class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        mapping = {}
        words = s.split()
        if len(pattern) != len(words):
            return False
        for i in range(len(pattern)) :
            if pattern[i] not in mapping:
                if words[i] not in mapping.values():
                    mapping[pattern[i]] = words[i]
                else:
                    return False

            elif mapping[pattern[i]] != words[i]:
                return False
        return True