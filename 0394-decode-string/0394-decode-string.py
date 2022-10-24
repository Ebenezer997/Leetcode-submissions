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
                nums = ""
                while stack and stack[-1].isdigit():
                    n = stack.pop()
                    nums = n + nums
                stack.append(int(nums)*substr)
        return "".join(stack)
                    
                    
            