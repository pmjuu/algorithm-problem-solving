class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for bracket in s:
            if (len(stack) and (
                (bracket == ')' and stack[-1] == '(')
                or (bracket == ']' and stack[-1] == '[')
                or (bracket == '}' and stack[-1] == '{'))
               ):
                stack.pop()
                continue
            
            stack.append(bracket)
        
        return not bool(len(stack))