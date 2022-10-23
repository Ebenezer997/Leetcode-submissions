class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        x = []
        c = []
        
        for i in s:
            if len(x) == 0:
                x.append(i)
                c.append(1)
            else:
                if x[-1] == i:
                    c[-1] += 1
                    if c[-1] == k:
                        x.pop()
                        c.pop()
                else:
                    x.append(i)
                    c.append(1)
        res = ''
        for i in range(len(x)):
            res += x[i]*c[i]
        return res
                    
                
        