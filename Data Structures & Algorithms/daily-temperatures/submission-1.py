class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = list()
        answer = [0]*len(temperatures)
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                a, stack_index = stack.pop()
                answer[stack_index] = (index - stack_index)
            stack.append([temp, index])
        return answer