class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        duplicate = set()
        left, right = 0, 0
        answer = 0
        while right < len(s):
            curr = s[right] # optimistic
            if curr not in duplicate:
                answer = max(answer, right-left+1)
                duplicate.add(curr)
                right += 1
            else:
                duplicate.remove(s[left])
                left += 1
        return answer