class Solution:
    def removeDuplicates(self, s: str, k: int) -> str: 
        x = []
        c = []
        for i in s:
            if len(x) == 0:
                x.append(i)
                c.append(1)
            else:
                if(x[-1] != i):
                    x.append(i)
                    c.append(1)
                else:
                    c[-1] += 1
                    if(c[-1] == k):
                        x.pop()
                        c.pop()
        ans = ""
        for i in range(len(x)):
            ans += c[i] *(x[i])
        return (ans)
     
            
                