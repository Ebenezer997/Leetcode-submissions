class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_len = len(digits)
        
        for i in reversed(range(digits_len)):
            digits[i] += 1
            if digits[i] < 10:
                return digits
            
            else:
                digits[i] = 0
        if digits[0] == 0:
            digits.insert(0,1)
        return digits
        
        