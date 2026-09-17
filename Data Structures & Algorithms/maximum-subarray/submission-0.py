class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        rolling_sum = 0
        answer = -10**9
        for i in range(len(nums)):
            curr = nums[i]
            if rolling_sum >= 0:
                answer = max(answer, curr+rolling_sum)
                rolling_sum += curr
            else:
                answer = max(answer, curr)
                rolling_sum = curr
        return answer