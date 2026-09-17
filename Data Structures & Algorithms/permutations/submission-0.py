class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.answer = []
        def rec(nums, index, curr, hashmap):
            if index == len(nums):
                self.answer.append(curr.copy())
                return 
            
            for i in range(len(nums)):
                if i not in hashmap:
                    # lets pick
                    curr.append(nums[i])
                    hashmap[i] = 1
                    rec(nums, index+1, curr, hashmap)
                    curr.pop()
                    hashmap.pop(i)
        rec(nums, 0, [], {})
        return self.answer