class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        if words is None or len(words)<1:
            return ""
        ans=''
        # Creating set to maintain the prefixes encountered
        prefixes=set()
        prefixes.add("")
        size=0
        # This sorts the words lexicographically
        words.sort()
        # Traversing all the words in the input
        for word in words:
            # Checking if their prefixes are previously encountered
            if word[:-1] in prefixes:
                # Since the prefix exists, I am updating the ans if current word's length is greater than the ans length
                if len(word)>size:
                    size=len(word)
                    ans=word
                # Adding the current word to the prefix set
                prefixes.add(word)
        
        return ans