class Solution:
    def isValid(self, s: str) -> bool:
        #create a dictionary with matching pairs of parenthesis
        store = {')':'(',']':'[','}':'{'}
        
        #create empty stack to contain strings
        stack = []
        
        ##loop through S
        for i in s:
            # if i not closing a parenthesis we add it to the stack
            if i not in store.keys():
                stack.append(i)
            #if it is , we chack if stack not empty and check if they are pairs
            else:
                if len(stack)>0 and store[i] == stack[-1] :
                    #they are pairs we pop it 
                    stack.pop()
                #if are not we return false
                else:
                    return False
        #at the end we return ==[]
        return stack == []
        
        #big 0 is linear(0(n)) and space 0(n)
        