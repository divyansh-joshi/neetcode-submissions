class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap = dict()
        counter = 0
        for s in s1:
            hashmap[s] = 1 + hashmap.get(s, 0)
        left, right = 0, 0
        window_size = len(s1)
        if window_size > len(s2):
            return False
        for i in range(window_size):
            curr = s2[i]
            hashmap[curr] = hashmap.get(curr, 0) - 1
        j = 0
        for i in range(window_size, len(s2)):
            if max(hashmap.values()) == 0:
                return True
            else:
                hashmap[s2[i]] = hashmap.get(s2[i], 0) - 1
                hashmap[s2[j]] = hashmap.get(s2[j], 0) + 1
                j += 1
        if max(hashmap.values()) == 0:
                return True
        return False