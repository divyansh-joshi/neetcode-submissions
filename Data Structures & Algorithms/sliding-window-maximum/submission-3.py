class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        left, right = 0, 0
        answer = []
        while right < len(nums):
            while deque and nums[deque[-1]] < nums[right]:
                deque.pop()
            deque.append(right)
            if left > deque[0]:
                deque.popleft()
            if k == right - left + 1:
                answer.append(nums[deque[0]])
                left += 1
            right += 1
        return answer