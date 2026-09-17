class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        i, j = 0, 0
        nums.sort()
        while i < len(nums) and nums[i] <= 0:
            ii = nums[i]
            j = i + 1
            k = len(nums)-1
            while k > j:
                curr = nums[i] + nums[j] + nums[k]
                if curr == 0:
                    answer.append([nums[i], nums[j], nums[k]])
                    ii, jj, kk = nums[i], nums[j], nums[k]
                    while j < len(nums) and nums[j] == jj:
                        j += 1
                    while k >= 0 and nums[k] == kk:
                        k -= 1
                elif curr > 0:
                    k -= 1
                else:
                    j += 1
            
            while i < len(nums) and nums[i] == ii:
                i += 1
        return answer
            