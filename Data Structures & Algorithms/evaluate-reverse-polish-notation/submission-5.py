class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[-1])
        opers = ['+', '-', '*', '/']
        stack = []

        res = 0

        for o in tokens:
            if o in opers:
                n2 = int(stack.pop())
                n1 = int(stack.pop())

                if o == "+":
                    res = n1 + n2
                elif o == "-":
                    res = n1 - n2
                elif o == "*":
                    res = n1 * n2
                else:
                    res = int(n1/n2)
                
                stack.append(res)

            else:
                stack.append(o)

        return stack[-1]
