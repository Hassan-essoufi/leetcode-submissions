class Solution(object):
    def tribonacci(self, n):
        memo = {0: 0, 1: 1, 2: 1}

        def dp(n):
            if n in memo:
                return memo[n]

            memo[n] = dp(n - 1) + dp(n - 2) + dp(n - 3)
            return memo[n]

        return dp(n)
        