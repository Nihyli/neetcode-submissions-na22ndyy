class Solution:
    def isValid(self, s: str) -> bool:

        brackets = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for char in s:
            if char in brackets:
                if not stack or brackets[char] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return not stack


