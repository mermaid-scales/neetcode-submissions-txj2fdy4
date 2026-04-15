class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        
        for word in strs:
            result += str(len(word)) + "#" + word
        
        return result


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        
        while i < len(s):
            # Step 1: get length
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            
            # Step 2: get word using length
            word = s[j+1 : j+1+length]
            result.append(word)
            
            # Step 3: move pointer
            i = j + 1 + length
        
        return result