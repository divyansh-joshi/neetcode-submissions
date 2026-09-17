class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.answer = []
        def rec(nums, index, curr):
            if index >= len(nums):
                self.answer.append(curr.copy())
                return
            
            # pick
            curr.append(nums[index])
            rec(nums, index+1, curr)

            # not pick
            curr.pop()
            rec(nums, index+1, curr)
        rec(nums, 0, list())
        return self.answer