class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opp = ('+', '-', '/', '*')

        for t in tokens:
            if t in opp:
                pop2, pop1 = int(stack.pop()), int(stack.pop())
                if t == '+':
                    stack.append(pop1 + pop2)
                if t == '-':
                    stack.append(pop1 - pop2)
                if t == '*':
                    stack.append(pop1 * pop2)
                if t == '/':
                    stack.append(int(pop1 / pop2))
            else:
                stack.append(int(t))      


        return stack[0] 