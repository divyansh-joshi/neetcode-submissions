class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right, answer = 0, 0, 0
        hashmap = dict()
        while right < len(s):
            hashmap[s[right]] = 1 + hashmap.get(s[right], 0)
            max_freq = max(list(hashmap.values()))
            if max_freq + k >= right-left+1:
                answer = max(answer, right-left+1)
            else:
                if left < len(s) and s[left] in hashmap and hashmap[s[left]] == 1:
                    hashmap.pop(s[left])
                elif left < len(s) and  s[left] in hashmap:
                    hashmap[s[left]] -= 1
                left += 1
            right += 1
        return answer