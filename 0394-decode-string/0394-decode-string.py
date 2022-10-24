class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            
            else:
                substr = ""
                while stack[-1] != "[":
                    c = stack.pop()
                    substr = c + substr
                stack.pop()
                n = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop()
                    n = num + n
                stack.append(int(n)*substr)
        return "".join(stack)
                
        
        