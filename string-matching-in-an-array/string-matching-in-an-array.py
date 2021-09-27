class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key = len)
        v = set()
        
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if words[i] in words[j]:
                    v.add(words[i])
        return v