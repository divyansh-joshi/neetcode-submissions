class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1]*(len(nums)+1)
        def rec(nums, index):
            if index == 0:
                return nums[index]
            if index < 0:
                return 0
            if dp[index]!=-1:
                return dp[index]
            
            option1 = rec(nums, index-2) + nums[index]
            option2 = rec(nums, index-1)

            dp[index] = max(option1, option2)
            return dp[index]
        return rec(nums, len(nums)-1)