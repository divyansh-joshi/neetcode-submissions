class Solution:
    def trap(self, height: List[int]) -> int:
        left = []
        right = [0]* len(height)
        maxi = 0
        for h in height:
            maxi = max(maxi, h)
            left.append(maxi)
        maxi = 0
        for i in range(len(height)-1, -1, -1):
            maxi = max(maxi, height[i])
            right[i] = maxi
        
        water = 0
        for i in range(len(height)):
            water += max(min(left[i], right[i])-height[i], 0)
        return water