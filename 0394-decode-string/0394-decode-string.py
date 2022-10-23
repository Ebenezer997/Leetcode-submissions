class Solution:
    def decodeString(self, s: str) -> str:
        stack= []
        
        for i in range(len(s)):
            if s[i]  != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    c = stack.pop()
                    substr = c + substr
                #pop the closed bracket "["
                stack.pop()
                #find the number 
                n = ""
                while stack and stack[-1].isdigit():
                    nums = stack.pop()
                    n = nums + n
                stack.append(int(n)*substr)
        return "".join(stack)
                
                
        