class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.answer = []
        def rec(nums, target, curr, index):
            if index >= len(nums):
                if target == 0:
                    self.answer.append(curr.copy())
                    return
                else:
                    return
            # pick allowed?
            if target >= nums[index]:
                curr.append(nums[index])
                rec(nums, target-nums[index], curr, index)
                
                # not pick undo
                curr.pop()
            
            # not pick
            rec(nums, target, curr, index+1)
        
        curr = []
        rec(nums, target, curr, 0)
        return self.answer