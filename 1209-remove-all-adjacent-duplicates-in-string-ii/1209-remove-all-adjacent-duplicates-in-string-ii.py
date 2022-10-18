class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        x = []
        c = []
        
        for i in s:
            if len(x) == 0:
                x.append(i)
                c.append(1)
            
            else:
                if i == x[-1]:
                    c[-1]+= 1
                    if (c[-1] == k):
                        x.pop()
                        c.pop()
                else:
                    x.append(i)
                    c.append(1)
        ans = ""
        for i in range(len(x)):
            ans += c[i]*x[i]
        return ans
                    