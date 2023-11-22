class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        
        for token in tokens:
            if token in operators:
                second_num = stack.pop()
                first_num = stack.pop()
                evaluation = eval(first_num + token + second_num)

                stack.append(str(int(evaluation)))
            else:
                stack.append(token)

        return int(stack[0])