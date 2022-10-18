class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        output = []
        
        for i in s:
            if len(output) == 0:
                output.append(i)
            elif i != output[-1]:
                output.append(i)
            else:
                output.pop()
        return ''.join(output)
            
       
      
        