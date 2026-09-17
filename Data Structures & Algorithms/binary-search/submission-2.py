class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [-1,0,2,4,6,8]
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1