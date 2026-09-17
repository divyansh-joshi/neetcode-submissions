class Solution:
    def climbStairs(self, n: int) -> int:
        dp = dict()
        def rec(n, curr):
            if curr >= n-1:
                return 1
            if curr in dp:
                return dp[curr]
            option1 = rec(n, curr + 1) # one step
            option2 = rec(n, curr + 2)

            dp[curr] = option1 + option2
            return dp[curr]
        return rec(n, 0)