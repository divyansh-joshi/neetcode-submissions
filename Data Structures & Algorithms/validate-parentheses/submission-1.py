class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for char in s:
            if char in ["[", "{", "("]:
                stack.append(char)
            else:
                if char == "]":
                    if len(stack) == 0 or stack[-1] != "[":
                        return False
                    else:
                        stack.pop()
                if char == "}":
                    if len(stack) == 0 or stack[-1] != "{":
                        return False
                    else:
                        stack.pop()
                if char == ")":
                    if len(stack) == 0 or stack[-1] != "(":
                        return False
                    else:
                        stack.pop()
        return len(stack) == 0