class Solution:
    def isValid(self, s: str) -> bool:
        store = {")":"(","}":"{","]":"["}
        stack = []
        
        for i in s:
            if i in store.values():
                stack.append(i)
            else:
                if len(stack)>0 and store[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return stack == []