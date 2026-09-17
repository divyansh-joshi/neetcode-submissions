class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while right >= left:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            # identify the sorted half
            if nums[mid] >= nums[left]: # First half is sorted
                if nums[left] <= target and target <= nums[mid]:
                    right = mid
                else:
                    left = mid+1
            elif nums[right] >= nums[mid]: # Second Half is sorted
                if nums[mid] <= target and target <= nums[right]:
                    left = mid
                else:
                    right = mid-1
           
        return -1