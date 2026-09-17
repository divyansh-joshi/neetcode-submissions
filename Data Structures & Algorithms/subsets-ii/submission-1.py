class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.answer = []
        nums.sort()
        def rec(nums, index, curr):
            
            self.answer.append(curr.copy())
            temp = -1000
            # pick:
            for i in range(index, len(nums)):
                if nums[i] != temp:
                    curr.append(nums[i])
                    rec(nums, i+1, curr)
                    temp = nums[i]
                    curr.pop()
        rec(nums, 0, [])
        return self.answer