class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for i in range(m)]
        def rec(i, j, m, n):
            if i == 0 and j == 0:
                return 1
            if i < 0 or j < 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            top = rec(i-1, j, m, n)
            left = rec(i, j-1, m, n)

            dp[i][j] = top+left
            return dp[i][j]
        return rec(m-1, n-1, m, n)