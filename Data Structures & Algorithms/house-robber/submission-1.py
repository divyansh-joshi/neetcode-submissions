class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            take = nums[i]
            if i-2 >= 0:
                take += dp[i-2]
            not_take = dp[i-1]
            dp[i] = max(take, not_take)
        return dp[-1]