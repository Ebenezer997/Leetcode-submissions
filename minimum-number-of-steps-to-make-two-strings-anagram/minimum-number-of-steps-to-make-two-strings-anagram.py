class Solution:
    def minSteps(self, s: str, t: str) -> int:
        res = 0
        chars_to_match = set(s)
        for c in chars_to_match:
            to_add = s.count(c) - t.count(c)
            if to_add > 0:
				# If the count of c in t is less than the count of c in s, add the difference to the result:
                res += to_add
				
        return res