class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def newFunc(mid, piles, h):
            answer = 0
            for p in piles:
                answer += p // mid
                if p % mid != 0:
                    answer += 1
            return answer <= h
        left = 1
        right = max(piles)
        answer = 10**9
        while right >= left:
            mid = (left + right) // 2
            if newFunc(mid, piles, h):
                
                answer = min(answer, mid)
                right = mid-1
            else:
                left = mid+1
        return answer