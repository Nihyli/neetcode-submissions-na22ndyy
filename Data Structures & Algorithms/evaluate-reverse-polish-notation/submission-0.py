class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        total = 0
        currentNum = 0 
        num1, num2 = 0, 0
        operators = {
            "+" : lambda x,y: x+y,
            "-" : lambda x,y: x-y,
            "/" : lambda x,y: int(x/y),
            "*" : lambda x,y: x*y
        }
        
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(int(tokens[i]))
            else:
                num2, num1 = stack.pop(), stack.pop()
                currentNum = operators[tokens[i]](num1,num2)
                stack.append(currentNum)
        
        return stack[0]

                

            



    