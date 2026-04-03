class Solution:
    def isValid(self, s: str) -> bool:
        """
        Given a string with container characters
        string is valid if every open container is closed by the same container type
        every close bracket has an open bracket
        and if they are in the right container
        """
        
        hmap = {")":"(", "}": "{", "]": "["}
        stack = []

        for c in s:
            if c not in hmap:
                stack.append(c)
                continue           
            else:
                if not stack or hmap[c] != stack[-1]:
                    return False
            stack.pop()
        return not stack

        

        
        

            


        

