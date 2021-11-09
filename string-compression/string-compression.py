class Solution:
    def compress(self, chars: List[str]) -> int:
       #count to count the values
        #two pointers i and j: i initialize at zero position and j is looped
        #check if j is not out of the range and j position is equal to the previous one we increase count by 1
        # j is not same value with previous . the i position is overide by chars[j-1]
        #and increase i by 1
        #if count is greater than 1 we loop through count and return each element
        
        i = 0
        count = 1
        
        for j in range(1,len(chars)+1):
            if j < len(chars) and chars[j] == chars[j-1]:
                count += 1
            else:
                chars[i] = chars[j-1]
                i += 1
                if count > 1:
                    for k in str(count):
                        chars[i] = k
                        i += 1
                count = 1
        
        return i
                        