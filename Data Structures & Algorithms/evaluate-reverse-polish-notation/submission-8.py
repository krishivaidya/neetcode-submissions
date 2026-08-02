class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '+' and stack :
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
            elif i == '-' and  stack:
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            
            elif i == '*' and  stack:
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b)

            elif i == '/' and  stack:
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(i))
        if stack:
            return stack.pop()



            

        