class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters)-1
        res = letters[0]
        
        while left<=right:
            mid = left +(right-left)//2
            if letters[mid] <= target:
                left = mid +1
            
            else:
                res = letters[mid]
                right = mid -1
        return res
            
        