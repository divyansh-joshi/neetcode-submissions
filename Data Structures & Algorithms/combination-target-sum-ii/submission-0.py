class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.answer = []
        candidates.sort()
        def rec(candidates, target, total, index, curr):
            if total == target:
                self.answer.append(curr.copy())
                return
            if index >= len(candidates) or total > target:    
                return

            # pick
            temp = -1
            for i in range(index, len(candidates)):
                if candidates[i] != temp:
                    # probable pick
                    curr.append(candidates[i])
                    rec(candidates, target, total+candidates[i], i+1, curr)
                    temp = candidates[i]
                    curr.pop()
                    
        rec(candidates, target, 0, 0, [])
        return self.answer