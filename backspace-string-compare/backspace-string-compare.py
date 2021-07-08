class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_out, t_out = [], []
        
        for char in s:
            if char == '#':
                if s_out: 
                    s_out.pop()
            else: 
                s_out.append(char)
            
        for char in t:
            if char == '#':
                if t_out: t_out.pop()
            else: 
                t_out.append(char)
        
        return s_out == t_out
#         string1 = []
#         string2 = []
        
#         for i in s:
#             if i == "#":
#                 if len(string1) >= 1:
#                     string1.pop()
#                 else:
#                     string1.append(i)
        
#         for i in t:
#             if i == "#":
#                 if len(string2) >= 1:
#                     string2.pop()
#                 else:
#                     string2.append(i)
                    
#         return string1 == string2
    
    
        
            
            
            
            
            
        