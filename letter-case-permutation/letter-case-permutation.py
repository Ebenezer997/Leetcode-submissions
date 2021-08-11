class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        output = [""]
        
        for c in s:
            temp = []
            if c.isalpha():
                for i in output:
                    temp.append(i+c.lower())
                    temp.append(i+c.upper())
            else:
                for i in output:
                    temp.append(i+c)
            output = temp
                
        return output 
        